from Arme import Arme
from Armure import Armure
from random import randint as rd


arme = Arme()
armure = Armure()

class Entites(object):
    def __init__(self, arme = arme, armure = armure, level : int = 0) -> None:
        self.nom = ""

        # stats
        self.sante = 100
        self.sante_max = 100
        self.force = 10
        self.technique = 10
        self.defense = 10
        self.distance_attaque = 75
        self.race = None

        #
        self.arme = arme
        self.armure = armure
        self.inventaire = []
        self.position = [0, 0]
        self.taille = 75
        self.vitesse = 10

        # argent et experience
        self.xp = 0
        self.xp_neccessaire = 5
        self.level = level
        self.coins = 0
        self.diamants = 0
        self.xp_drop = 0

        # skin de base 
        self.img_psL = "player\squelette\debout_g.png"
        self.img_psR = "player\squelette\debout_d.png"
        self.img_psL_running_1 = "player\squelette\court_g_1.png"
        self.img_psL_running_2 = "player\squelette\court_g_2.png"
        self.img_psR_running_1 = "player\squelette\court_d_1.png"
        self.img_psR_running_2 = "player\squelette\court_d_2.png"
        self.player_img_affiché = "player\squelette\debout_g.png"


    def en_vie(self):
        if self.sante <= 0:
            return False
        return True
    
    def level_up(self):
        if self.xp_neccessaire == self.xp:
            self.xp = 0
            self.level += 1
            self.xp_neccessaire = int((self.xp_neccessaire * 1.2 + 12) // 1)
            self.sante_max += 5
            self.sante += 5
            n = input("1 : augmenter la force\n2 : augmenter defense")
            if n == 1 or n == "force" or n == "augmenter la force":
                return True
        return False
    
    def looting(self,ennemi):
        for chance in ennemi.loot:
            temp = rd(1,100)
            if temp <= chance:
                self.inventaire.append(ennemi.loot[chance])

    
    def attaque(self, ennemi):
        if abs(self.position[0] - ennemi.position[0]) <= self.distance_attaque and abs(self.position[1] - ennemi.position[1]) <= self.distance_attaque :
            ennemi.sante -= (self.force + self.arme.degats) - ennemi.armure.defense
            if ennemi.sante <= 0:
                self.xp += ennemi.xp_drop*2 if self.race == "goblin" else ennemi.xp_drop
                self.level_up()
                if self.race == "vampire":
                    self.sante += (self.sante_max/100)*10
                    if self.sante > self.sante_max:
                        self.sante = self.sante_max

    def soigner(self, niveau):
        self.sante += niveau
        if self.sante > self.sante_max:
            self.sante = self.sante_max