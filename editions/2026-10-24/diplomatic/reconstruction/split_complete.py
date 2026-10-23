"""Recover the cover and five complete documents from the direct cumulative TeX."""
from pathlib import Path
import argparse
import hashlib
import re

IDS=['COVER','BASE','IV1','IV2','IV3','IV4']
PATTERN=re.compile(rb'^% EGA-COMPONENT-BEGIN ([A-Z0-9]+) ([A-F0-9]{64})\n(.*?)^% EGA-COMPONENT-END \1\n',re.M|re.S)

def extract(data):
    matches=list(PATTERN.finditer(data))
    if [m[1].decode() for m in matches]!=IDS:
        raise ValueError('Missing, repeated or reordered source document')
    result={}
    for match in matches:
        if hashlib.sha256(match[3]).hexdigest().upper().encode()!=match[2]:
            raise ValueError('Source content hash mismatch')
        result[match[1].decode()]=match[3]
    return result

def main():
    p=argparse.ArgumentParser(description='Extraire les six documents complets, couverture comprise.')
    p.add_argument('source',type=Path);p.add_argument('destination',type=Path)
    a=p.parse_args();parts=extract(a.source.read_bytes())
    a.destination.mkdir(parents=True,exist_ok=False)
    for key,body in parts.items():
        with (a.destination/(key+'.tex')).open('xb') as f:f.write(body)

if __name__=='__main__':main()
