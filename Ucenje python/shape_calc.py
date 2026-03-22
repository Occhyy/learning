# kalkulator kvadrat,pravokotnik trikotnik krog


def krog(polmer):
    obseg = 2 * 3.14 * polmer
    povrsina = 3.14 * polmer**2
    return obseg, povrsina


menu = input("izberi obliko (kvadrat, pravokotnik, trikotnik, krog) ")

if not menu in ["kvadrat", "pravokotnik", "trikotnik", "krog"]:
    print("neveljaven vnos")
    exit()

elif menu == "kvadrat":

    stranica = int(input("vnesi stranico "))

    obseg = 4 * stranica
    povrsina = stranica**2
    diagonala = stranica * (2**0.5)

    print("obseg = ", obseg)
    print("povrsina = ", povrsina)
    print("diagonala = ", diagonala)

elif menu == "pravokotnik":

    stranicaA = int(input("vnesi stranico a "))
    stranicaB = int(input("vnesi stranico b "))

    obseg = 2 * (stranicaA + stranicaB)
    povrsina = stranicaA * stranicaB
    diagonala = (stranicaA**2 + stranicaB**2) ** 0.5

    print("obseg = ", obseg)
    print("povrsina = ", povrsina)
    print("diagonala = ", diagonala)

elif menu == "trikotnik":

    stranicaA = int(input("vnesi stranico a "))
    stranicaB = int(input("vnesi stranico b "))
    stranicaC = int(input("vnesi stranico c "))

    obseg = stranicaA + stranicaB + stranicaC
    s = obseg / 2
    povrsina = (s * (s - stranicaA) * (s - stranicaB) * (s - stranicaC)) ** 0.5

    print("obseg = ", obseg)
    print("povrsina = ", povrsina)

elif menu == "krog":

    polmer = int(input("vnesi polmer "))

    obseg, povrsina = krog(polmer)

print("konec programa")
