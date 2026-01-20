def PoidsIdeal (t,s):
    if s.upper=="M":
        pi=t-100-(t-150)/4
    else:
        pi=t-100-(t-150)/2.5
    return pi
t=float(input("Saisissez votre taille en cm :"))
s=input("Saisissez votre sexe (M/F) :")
print(f"Votre poids idéal est : {PoidsIdeal (t,s)}")