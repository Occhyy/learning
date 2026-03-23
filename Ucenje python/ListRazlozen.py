names = ["An", "Mai", "Tian", "Zan Luka"]
# index    0      1      2         3

# printas ime z stevilko indexa
print(names[0])  # An
print(names[1])  # Mai
print(names[2])  # Tian
print(names[3])  # Zan Luka

# stetje inexov nazaj(obratni vrstni red, ni ničle)
print(names[-1])  # Zan Luka
print(names[-2])  # Tian
print(names[-3])  # Mai
print(names[-4])  # An

# slicing izberemo del seznama
print(names[0:2])  # ['An', 'Mai'] - od indexa 0 do indexa 1 (2 ni vključen)
print(names[1:3])  # ['Mai', 'Tian'] - od indexa 1 do indexa 2 (3 ni vključen)
print(names[0:])  # ['An', 'Mai', 'Tian', 'Zan Luka'] - od indexa 0 do konca
print(names[:3])  # ['An', 'Mai', 'Tian'] - od začetka do indexa 2 (3 ni vključen)
print(names[:])  # ['An', 'Mai', 'Tian', 'Zan Luka'] - od začetka do konca

# iskanje elementa v seznamu (vrne True ali False)
print("Tian" in names)  # True
print("Luka" in names)  # False

# Iskanje indexa elementa v seznamu(vrne index stevilko)
print(names.index("Tian"))  # 2
print(names.index("Mai"))  # 1
