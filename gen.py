from utils import d,n
from Crypto.Util.number import isPrime, getRandomRange

def gen_key():
    a = []
    s = 0
    for i in range(n):
        t = getRandomRange(max(2**(d*n-n+i-1), s+1), 2**(d*n-n+i))
        s += t
        a.append(t)
    m = getRandomRange(max(2**(d*n-1), s+1), 2**(d*n))
    while not isPrime(m):
        m = getRandomRange(max(2**(d*n-1), s+1), 2**(d*n))
    u = getRandomRange(1, m)
    w = pow(u, m-2, m)
    b = [x*u%m for x in a]
    private = {
        'm': m,
        'w': w,
        'a': a,
    }
    public = {
        'a': b,
    }
    return private, public

def gen_small_key():
    private = {
        'm': 181,
        'w': 62,
        'a': [12, 17, 47, 79],
    }
    public = {
        'a': [152, 155, 173, 156],
    }
    return private, public