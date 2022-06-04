def encrypt(message, public):
    a = public['a']
    n = len(a)
    cipher = 0
    for i in range(n):
        if (message>>i)&1:
            cipher += a[i]
    return cipher

def decrypt(cipher, private):
    m = private['m']
    w = private['w']
    a = private['a']
    c = cipher*w%m
    n = len(a)
    message = 0
    for i in range(n-1,-1,-1):
        if c >= a[i]:
            c -= a[i]
            message ^= 2**i
    assert c==0
    return message
