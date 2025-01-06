voyelle = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
phrase = input('Entrez une phrase : ')
nb_voy = 0
for lettre in phrase:
    if lettre in voyelle:
        nb_voy += 1
print(nb_voy)
