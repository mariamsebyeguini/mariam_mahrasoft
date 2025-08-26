import os
import json
print("+"*50)
print(os.getcwd())
print("+"*50)
fichiers=os.listdir(".")
print(fichiers[:5])
if os.path.exists("important2.py"):
    print("le fichier existe")
else:
    print("le fichier n'existe pas")
chemin=os.path.join("dossier","sous_dossier","fichier.txt") 
print(chemin)
if os.path.exists("osysteme.py"):
    taille=os.path.getsize("osysteme.py")
print(f"taille:{taille}octets")


  

# with open("c:/Users/Mahrasoft/Desktop/mariam/programme/exo4.py", "r", encoding="utf-8") as file:
#     f = file.read()
#     print(f)