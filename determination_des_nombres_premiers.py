p = int(input("Saisir un nombre: "))

premier = True

if p == 1 :
    print(p, " est un nombre premier")

else:

    for i in range(2,p):

        if p % i == 0 :
            premier = False
            break

    if premier == True:
         print(p, " est un nombre premier")

    elif premier == False:
        print(p, " n'est pas premier")
