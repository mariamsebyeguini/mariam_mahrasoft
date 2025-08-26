import random
print(random.random())
print(random.randint(1,10))
couleurs=["jaune","rouge","bleue","vert"]
print(random.choice(couleurs))
nombres=[1,2,3,4,5]
random.shuffle(nombres)
print(nombres)
print(random.sample(couleurs,1))
jeu=["pierre","papier","ciseaux"]
while True:
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
    elif choix==ordinateur:
        print("nul")
    else:
        print("eurreur , entrer un choix")      
        


