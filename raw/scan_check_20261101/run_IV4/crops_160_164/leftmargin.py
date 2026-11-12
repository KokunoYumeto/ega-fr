import sys
from PIL import Image
import numpy as np
p,s=int(sys.argv[1]),int(sys.argv[2])
base=r"user\Documents\ega_scan_check_20261101\run_IV4"
im=np.array(Image.open(rf"{base}\page_{p:03d}_s{s}.png").convert('L'))
dark=im<128
rows=dark.sum(axis=1)
# find text lines: runs of rows with dark pixels
lines=[];inrun=False
for y,v in enumerate(rows):
    if v>3 and not inrun: start=y;inrun=True
    elif v<=3 and inrun:
        inrun=False
        if y-start>8: lines.append((start,y))
for (a,b) in lines:
    cols=np.where(dark[a:b].sum(axis=0)>0)[0]
    print("rows %d-%d  left=%d right=%d"%(a,b,cols.min(),cols.max()))
