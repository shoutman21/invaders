import pygame  # necessaire pour charger les images et les sons


class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.sens=None
        self.image=pygame.image.load('vaisseau.png')
        self.position=368
    def deplacer(self):
        if self.sens =="droite":
            self.position+=1
            if self.position>736:
                self.position=736
        elif self.sens=="gauche":
            self.position-=1
            if self.position<0:
                self.position=0
            
class Balle():
    def __init__(self):
        self.tireur= Joueur()
        self.image =pygame.image.load('balle.png')
        self.hauteur = Joueur.position
        self.depart = Joueur(position)
        
    def bouger():
        pass