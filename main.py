from frac import frac
from gen import gen_key, gen_small_key
from crypto import encrypt, decrypt
from utils import d,n
from Crypto.Util.number import getRandomInteger
from hack import find_sols, segs_to_fracs, to_small_segs

def check_small_key():
    private, public = gen_small_key()
    for message in range(16):
        cipher = encrypt(message, public)
        decrypted = decrypt(cipher, private)
        assert message==decrypted
    print('check small key ok')

def check_key():
    private, public = gen_key()
    message = getRandomInteger(n)
    cipher = encrypt(message, public)
    decrypted = decrypt(cipher, private)
    assert message==decrypted
    print('check key ok')

def solve_small_key():
    private, public = gen_small_key()
    sols = find_sols(public)
    w = private['w']
    m = private['m']
    a = public['a']
    x = w*a[0]//m
    print(x)
    print(sols)
    assert x in sols
    segs = to_small_segs(public, sols)
    print(segs)
    print(segs_to_fracs(segs,128,256))
    print(frac(w,m))

def solve_key():
    private, public = gen_key()
    sols = find_sols(public)
    w = private['w']
    m = private['m']
    a = public['a']
    x = w*a[0]//m
    print(x)
    print(sols)
    segs = to_small_segs(public, sols)
    print(segs)
    fracs = segs_to_fracs(segs,2**(d*n-1),2**(d*n))
    print(len(fracs))
    print(frac(w,m))
    for p in fracs:
        if p[0]==frac(w,m):
            print(p)

if __name__ == '__main__':
    check_small_key()
    check_key()
    solve_small_key()
    solve_key()
