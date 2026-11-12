import sys
from PIL import Image
import numpy as np
base=r"user/Documents/ega_scan_check_20261101/run_IV4/"
def glyph(page,strip,box,thr=128):
    im=np.array(Image.open(base+f"page_{page:03d}_s{strip}.png").convert('L').crop(box))
    dark=im<thr
    ys,xs=np.nonzero(dark)
    if len(xs)==0: return None
    # bounding box
    y0,y1,x0,x1=ys.min(),ys.max(),xs.min(),xs.max()
    d=dark[y0:y1+1,x0:x1+1]
    # horizontal run lengths per row
    runs=[]
    for r in d:
        cnt=0;best=0
        for v in r:
            if v: cnt+=1; best=max(best,cnt)
            else: cnt=0
        runs.append(best)
    return dict(ink=int(d.sum()),h=int(y1-y0+1),w=int(x1-x0+1),maxrun=max(runs),medrun=float(np.median([x for x in runs if x>0])))
if __name__=='__main__':
    args=sys.argv[1:]
    p,s=int(args[0]),int(args[1]); box=tuple(int(a) for a in args[2:6])
    print(glyph(p,s,box))
