#Fonction pour calculer le factorielle
def fact(n):
     f = 1
     for i in range(1,n+1):
         f = f * i

     return f


#Fonction pour calculer la combinaison
def comb(k,n):
    c = (fact(n))//((fact(k)*fact(n-k)))

    return c


#Programme principal

n = int(input("Le nombre de ligne du triangle: "))
c = 1
for i in range(0,n+1):
  for k in range(0, i+1):
      print(comb(k,i), end = " ")  #Une ligne du triangle, on doit le looper
  print("\n")
