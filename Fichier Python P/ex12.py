import random as rd
clavier = [chr(i) for i in range(32, 127)]
mdp = ""
longeur_mdp = int(input("Entrez le nombre de caratere souhaité pour le mot de passe"))
for i in range (longeur_mdp):
    mdp += rd.choice(tuple(clavier))
print(mdp)



