# Kapni sta vrednosti spremenljivk a in b po izvedbi naslednje programske kode? Kolikokrat se zanka ponovi?

a = 1
b = 1
while a < 5:
    a = a + 1
    if b > 7:
        break
    b = b + 3

print(f"Vrednost a-ja je {a}, vrednost b-ja je {b}, število ponovitev zanke je 4.")

# Trace table (for reference):
# a	b
# ------------------------
# 1	1
# 2	1
# 2	4
# 3	4
# 3	7
# 4	7
# 4	10
# 5	10