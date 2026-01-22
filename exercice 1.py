nb_posi=1
liste=[]
while nb_posi>0 :
 nb_posi=int(input("Saisissez un nombre entier positif pour l'ajouter à une liste :"))
 liste.append(nb_posi)
print(liste)
print(f"La plus petite valeur est {min(liste)}")
print(f"La plus grande valeur est {max(liste)}")
