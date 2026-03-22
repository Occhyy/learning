# for loop = a statement that will execute its block of code a limited amount of times
# you can iterate over a sequence (list, tuple, string) or other iterable objects


# count to 10
for x in range(1, 11):
    print(x)

# count from 10 backwards to 1
for x in reversed(range(1, 11)):
    print(x)

# count by two's
for x in range(0, 11, 2):
    print(x)

# count to 20 and skip 5
for x in range(0, 21):
    if x == 5:
        continue
    else:
        print(x)

# count to 20 break at 15
for x in range(0, 21):
    if x == 15:
        break
    else:
        print(x)
