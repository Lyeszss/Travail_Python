import random as rd
x = rd.randint(1,100)
guess = int(input("Trouver le nombre mystère entre 1 et 100: "))
while guess != x:
    if guess < x:
        print("C'est plus grand")
    elif guess > x:
        print("C'est plus petit")
    guess = int(input())
print('Bravo vous avez trouvé le nombre mystère !')
