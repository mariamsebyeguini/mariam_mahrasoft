import csv
def lire_csv(clients_csv):
    with open(clients_csv,"r",newline="") as fichier:
        lecteur=csv.reader(fichier)
        for ligne in lecteur:
            print(ligne)
lire_csv("clients.csv")
def ecrire_csv(clients_csv,donnees):
    with open (clients_csv,"w",newline="") as fichier:
        f=csv.writer(fichier)
        f.writerow(["nom","age","ville"])
        for ligne in donnees:
            f.writerow(ligne)
            
donnees=[
    ["alice",25,"tchad"],
    ["bob",16,"paris"],
    ["nour",17,"togo"],
    ["nousradine", 25, "Tchad"],
    ["Ache", 19, "Tchad"]
]
ecrire_csv("personnes.csv",donnees)                       
    