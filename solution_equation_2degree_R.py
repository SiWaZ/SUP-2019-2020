from math import sqrt

from math import sqrt

a = float(input("Saisir le coefficient de x^2:"))
b = float(input("Saisir le coefficient de x:"))
c = float(input("Saisir le coefficient de constante:"))

delta = b**2 - 4*a*c

if a == 0 :
    if b == 0:
        if c == 0:
            print("Tous les nombres sont solutions de l'equation")
        else :
            print("L'equation n'admet pas de solution")
    else:
        print("La solution de l'equation est :", -c/b)


elif delta == 0:
    s = -b / (2*a)
    print("La solution est : {", s , "}")

elif delta > 0 :
    s1 = ( -b - sqrt(delta)) / (2*a)
    s2 = ( -b + sqrt(delta)) / (2*a)
    print("Les solutions de l'équation sont ", "{", s1 ,"," ,s2 , "}")

else :
    print("L'equation n'admet pas de solutions dans R")
