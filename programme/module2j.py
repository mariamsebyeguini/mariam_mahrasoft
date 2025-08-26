import json
def ecrire_json(nom_fichier,donnees):
    with open(nom_fichier,"w") as fichier:
        json.dump(donnees,fichier,indent=4)

donnees={
     "nom":"mariam",
     "age":30,
     "ville":"paris",
     "hobbies":["read coran","cuisine","voyage"],
 } 


ecrire_json("personne.json",donnees)      