'''3.	Napiši metodo, ki sprejme dve celi števili in ustvari seznam s podseznami. Prvi argument metode je število podseznamov, drugi pa dolžina podseznama. Metoda nato seznam napolni z naključnimi celimi števili v mejah med -25 in 25. Ustvari nov modul in v njem'''
import modul
seznam = []
def ustvariSeznam(st,dol):
    import random

    for i in range(st):
        ps = []
        for k in range(dol):
            ps.append(random.randrange(-25,26))
        seznam.append(ps)
    
ustvariSeznam(3,3)
#stps = modul.steviloPs(seznam)
#print(stps)
#st = modul.negativnost(seznam)
#print(st)
#pv = modul.povprecje(seznam)
#print(pv)
mnmx = modul.minMax(seznam)
print("najmanjse: ",mn)
print("najvecje:", mx)
