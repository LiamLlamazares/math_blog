import random, math, sys
p=0.9
ns=sorted(set(int(round(10**(k/50))) for k in range(50,201)))
out=open(sys.argv[1],'w'); out.write("n r1 r2 r3\n")
runs=[]
for seed in (24,13,26):
    r=random.Random(seed); s=0; est={}
    for i in range(1,10001):
        s+= r.random()<p
        if i in ns: est[i]=s/i
    runs.append(est)
for n in ns: out.write(f"{n} {runs[0][n]:.4f} {runs[1][n]:.4f} {runs[2][n]:.4f}\n")
out.close()
b=open(sys.argv[2],'w'); b.write("n y\n")
up=[(n,min(1.0,p+1.96*math.sqrt(p*(1-p)/n))) for n in ns]
lo=[(n,p-1.96*math.sqrt(p*(1-p)/n)) for n in ns]
for n,y in up: b.write(f"{n} {y:.4f}\n")
for n,y in reversed(lo): b.write(f"{n} {y:.4f}\n")
b.close()
print(p+1.96*math.sqrt(p*.1/24), 1.96*math.sqrt(p*.1/24),1.96*math.sqrt(p*.1/1000))
