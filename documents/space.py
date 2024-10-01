import pygame  # necessaire pour charger les images et les sons
import random
import math

class Joueur() : # classe pour créer le vaisseau du joueur
    skcore=0
    def __init__(self) :
        self.sens=None
        self.score=0
        self.image=pygame.image.load('vaisseau.png')
        self.position=268
    def deplacer(self):
        if self.sens =="droite":
            self.position+=1
            if self.position>736:
                self.position=736
        elif self.sens=="gauche":
            self.position-=1
            if self.position<0:
                self.position=0
    def tirer(self):
        self.sens=None
    def marquer(self):
        self.score = self.score + 1
            
class Balle():
    def __init__(self,tireur):
        self.tireur= tireur
        self.image =pygame.image.load('balle.png')
        self.hauteur = 492
        self.depart = tireur.position + 16
        
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - 5
        
        if self.hauteur < 0:
            self.etat = "chargee"
    def toucher(self,Ennemi):
        if (math.fabs(self.hauteur - Ennemi.hauteur) < 40) and (math.fabs(self.depart - Ennemi.depart) < 40):
            self.etat = "chargee"
            return True
class Ennemi():
    def __init__(self):
        self.depart=random.randint(0,750)
        self.hauteur=0
        self.type=random.randint(1,2)
        self.image=pygame.image.load('invader'+str(self.type)+'.png')
        self.vitesse=random.randint(1,3)/10
        
    def avancer(self):
        
        self.hauteur+=self.vitesse
    def disparaitre(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 1
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 2

class Joueur2() : # classe pour créer le vaisseau du joueur
    skcore=0
    def __init__(self) :
        self.sens=None
        self.score=0
        self.image=pygame.image.load('vaisseau2.png')
        self.position=568
    def deplacer(self):
        if self.sens =="droite":
            self.position+=1
            if self.position>736:
                self.position=736
        elif self.sens=="gauche":
            self.position-=1
            if self.position<0:
                self.position=0
    def tirer(self):
        self.sens=None
    def marquer(self):
        self.score = self.score + 1
            