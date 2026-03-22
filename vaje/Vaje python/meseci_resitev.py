


"""2.	Ustvari slovar mesecev in števila dni v za vsak mesec v letu. Za ime meseca uporabi prve tri črke (jan, feb, mar…) Nato napiši metodo, ki sprejme dva datuma v tekstovni obliki (primer: ''12.mar'') ter izračuna in vrne število dni met tema datumoma. Upoštevaj:"""

meseci = {
"jan" : 31,
"feb" : 28,
"mar" : 31,
"apr" : 30,
"maj" : 31,
"jun" : 30,
"jul" : 31,
"avg" : 31,
"sep": 30,
"okt" : 31,
"nov" : 30,
"dec" : 31 
}

# •	Metoda obvezno preveri argumente, če oblika vnosa ustreza (če je ključ v imeniku).


def dnevi(dat1, dat2):
    
    razlika_dni = 0                 
    dan1 = int(dat1.split(".")[0])  #dan prvega datuma
    mes1 = dat1.split(".")[1]       #mesec prvega datuma
    dan2 = int(dat2.split(".")[0])
    mes2 = dat2.split(".")[1]
    m = meseci.keys()               #imena mesecev (tuple ključev)
    d = meseci.values()             #število dni v posameznem mesecu (tuple)
  
    #zamenjava datumov, če je prvi večji od drugega    
    if mes1 > mes2:
        mes1,mes2=mes2,mes1
      
    if mes1 == mes2 and dan1 > dan2:
        dan2,dan1=dan1,dan2
    
    if mes1 in m and mes2 in m:
        if dan1 > 0 and dan1 < meseci[mes1]:
            if dan2 > 0 and dan2 < meseci[mes2]:
                ix1 = list(m).index(mes1)       #index meseca prvega datuma
                ix2 = list(m).index(mes2)       #index meseca drugega datuma
                vr = list(d)                    #seznam števila dni v posamaznem mesecu
                for i in range(ix1+1, ix2):
                    razlika_dni+=vr[i]
                razlika_dni +=dan2+meseci[mes1] - dan1    
                print(razlika_dni)
            else: print("neveljaven vnos")
        else: print("neveljaven vnos")
    else: print("neveljaven vnos")
    
dnevi("12.sep","24.apr")