import json
def lire_json(nom_fichier):
    try:
        with open(nom_fichier,"r")as fichier:
            donnees=json.load(fichier)
            return donnees
    except json.JSONDecodeError :
        print("erreur:fichier json invalide")   
        return None
def ecrire_json(nom_fichier,donnees):
    with open(nom_fichier,"w")as fichier:
        json.dump(donnees,fichier,indent=4)

donnees=lire_json("sample.json")
print(donnees)
        
           
    
        