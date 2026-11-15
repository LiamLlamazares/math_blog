import re,sys
def toks(d): return re.findall(r'[A-Za-z]|-?(?:\d+\.?\d*|\.\d+)(?:e-?\d+)?',d)
import math
def arc(x1,y1,rx,ry,phi,fa,fs,x2,y2):
    if rx==0 or ry==0: return [(x1,y1,x2,y2,x2,y2)]
    rx,ry=abs(rx),abs(ry); ph=math.radians(phi); c,s_=math.cos(ph),math.sin(ph)
    dx,dy=(x1-x2)/2,(y1-y2)/2; x1p=c*dx+s_*dy; y1p=-s_*dx+c*dy
    lam=x1p**2/rx**2+y1p**2/ry**2
    if lam>1: rx*=math.sqrt(lam); ry*=math.sqrt(lam)
    num_=rx*rx*ry*ry-rx*rx*y1p*y1p-ry*ry*x1p*x1p; den=rx*rx*y1p*y1p+ry*ry*x1p*x1p
    co=math.sqrt(max(0,num_/den))*(-1 if fa==fs else 1)
    cxp=co*rx*y1p/ry; cyp=-co*ry*x1p/rx
    cx=c*cxp-s_*cyp+(x1+x2)/2; cy=s_*cxp+c*cyp+(y1+y2)/2
    ang=lambda ux,uy,vx,vy: math.atan2(ux*vy-uy*vx,ux*vx+uy*vy)
    th1=ang(1,0,(x1p-cxp)/rx,(y1p-cyp)/ry); dth=ang((x1p-cxp)/rx,(y1p-cyp)/ry,(-x1p-cxp)/rx,(-y1p-cyp)/ry)
    if not fs and dth>0: dth-=2*math.pi
    if fs and dth<0: dth+=2*math.pi
    n=max(1,math.ceil(abs(dth)/(math.pi/2))); d=dth/n; t=4/3*math.tan(d/4); out=[]
    def pt(th): return (cx+rx*math.cos(th)*c-ry*math.sin(th)*s_, cy+rx*math.cos(th)*s_+ry*math.sin(th)*c)
    def dv(th): return (-rx*math.sin(th)*c-ry*math.cos(th)*s_, -rx*math.sin(th)*s_+ry*math.cos(th)*c)
    for k in range(n):
        a0=th1+k*d; a1=a0+d; p0=pt(a0); p1=pt(a1); d0=dv(a0); d1=dv(a1)
        out.append((p0[0]+t*d0[0],p0[1]+t*d0[1],p1[0]-t*d1[0],p1[1]-t*d1[1],p1[0],p1[1]))
    return out
def conv(path):
    s=open(path).read(); ops=[]
    for m in re.finditer(r'<(circle|path)\b([^>]*)>',s):
        kind,at=m.groups()
        a=dict(re.findall(r'([\w-]+)=[\'"]([^\'"]*)[\'"]',at))
        f=a.get('fill')
        if not f or f=='none': continue
        r,g,b=[int(f[i:i+2],16)/255 for i in (1,3,5)]
        ops.append(f'{r:.4f} {g:.4f} {b:.4f} rg')
        if kind=='circle':
            cx,cy,rr=float(a['cx']),float(a['cy']),float(a['r']); k=0.5523*rr
            P=lambda x,y:f'{x:.3f} {100-y:.3f}'
            ops+= [f'{P(cx+rr,cy)} m',f'{P(cx+rr,cy+k)} {P(cx+k,cy+rr)} {P(cx,cy+rr)} c',f'{P(cx-k,cy+rr)} {P(cx-rr,cy+k)} {P(cx-rr,cy)} c',
                   f'{P(cx-rr,cy-k)} {P(cx-k,cy-rr)} {P(cx,cy-rr)} c',f'{P(cx+k,cy-rr)} {P(cx+rr,cy-k)} {P(cx+rr,cy)} c','h f']
            continue
        t=toks(a['d']); i=0; x=y=sx=sy=0; cmd=None; lc=None
        def P(x,y): return f'{x:.3f} {100-y:.3f}'
        def num():
            nonlocal i; v=float(t[i]); i+=1; return v
        while i<len(t):
            if t[i].isalpha(): cmd=t[i]; i+=1
            if cmd in 'zZ': ops.append('h'); x,y=sx,sy; lc=None; continue
            rel=cmd.islower(); c=cmd.upper()
            if c=='M':
                nx,ny=num(),num()
                if rel: nx+=x; ny+=y
                x,y=sx,sy=nx,ny; ops.append(f'{P(x,y)} m'); cmd='l' if rel else 'L'; lc=None
            elif c=='L':
                nx,ny=num(),num()
                if rel: nx+=x; ny+=y
                x,y=nx,ny; ops.append(f'{P(x,y)} l'); lc=None
            elif c=='H':
                nx=num(); x=nx+x if rel else nx; ops.append(f'{P(x,y)} l'); lc=None
            elif c=='V':
                ny=num(); y=ny+y if rel else ny; ops.append(f'{P(x,y)} l'); lc=None
            elif c in 'CS':
                if c=='C': x1,y1=num(),num()
                else:
                    x1,y1=(2*x-lc[0],2*y-lc[1]) if lc else (x,y)
                    if False: pass
                x2,y2,nx,ny=num(),num(),num(),num()
                if rel:
                    if c=='C': x1+=x;y1+=y
                    x2+=x;y2+=y;nx+=x;ny+=y
                ops.append(f'{P(x1,y1)} {P(x2,y2)} {P(nx,ny)} c'); lc=(x2,y2); x,y=nx,ny
            elif c=='A':
                rx,ry,rot,fa,fs,nx,ny=[num() for _ in range(7)]
                if rel: nx+=x; ny+=y
                for seg in arc(x,y,rx,ry,rot,int(fa),int(fs),nx,ny): ops.append(f'{P(seg[0],seg[1])} {P(seg[2],seg[3])} {P(seg[4],seg[5])} c')
                x,y=nx,ny; lc=None
            else: raise SystemExit('unsupported '+cmd)
        ops.append('f*' if a.get('fill-rule')=='evenodd' or 'evenodd' in s else 'f')
        # fix: the previous 'h f' pattern; path ends with fill op
    stream='\n'.join(ops).encode()
    objs=[b'<</Type/Catalog/Pages 2 0 R>>',b'<</Type/Pages/Kids[3 0 R]/Count 1>>',
      b'<</Type/Page/Parent 2 0 R/MediaBox[0 0 100 100]/Contents 4 0 R/Resources<<>>>>',
      b'<</Length %d>>\nstream\n'%len(stream)+stream+b'\nendstream']
    out=b'%PDF-1.4\n'; offs=[]
    for n,o in enumerate(objs,1): offs.append(len(out)); out+=b'%d 0 obj\n'%n+o+b'\nendobj\n'
    x=len(out); out+=b'xref\n0 %d\n0000000000 65535 f \n'%(len(objs)+1)+b''.join(b'%010d 00000 n \n'%o for o in offs)
    out+=b'trailer<</Size %d/Root 1 0 R>>\nstartxref\n%d\n%%%%EOF'%(len(objs)+1,x)
    return out
for n in sys.argv[2:]:
    open(f'{sys.argv[1]}/{n}.pdf','wb').write(conv(f'/home/llamazar/github/math_blog/posts/Future/Magic/_kit/symbols/{n}.svg'))
