class Etudiants:
    def __init__(self,nom,prenom, numero_etudiant):
        self.nom=nom
        self.prenom=prenom
        self.numero_etudiant=numero_etudiant
        self.notes={}
        self.moyenne_generale=0
        
        
    def ajouter_note(self,matiere,note) : 
        if 0 <=note<=20:
            if matiere not in self.notes:
                self.notes[matiere]=[]
            self.notes[matiere].append(note) 
            print(f"note {note}/20 ajoutee en {matiere} pour {self.prenom} {self.nom}")
            self.calculer_moyenne_generale()
        else:
            print("la note doit etre entre 0 et 20")
            
    def calculer_moyenne_matiere(self,matiere):
        if matiere in self.notes and self.notes[matiere]:
            return sum(self.notes[matiere])/len(self.notes[matiere])
        return 0 
    def calculer_moyenne_generale(self):
        if not self.notes:
            self.moyenne_generale=0
            return 
        total_moyennes=0
        nb_matieres=0
        for matiere in self.notes:
            if self.notes[matiere]:
                total_moyennes+= self.calculer_moyenne_matiere(matiere)
                nb_matieres +=1
            if nb_matieres> 0:
                self.moyenne_generale=total_moyennes/nb_matieres
            else:
                self.moyenne_generale=0
    def afficher_bulletin(self):
        print(f" bulletin de {self.prenom.upper()} {self.nom.upper()}")
        print(f"numero etudiant :{self.numero_etudiant}")
        print("-" *50)
        
        for matiere, notes in self.notes.items:
            moyenne=self.calculer_moyenne_matiere(matiere)
            print(f"{matiere}: {notes} moyenne:{moyenne:.2f}/20")
            
        print("_" * 50) 
        print(f"MOYENNE GENERALE:[self.moyenne_generale:2f]/20") 
        
        
        if self.moyenne_generale >=16:
            mention= "tres bien"
        elif self.moyenne_generale>=14:
            mention="bien"        
        elif self.moyenne_generale >=12:
            mention="assez bien"
        elif self.moyenne_generale>=10:
            mention="passable"
        else:
            mention ="insuffissant" 
            print(f"mention:{mention}")   
etudiant1=Etudiants("mariam","seby",2345)
etudiant1.ajouter_note("math",14)
etudiant1.ajouter_note("francais",15)
etudiant1.ajouter_note("histoire",18)
etudiant1.afficher_bulletin




