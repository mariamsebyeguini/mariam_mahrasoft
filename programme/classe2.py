class CompteBancaire:
    def __init__(self,proprietaire,solde_initial=0):
        self.proprietaire=proprietaire
        self._numero_compte = self._generer_numero()
        self.__solde=solde_initial
        self.__historique=[]
    def _generer_numero(self):
        import random 
        return f"FR{random.randint(1000000,9999999999)}" 
    def deposer(self,montant):
        if montant>0:
            self.__solde +=montant
            self.__historique.append(f"depot:+{montant} fCfA")
            return True
        return False
    def retirer(self,montant):
        if 0< montant <=self.__solde:
            self.__solde-=montant
            self.__historique.append(f"retrait: -{montant}")
            return True 
        return False
    def get_solde(self):
        return self.__solde
    def get_historique(self) :
        return self.__historique.copy()
    def __str__(self) :
        return f"compte de {self.proprietaire} ({self._numero_compte}):{self.__solde}FCFA"
compte=CompteBancaire("mariam seby",100000000) 
print(compte)
compte.deposer(100000)
compte.retirer(20000)


print(f"solde actuel:{compte.get_solde()}FCFA")
print(compte._numero_compte)