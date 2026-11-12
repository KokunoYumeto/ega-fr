import sys
from PIL import Image
import numpy as np
from scipy import ndimage
p,s=int(sys.argv[1]),int(sys.argv[2])
x0,y0,x1,y1=map(int,sys.argv[3:7])
thr=int(sys.argv[7]) if len(sys.argv)>7 else 128
base=r"user\Documents\ega_scan_check_20261101\run_IV3"
im=np.array(Image.open(rf"{base}\page_{p}_s{s}.png").convert('L'))[y0:y1,x0:x1]
mask=im<thr
lab,n=ndimage.label(mask)
objs=ndimage.find_objects(lab)
rows=[]
for i,sl in enumerate(objs):
    area=(lab[sl]==i+1).sum()
    if area<15: continue
    rows.append((sl[1].start+x0,sl[0].start+y0,sl[1].stop+x0,sl[0].stop+y0,area))
rows.sort()
for r in rows: print(r)
