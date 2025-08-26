class personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
    def se_presenter(self):
        print(f"bonjour,je suis {self.nom} et j'ai {self.age} ans")
mariam=personne("mariam",25)
bob=personne("bob",30) 
mariam.se_presenter()
bob.se_presenter()



class Voiture:
    def __init__(self,marque,modele,couleur,kilometrage=0):
        self.marque=marque
        self.modele=modele
        self.couleur=couleur
        self.moteur_allume=False
        self.kilometrage = kilometrage
    def demarrer(self):
        if not self.moteur_allume:
            print(f"la {self.marque} {self.modele} demarre ...vrooom")
        else:
            print("la voiture est deja arretee!")
         
        
    def arreter (self ):
       if self.moteur_allume:
          self.moteur_allume=False
          print("fla {self.marque} {self.modele} s'arrete")
       else:
           print(f"la voiture est deja arrete")
    def rouler(self,distance):
        if self.moteur_allume:
            self.kilometrage +=distance
            print(f"vous avez roule {distance}km.")
        else:
            print("demarrez d'abord la voiture")  
    def info(self):
        etat="demarre"  if self.moteur_allume else "arretee" 
        print(f"voiture:{self.marque} {self.modele}") 
        print(f'couleur:{self.couleur}') 
        print(f"kilometrage:{self.kilometrage} km.") 
        print(f"etat:{etat}") 
        
        
        
        
ma_voiture=Voiture("toyota","corolla","rouge") 
voiture_ami=Voiture(f"bnw","x5","noire",15000)
print("---ma voiture---")
ma_voiture.info()
ma_voiture.demarrer()
ma_voiture.info()
voiture_ami.info()
voiture_ami.rouler(1200)
voiture_ami.info()
             
           
           
             
                   