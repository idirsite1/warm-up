def PoidsIdeal (t,s):
    if s.upper()=="M":
        poids=t - 100 -(t - 150) / 4
    elif s.upper()=="F":
        poids=t - 100 - (t - 150) / 2.5
    return poids
t=float(input("Saisissez votre taille en cm :"))
s=input("Saisissez votre sexe (M/F) :")
print(f"Votre poids idéal est : {PoidsIdeal (t,s)}")