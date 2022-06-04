def gcd(a, b):
    while b!=0:
        t = a
        a = b
        b = t%b
    return a

class frac:
    def __init__(self, a, b):
        g = gcd(a, b)
        a = a//g
        b = b//g
        if b<0:
            a = -a
            b = -b
        self.a = a
        self.b = b
    def __lt__(self, f):
        return self.a*f.b<f.a*self.b
    def __le__(self, f):
        return self.a*f.b<=f.a*self.b
    def __gt__(self, f):
        return self.a*f.b>f.a*self.b
    def __ge__(self, f):
        return self.a*f.b>=f.a*self.b
    def __eq__(self, f):
        return self.a*f.b==f.a*self.b
    def __ne__(self, f):
        return self.a*f.b!=f.a*self.b
    def __repr__(self):
        return str(self.a)+'/'+str(self.b)