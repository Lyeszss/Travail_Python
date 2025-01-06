nb1 = int(input("Entrez un premier nombre"))
nb2 = int(input("Entrez un deuxieme nombre"))
nb3 = int(input("Entrez un troisieme nombre"))

if nb1 > nb2 and nb1 > nb3:
    print(f"Le plus grand nombre est {nb1}")
elif nb2 > nb1 and nb2 > nb3:
    print(f"Le plus grand nombre est {nb2}")
else:
    print(f"Le plus grand nombre est {nb3}")
