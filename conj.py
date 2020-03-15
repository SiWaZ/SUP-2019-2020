def conjugaison(s):
    ter = ["e", "es", "e", "ons", "ez", "ent"]
    pr = ["Je ", "Tu ", "Il/elle ", "Nous ", "Vous ", "Ils/Elles "]
    voy = ["a", "o", "u", "i", "e", "y"]
    n = len(ter)
    r = s[-len(s) : -2]
    if r[-1] == "c":
        for i in range(n):
            if i == 3:
                print(pr[i] + r[:-1] + "ç" + ter[i])
            else:
                print(pr[i] + r + ter[i])

    elif r[-1] == "g":
        for i in range(n):
            if i == 3:
                print(pr[i] + r + "e" + ter[i])
            else:
                print(pr[i] + r + ter[i])



    elif (r[-2]== "a" and r[-1]== "y") or (r[-2]=="u" and r[-1]=="y") or (r[-2]=="o" and r[-1]=="y"):
        for i in range(n):
            if i != 3 and i != 4:
                print(pr[i] + r[:-1] + "i" + ter[i])
            else:
                print(pr[i] + r + ter[i])


    elif r[0] in voy:
        pr[0] = "J' "
        for i in range(n):
            print(pr[i] + r + ter[i])


    else:
        for i in range(n):
            print(pr[i] + r + ter[i])



conjugaison("Chanter")
conjugaison("Changer")
conjugaison("Lancer")
conjugaison("Essayer")
conjugaison("Commencer")
