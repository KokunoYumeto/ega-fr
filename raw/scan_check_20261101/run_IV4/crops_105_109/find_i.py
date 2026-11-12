import sys
import numpy as np
from PIL import Image
from scipy import ndimage
base=r"user/Documents/ega_scan_check_20261101/run_IV4/"
def find(page,strip,hmin,hmax,wmin,wmax,thr=128):
    im=np.array(Image.open(base+f"page_{page:03d}_s{strip}.png").convert('L'))
    d=im<thr
    lab,n=ndimage.label(d)
    objs=ndimage.find_objects(lab)
    info=[]
    for i,sl in enumerate(objs,1):
        ys,xs=sl
        info.append((i,xs.start,ys.start,xs.stop,ys.stop,int((lab[sl]==i).sum())))
    dots=[t for t in info if 3<=t[3]-t[1]<=8 and 3<=t[4]-t[2]<=8]
    res=[]
    for t in info:
        i,x0,y0,x1,y1,ink=t
        w=x1-x0;h=y1-y0
        if hmin<=h<=hmax and wmin<=w<=wmax:
            # dot above: center x within body x-range (+3 px for slant), bottom of dot 2..10 px above top of body
            for dd in dots:
                _,dx0,dy0,dx1,dy1,dink=dd
                cx=(dx0+dx1)/2
                if x0-1<=cx<=x1+4 and 1<=y0-dy1<=10:
                    res.append(dict(x=x0,y=y0,w=w,h=h,ink=ink,dot=dink))
                    break
    return res
if __name__=='__main__':
    p,s,hmin,hmax,wmin,wmax=[int(a) for a in sys.argv[1:7]]
    for r in find(p,s,hmin,hmax,wmin,wmax): print(r)
