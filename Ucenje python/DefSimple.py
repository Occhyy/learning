# funkcija:   - mora imti jasno ime, ki opisuje kaj funkcija počne
#            - lahko ima argumente, ki so podatki, ki jih funkcija potrebuje za delovanje
#            - lahko vrne rezultat, ki je izračun ali informacija
#            - mora imeti samo eno nalogo, ki jo opravlja

enota = "cm squared"


def izracun_povrsine(
    visina, sirina
):  # definira izracun povrsine, ima dva argumenta, višina in širina
    povrsina = visina * sirina  # izračun povrsine, višina pomnožena s širino
    return povrsina  # vrne izračunano povrsino


povrsina = izracun_povrsine(5, 10)  # klic funkcije z argumenti

print(povrsina, enota)  # izpis izračunate površine
