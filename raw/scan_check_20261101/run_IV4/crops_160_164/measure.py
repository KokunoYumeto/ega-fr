import sys
from PIL import Image
import numpy as np
# usage: measure.py page strip x0 y0 x1 y1  -> prints dark-pixel bounding boxes of connected blobs
p,s,x0,y0,x1,y1=[int(a) for a in sys.argv[1:7]]
thr=int(sys.argv[7]) if len(sys.argv)>7 else 128
base=r"user\Documents\ega_scan_check_20261101\run_IV4"
im=np.array(Image.open(rf"{base}\page_{p:03d}_s{s}.png").convert('L'))
reg=im[y0:y1,x0:x1]<thr
from scipy import ndimage
lab,n=ndimage.label(reg)
objs=ndimage.find_objects(lab)
res=[]
for i,o in enumerate(objs):
    ys,xs=o
    h=ys.stop-ys.start; w=xs.stop-xs.start
    cnt=(lab[o]==i+1).sum()
    res.append((xs.start+x0,ys.start+y0,w,h,cnt))
res.sort()
for r in res:
    if r[4]>5: print("x=%d y=%d w=%d h=%d n=%d"%r)
