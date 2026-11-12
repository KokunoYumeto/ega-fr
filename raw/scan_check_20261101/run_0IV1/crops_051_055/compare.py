import sys
from PIL import Image
# usage: compare.py out scale src1 x0 y0 x1 y1 [src2 x0 y0 x1 y1 ...]  -> side by side
out=sys.argv[1]; scale=float(sys.argv[2]); args=sys.argv[3:]
ims=[]
for i in range(0,len(args),5):
    src=args[i]; x0,y0,x1,y1=map(int,args[i+1:i+5])
    c=Image.open(src).convert('L').crop((x0,y0,x1,y1))
    ims.append(c.resize((int(c.width*scale),int(c.height*scale)),Image.LANCZOS))
W=sum(c.width for c in ims)+20*(len(ims)-1); H=max(c.height for c in ims)
canvas=Image.new('L',(W,H),255); x=0
for c in ims:
    canvas.paste(c,(x,0)); x+=c.width+20
canvas.save(out); print(out,canvas.size)
