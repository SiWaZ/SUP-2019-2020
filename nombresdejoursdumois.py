m = int(input("Entrez le mois: "))
a = int(input("Entrez l'année: "))
if m <= 7:
    if m == 2:
        if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
            print("Le nombre de jours est : 29")
        else:
            print("Le nombre de jours est : 28")
    elif m % 2 != 0:
        print("Le nombre de jours est 31")
    else:
        print("Le nombre de jours est 30")

elif 7 < m <= 12:
    if m % 2 == 0:
        print("Le nombre de jours est 31")
    else:
        print("Le nombre de jours est 30")

else :
    print("Veuillez saisir un mois valalble")
