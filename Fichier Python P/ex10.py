note = input('Entrez les notes séparées par des virgules : ')
note = [float(i) for i in note.split(',')]
moyenne_note = sum(note) / len(note)
print("Moyenne : ", moyenne_note)

