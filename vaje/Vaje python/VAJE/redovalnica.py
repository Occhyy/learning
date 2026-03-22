imena={"dgdsg","dgsdsgds","dsgdgds","dsgsdf","dtw","ddghs","dgsg"}
predmeti={"NPB","VIP","SLO","ANJ","MAT","PRO"}
priimki={"asfa","afasfga","afga","afsfga","agag","agaga","agaht","aggagat"}

import random

def UstvariDijake(imena,priimki):
    dijaki=[]
    for i in range(20):
        ime=list(imena)[random.randrange(0,len(imena))]
        priimek=list(priimki)[random.randrange(0,len(priimki))]
        dijaki.append(ime+" "+priimek)
    return dijaki

a= UstvariDijake(imena,priimki)
for item in a:
    print(item)

def VnosOcen():
    ocene=[]
    for i in range(20):
        ps=[]
        for j in range(6):
            ps.append(random.randrange(17,60)//10)
        ocene.append(ps)
    return ocene


def uspeh(ocene):
  povp=0
  sez=[]
  for ps in ocene:
    povp=0
    if 1 in ps:
      sez.append(1.0)
    else:
      for oc in ps:
        povp += oc
      sez.append(round(povp/len(ps),1))
  return sez

def izpis(dijaki,predmeti,ocene,uspeh):
  print("%20s" % " ",end="")
  for p in predmeti:
    print("%4s" % p,end="")
  print("  Uspeh")
  k = 0
  for item in dijaki:
    i=0
    print("%-18s " % item,end="")
    for oc in ocene[k]:
      print("%4d" % int(oc), end="")
      i+=1
    print("%7s" % uspeh[k])
    k = k+1
#GLAVNI PROGRAM 
b=VnosOcen()
d=UstvariDijake(imena,priimki)
u=uspeh(b)
izpis(d,predmeti,b,u)

