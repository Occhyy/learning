"""
1. Poleti so Butalci za otroke na mestno igrišče postavili šotor v obliki stožca z višino 1,5 m. 
Kasneje so na igrišče postavili še 9 šotorov. Vsak naslednji šotor je bil za 20 cm višji od predhodnega. 
Kako visok (v matrih) je bil zadnji, deseti šotor?
1.5 1.7 1.9 2.1 2.3 2.5 2.7 2.9 3.1 3.3"""
visina=1.5
st_sotorov=9
for i in range(st_sotorov):
    visina=visina+0.2
visina=round(visina,2)
print("višina zadnjega:",visina)

"""
2. Na kmetiji so izkopali vodnjak v obliki valja z globino 12 m. 
Za kopanje prvega metra so plačali 10 €, za kopanje vsakega naslednjega metra pa 5 € več. 
Koliko stane kopanje zadnjega metra in koliko celega vodnjaka?
10 15 20 25 30 35 40 45 50 55 60 65 """

globina = 12
meter = 10
skupaj = 0
for i in range(globina):
    skupaj=skupaj+meter
    meter=meter+5
print("skupaj:",skupaj)
print("zadnji:",meter-5)

"""
3. V jedilnici turistične kmetije stoji 6 miz. Na prvi je 6 kozarcev. Na vsako naslednjo mizo postavijo dvakrat toliko kozarcev 
kot jih je na prejšnji mizi. Koliko kozarcev je na zadnji mizi? Koliko kozarcev je na vseh mizah skupaj? 
6 12 24 48 96 192"""

st_miz = 6
kozarci = 6
skupaj = 0
for i in range(st_miz):   
    skupaj=skupaj+kozarci
    kozarci=kozarci*2
print("skupaj:",skupaj)
print("zadnji;",kozarci//2)    

"""
4. V mestnem drevoredu je zasajenih 80 dreves. Gozdar Matic označi vsako tretje drevo, gozdar Jure pa vsako peto drevo. 
Podrli bomo tista drevesa, ki so označena z znakoma obeh gozdarjev. Koliko jih bomo podrli? Katero drevo bo prvo podrto?
15 30 45 60 75"""
koliko,prvo=0,0
st_dreves=80
for i in range(1,st_dreves+1):
    if i%3==0 and i%5==0:
        koliko=koliko+1
        if koliko==1:
            prvo=i
print("koliko:",koliko)
print("prvo:",prvo)

"""
5. Butalci so na njivo trikotne oblike zasadili krompir: v prvo vrsto 2 krompirja, v vsako naslednjo vrsto 4 krompirje več. 
Koliko krompirja so zasadili v 25. vrsto? Koliko krompirja so zasadili v vseh 25 vrst skupaj?
(rešitev: zadnja vrsta - 98, skupaj - 1250)"""
st_vrst=25
kromp=2
skupaj=0
for i in range(st_vrst):
    skupaj=skupaj+kromp
    kromp=kromp+4
print("skupaj:",skupaj)
print("zadnji:",kromp-4)
   
"""
6. Primož je prvi teden vsak dan tekel. Prvi dan je pretekel 3 km, vsak naslednji dan pa 1,5 km več. 
Koliko km je pretekel sedmi dan? Koliko km je pretekel skupaj v sedmih dneh?
3  4.5  6  7.5  9  11.5  13     skupaj: 54.5 km"""

"""
7. Primož je prvi dan prekolesaril 5 km. Odločil se je, da bo v naslednjih dveh tednih vsak naslednji dan prekolesaril 2,5 km več kot prejšnji dan. 
Koliko km je prekolesaril peti dan? Kateri dan bo prekolesaril 35 km? Koliko km je prekolesaril v teh dveh tednih?
5  7.5  10  12.5  15  17.5  20  22.5  25  27.5  30  32.5  35  37.5  skupaj: 297.5 km"""
na_dan=5
st_dni=14
skupaj=0
for i in range(1,st_dni+1):
    skupaj=skupaj+na_dan   
    if i==5:
        peti=na_dan
    if na_dan==35:
        dan=i
    na_dan=na_dan+2.5
print("peti dan:",peti)
print("35 km:",dan)
print("skupaj:",skupaj)
        
        
