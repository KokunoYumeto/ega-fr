import sys
from PIL import Image
# usage: ink.py src x0 y0 x1 y1 [thr]  -> dark-pixel count and bbox of dark pixels
src=sys.argv[1]; x0,y0,x1,y1=map(int,sys.argv[2:6]); thr=int(sys.argv[6]) if len(sys.argv)>6 else 128
im=Image.open(src).convert('L').crop((x0,y0,x1,y1))
px=im.load(); W,H=im.size
pts=[(x,y) for y in range(H) for x in range(W) if px[x,y]<thr]
if not pts: print('none'); sys.exit()
xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
bw=max(xs)-min(xs)+1; bh=max(ys)-min(ys)+1
print(f'{src} ink={len(pts)} bbox={bw}x{bh} density={len(pts)/(bw*bh):.2f}')
