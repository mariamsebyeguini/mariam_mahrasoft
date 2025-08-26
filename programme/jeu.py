import random
jeu=["pierre","papier","ciseaux"]
choix=input("entrer votre choix")
ordinateur=(random.choice(jeu))
if choix=="papier" and ordinateur=="pierre":
    print("j'ai gagne")
elif choix=="pierre" and ordinateur=="papier":
    print("ordinateur a gagne")                                                                                                             
elif choix=="ciseaux"and ordinateur=="pierre":
    print("l'ordinateur a gagne")
elif choix=="pierre" and ordinateur=="ciseaux":
    print("j'ai gagne")
elif choix=="ciseaux" and ordinateur=="papier":
    print("j'ai gagne")
elif choix=="papier"and ordinateur=="ciseaux":
    print("l'ordinateur an gagne")           
elif choix==ordinateurls:
    print("nul")
else:
    print("eurreur , entrer un choix") 