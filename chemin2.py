from pathlib import Path
chemin=Path("dossier/sous_dossier/fichier.txt")
print(f"nom du fichier:{chemin.name}")
print(f"extension du fichier:{chemin.suffix}")
print(f"repertoire parent:{chemin.parent}")
print(f"chemin:{chemin.absolute()}")
print(f"Existe:{chemin.exists()}")
print(f"est un fichier:{chemin.is_file()}")
print(f"est un dossier:{chemin.is_dir}")
nouveau_dossier=Path("maria")
nouveau_dossier.mkdir(exist_ok=True)
nouveau_dossier=Path("dossier\mariam\exercice")
nouveau_dossier.mkdir(parents=True,exist_ok=True)
      