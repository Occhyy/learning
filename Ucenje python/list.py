detectJewFromList = [
    "An",
    "Bojan",
    "Cvetko",
    "David",
    "Ema",
    "Feri",
    "Goran",
    "Hana",
    "Ivo",
    "Jana",
    "tian",
]

name = input("Enter a name to check if jewish: ")
for name in detectJewFromList:
    if name == "an" or name == "An" or name == "AN":
        print("JEWWWWWWWWWW", name)
        continue
    else:
        print("normal person", name)
