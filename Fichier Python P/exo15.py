import random as rd
nb_mystere = rd.randint(1,1000)
guess = int(input("Trouver le nombre mystère entre 1 et 1000: "))
for i in range (10):
        if guess != nb_mystere:
            if guess < nb_mystere:
                print("C'est plus grand")
            elif guess > nb_mystere:
                print("C'est plus petit")
            guess = int(input())
     
if guess == nb_mystere:             
    print('Bravo vous avez trouvé le nombre mystère !')
else:
    print("C'est perdu /: Vous avez utilisé vos 10 essai !")   