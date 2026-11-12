import sys
from PIL import Image
import numpy as np
from scipy import ndimage
def run(src,x1,y1,x2,y2,minh=25,maxw=16):
    a=np.array(Image.open(src).convert('L'))
    sub=a[y1:y2,x1:x2]<128
    lab,n=ndimage.label(sub)
    res=[]
    for i in range(1,n+1):
        ys,xs=np.where(lab==i)
        w=xs.max()-xs.min()+1; h=ys.max()-ys.min()+1
        if h>=minh and w<=maxw:
            top,bot=ys.min(),ys.max(); hh=bot-top+1
            t=xs[ys<top+hh/4].mean(); b=xs[ys>bot-hh/4].mean()
            res.append((xs.min()+x1,ys.min()+y1,w,h,round((t-b)/hh,2)))
    for r in sorted(res): print('x=%d y=%d w=%d h=%d slant=%.2f'%r)
if __name__=='__main__':
    src=sys.argv[1]; x1,y1,x2,y2=map(int,sys.argv[2:6])
    run(src,x1,y1,x2,y2)
