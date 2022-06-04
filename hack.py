from frac import frac
from utils import d
import cvxpy as cp
from numpy import array
l = d+2
k = 100

def find_sol(a, b, c):
    x = cp.Variable(l, integer=True)
    obj = cp.Minimize(array(c)@x)
    cons = [array(a)@x<=array(b),x>=1]
    prob = cp.Problem(obj, cons)
    prob.solve(solver=cp.CPLEX)
    if prob.status == cp.OPTIMAL:
        return int(x.value[0])
    else:
        return 0

def find_sols(public):
    p = public['a']
    n = len(p)
    c = [1]
    a = []
    b = []
    sols = []
    for i in range(1,l):
        c.append(0)
        tmp = [0]*l
        tmp[0] = p[i]
        tmp[i] = -p[0]
        a.append(tmp)
        b.append(p[0]>>n-i)
        tmp = [0]*l
        tmp[0] = -p[i]
        tmp[i] = p[0]
        a.append(tmp)
        b.append(p[i]>>n)
        tmp = [0]*l
        tmp[i] = 1
        a.append(tmp)
        b.append(p[i]-1)
    tmp = [0]*l
    tmp[0] = 1
    a.append(tmp)
    b.append(p[i]-1)
    tmp = [0]*l
    tmp[0] = -1
    a.append(tmp)
    b.append(-1)
    for i in range(k):
        x = find_sol(a,b,c)
        if x <= 0 or x >= p[0]:
            break
        else:
            sols.append(x)
            b[-1] = -x-1
    return sols

def to_small_segs1(public, s):
    a = public['a']
    n = len(a)
    ret = []
    for x in s:
        t = [frac(x,a[0]), frac(x+1,a[0])]
        for i in range(1, n):
            l = (a[i]*x+a[0]-1)//a[0]
            r = (a[i]*(x+1)+a[0]-1)//a[0]
            for y in range(l,r):
                t.append(frac(y,a[i]))
        t.sort(reverse=False)
        m = len(t)
        for i in range(m-1):
            if t[i]!=t[i+1]:
                ret.append((t[i],t[i+1]))
    print(ret)
    return ret

def to_small_segs2(public, s):
    a = public['a']
    n = len(a)
    ret = []
    for p in s:
        l,r = p
        u = 0
        v = 0
        legal = True
        for i in range(n):
            d = l.a*a[i]//l.b
            x = a[i]-u
            y = d-v
            t = frac(y,x)
            if x>0 and t>l:
                l = t
            elif x<0 and t<r:
                r = t
            elif x==0 and y>=0:
                legal = False
            u += a[i]
            v += d
        v += 1
        t = frac(v,u)
        if t<r:
            r = t
        if legal and l<r:
            ret.append((l,r))
    return ret

def to_small_segs(public, s):
    return to_small_segs2(public, to_small_segs1(public, s))

def simple_frac(a, b, c, d):
    if a>=b:
        t = a//b
        r = simple_frac(a-b*t,b,c-d*t,d)
        return frac(r.a+t*r.b,r.b)
    if c>d:
        return frac(1,1)
    if a==0:
        return frac(1,d//c+1)
    r = simple_frac(d,c,b,a)
    return frac(r.b,r.a)

def seg_to_frac(s):
    l,r = s
    assert l<r
    return simple_frac(l.a, l.b, r.a, r.b)

def seg_to_fracs(s, x, y, d):
    f = seg_to_frac(s)
    ret = []
    if f.b>=y:
        return ret
    if f.b>=x:
        ret.append((f,d))
    l,r = s
    ret.extend(seg_to_fracs((l,f),x,y,d+1))
    ret.extend(seg_to_fracs((f,r),x,y,d+1))
    return ret

def segs_to_fracs(segs, x, y):
    ret = []
    for s in segs:
        ret.extend(seg_to_fracs(s,x,y,0))
    return ret
