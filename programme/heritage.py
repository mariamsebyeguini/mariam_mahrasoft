class Vehicule:
    def __init__(self,marque,modele,vitesse_max):
        self.marque=marque
        self.modele=modele
        self.vitesse_max=vitesse_max
        self.vitesse_actuelle=0
    def accelerer(self,augmentation ):
        nouvelle_vitesse=self. vitesse_actuelle+augmentation
        if nouvelle_vitesse<=self.vitesse_max:
            self.vitesse_actuelle=nouvelle_vitesse
            print(f"vitesse actuelle:{self.vitesse_actuelle}km/h")
        else:
            self.vitesse_actuelle=nouvelle_max
            print(f"vitesse maximale atteinte:{self.vitesse_max}km/h")
    def freiner(self,diminution) :
        nouvelle_vitesse=self.vitesse_actuelle-diminution
        self.vitesse_actuelle=max(0,nouvelle_vitesse) 
        print(f"vitesse apres freinage:{self.vitesse_actuelle}km/h")
         
class Voiture(Vehicule):
    def __init__(self, marque, modele, vitesse_max,nombre_portes):
        super(). __init__(self,marque,modele,vitesse_max)
        self.nombre_portes=nombre_portes
        self.coffre_ouvert=False
    def ouvrir_coffre(self):
        self.coffre_ouvert=True
        print("coffre ouvert")
    def fermer_coffre(self) :
        self.coffre_ferme=False
        print("coffre ferme")
class Moto(Vehicule):
    def __init__(self, marque, modele, vitesse_max,type_moto):
        super().__init__(marque, modele, vitesse_max)
                
           
           
                