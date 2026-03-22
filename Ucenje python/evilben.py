# povprasaj po imenu

print("Hello welcome to the coffee shop")
name = input("what is your name? ")

# sistem preveri če je osibi ime ben in potem se prepriča da ni zloben.
if name == "ben" or name == "Ben" or name == "BEN":
    evil = input("Are you evil? ")
    if evil == "yes":
        print("You are not welcome here!")
    else:
        print("Welcome to the coffee shop,", name)
else:
    print("Welcome to the coffee shop,", name)
