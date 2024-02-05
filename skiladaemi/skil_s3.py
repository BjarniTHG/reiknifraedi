import re

class Skil(object):
    """Skilaverkefni 3 f. REI, Bjarni Þór Guðmundsson(btg7@hi.is)"""

    def arr_to_dict(self,arr):
        d = {} #búa til tómt dictionary
        for i in range(len(arr)):
            for j in range (len(arr[i])):
                d[(i, j)] = arr[i][j] #hvert key-value par í dictionaryinu hefur lykilinn [i][j] og gildið x sem er í tiltekna stakinu innan tvívíða fylkisins
        
        return d

    def dict_to_arr(self,d):
        fylkja_staerd = 0
        
        for i in d.keys():
            fylkja_staerd = max(fylkja_staerd, i[0], i[1]) #max function sniðugt til að halda utan um stærsta gildið af inntökunum fundið so far 
        staerd = fylkja_staerd + 1 #+1 því núll indexað
        ls = [[0]*staerd for _ in range(staerd)]
        #'pythonic' leið til að framkvæma:
        #ls = []
        #for _ in range(staerd):
            #ls.append([0] * staerd)
            #m.ö.o búa til lista af stærð 'staerd' af listum af stærð 'staerd'
        #Núna búinn að búa til tvívítt núllfylki af réttri stærð, getum núna fyllt inn með réttum gildum:
        for(i, j), value  in d.items(): #.items skilar ítrara með öllum pörum í d og [(i, j), value] brýtur hvert par niður í lykil+gildi, við notum þá gildið til að setja í ls[i][j]
            ls[i][j] = value #value er bara breytunafn, ekki function eða annað, mætti heita hvað sem er
        return ls

    def snuavid(self,d1):
        d2 = {} #Búum til nýtt tómt dictionary
        for key, value in d1.items():
            if value in d2: #Ef gildið er þegar til í d2
                if not isinstance(d2[value], list): #Ef það er ekki nú þegar búið að breyta staki í lista til að halda utan um fleiri en einn lykil sem á við sama gildi
                    d2[value] = [d2[value]] #þá breyta tagi af staki í lista til að halda utan um fleiri lykla
                d2[value].append(key) #Bætum lykli aftan við fyrri lykla sem möppuðu á sama gildi
            else:
                d2[value] = key #Ef hefur ekki komið fyrir áður þá bara búa til setja valueið á núverandi staki í d2 sem tiltekin lykil úr d1
        return d2


if __name__ == '__main__':
    skil = Skil()
