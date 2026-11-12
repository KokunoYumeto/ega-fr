import sys
import numpy as np
from PIL import Image
from scipy import ndimage
base=r"user/Documents/ega_scan_check_20261101/run_IV4/"
def comps(page,strip,box,thr=128):
    x0,y0,x1,y1=box
    im=np.array(Image.open(base+f"page_{page:03d}_s{strip}.png").convert('L'))[y0:y1,x0:x1]
    d=im<thr
    lab,n=ndimage.label(d)
    out=[]
    for i,sl in enumerate(ndimage.find_objects(lab),1):
        ys,xs=sl
        m=(lab[sl]==i)
        out.append((x0+xs.start,y0+ys.start,x0+xs.stop,y0+ys.stop,int(m.sum())))
    out.sort()
    return out
def stemw(page,strip,box,thr=128):
    # mean horizontal run in middle half of body rows
    x0,y0,x1,y1=box
    im=np.array(Image.open(base+f"page_{page:03d}_s{strip}.png").convert('L'))[y0:y1,x0:x1]
    d=im<thr
    rows=np.nonzero(d.any(1))[0]
    if len(rows)==0: return None
    h=rows[-1]-rows[0]+1
    mid=range(rows[0]+h//4, rows[-1]-h//4+1)
    runs=[]
    for r in mid:
        best=cnt=0
        for v in d[r]:
            if v: cnt+=1; best=max(best,cnt)
            else: cnt=0
        if best: runs.append(best)
    return round(float(np.mean(runs)),2), int(d.sum()), int(h)
if __name__=='__main__':
    a=[int(x) for x in sys.argv[1:]]
    for c in comps(a[0],a[1],tuple(a[2:6])): print(c)
