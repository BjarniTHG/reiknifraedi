import re
import math

class Skil(object):
    """Timadaemi 2 f. REI"""
    #Bjarni Þór Guðmundsson
    #btg7@hi.is
    def asj(self, a, b, c):
        adgreinir = b**2-4*a*c
        if(adgreinir<0):
            return None
        elif(adgreinir == 0):
            return -b/2*a
        else:
            rot1 = (-b+math.sqrt(adgreinir))/(2*a)
            rot2 = (-b-math.sqrt(adgreinir))/(2*a)
            return rot1, rot2

    def trap(self,f, a, b, n): #f er fallið sem á að heilda, (a, b) er bilið og n er jákvæð heiltala sem heildið er deilt upp í(fjöldi stika)
        delta_x = (b-a) / n #DeltaX = (b-a)/n til að reikna breidd hverrar stiku
        heildarsvaedi = 0.5 * (f(a) + f(b)) #Formulan fyrir svaedi trapisu er A = 1/2 x (b1 + b2) x h, þar sem b1 og b2 eru hliðarlengdir trapisurnar og h er hæð trapisunar
                                            #og hliðarlengdir í okkar tilviki eru f(a) og f(b)

        for i in range(1, n): #Frá fyrstu stiku upp í n-fjölda stika sem við ætlum að deila upp í
            x_i = a + i * delta_x #reikna staðsetningu hverrar stiku á x-ás
            heildarsvaedi += f(x_i) #summa hverja stiku til að fá heildar svæði heildisins

        return heildarsvaedi * delta_x

    def krot(self, a):
        x = 1 #giskum fyrst á x
        skekktarmork = 1e-10
        while(True): #á meðan giskið er ekki jafnt og talan sem á að finna
            y = (x + a/x)/2 #Newton aðferðin
            if(abs(x - y) < skekktarmork): #algildið á x-y ekki jafnt og a
                return y
            x = y #y er nýja giskið okkar

