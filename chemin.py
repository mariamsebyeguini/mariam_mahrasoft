import os 
chemin_absolu=os.path.abspath("etudiant.txt")
print(chemin_absolu)
repertoire,nom_fichier=os.path.split(chemin_absolu)
print(f"repertoire:{repertoire}")
print(f"nom du fichier:{nom_fichier}")
nom,extension=os.path.splitext(nom_fichier)
print(f"nom:{nom}")
print(f"extension:{extension}")
