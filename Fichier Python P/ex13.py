liste = input('Entrez les nombres séparés par des virgules : ')
liste = [float(i) for i in liste.split(',')]
print(sorted(liste))