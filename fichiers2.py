with open("etudiant.txt") as fichier:
    lignes=fichier.readlines()
    for ligne in lignes:
        print(ligne)