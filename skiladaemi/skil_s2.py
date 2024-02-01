import re

class Skil(object):
    """Skilaverkefni 2 f. REI

    """
    def simpson(self, f, a, b, n):
        delta_x = (b - a) / n
        total = 0
        
        for i  in range(0, n+1):
            x_i = a + i * delta_x
            if i == 0 or i == n:
                total += f(x_i)
            elif i % 2 == 0:
                total += f(x_i) * 2
            elif i % 2 == 1:
                total += f(x_i) * 4
                
        final = total * (delta_x / 3)
        return final

    def vextir(self, u, p, k, m):
        a = p / 100
        v = u*(1+a)**k * (1+(a*m)/12) - u
        
        return int(v)
        
    def vextir2(self, p):
        u = 1
        k = 0
        m = 0
        
        while True:
            vaxtarupphaed = self.vextir(u, p, k, m)
            if vaxtarupphaed >= u:
                break
            m += 1
            if m >= 12:
                m = 0
                k += 1
        
        ar = k
        man = m
        return ar, man


    def bolurodun(self, x):
        vixlad = True
        while vixlad:
            vixlad = False
            for i in range(1, len(x)):
                if x[i-1] > x[i]:
                    x[i-1], x[i] = x[i], x[i-1] #(a, b) = (b, a)
                    vixlad = True
        return x
