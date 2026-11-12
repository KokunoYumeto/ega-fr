import numpy as np
from PIL import Image
base=r"user/Documents/ega_scan_check_20261101/run_IV4/"
def stem(page,strip,box,thr=128):
    im=np.array(Image.open(base+f"page_{page:03d}_s{strip}.png").convert('L').crop(box))
    d=im<thr
    rows=np.nonzero(d.any(1))[0]
    # split dot from body: find gap rows
    groups=[];start=rows[0];prev=rows[0]
    for r in rows[1:]:
        if r!=prev+1: groups.append((start,prev)); start=r
        prev=r
    groups.append((start,prev))
    body=max(groups,key=lambda g:g[1]-g[0])
    b0,b1=body
    h=b1-b0+1
    mid=range(b0+h//4,b1-h//4+1)
    runs=[]
    for r in mid:
        row=d[r];best=0;cnt=0
        for v in row:
            if v: cnt+=1;best=max(best,cnt)
            else: cnt=0
        runs.append(best)
    return dict(groups=groups,body_h=int(h),ink_body=int(d[b0:b1+1].sum()),ink_all=int(d.sum()),stem_med=float(np.median(runs)),stem_mean=round(float(np.mean(runs)),2))
