from arme import Arme
from armure import Armure

class Entités(object):
    def __init__(self, arme = Arme(), armure = Armure()) -> None:
        self.nom = ""
        self.sante = 100
        self.sante_max = 100
        self.armure = armure
        self.force = 10
        self.arme = arme
        self.position = (0,0)
        self.xp = 0
        self.lvl = 0
        self.race = None
        self.item = 0

    def en_vie(self):
        if self.sante <= 0:
            return False
        return True
    
    def attaque(self, ennemi):
        ennemi.sante -= self.force + self.arme.degats - ennemi.armure.defense
        if ennemi.sante <= 0:
            if self.race == "vampire":
                self.sante += 5
                if self.sante > 80:
                    self.sante = 80
            self.xp += 5 if self.race == "goblin" else 2
            if self.xp >= 20:
                self.xp -= 20
                self.lvl += 1
                self.force += 2 

    def __str__(self) -> str:
        l0 = f" <:> {self.nom} <:> \n"
        l1 = f" RACE : {self.race}\n"
        l2 = f" SANTE : {self.sante}/{self.sante_max}\n"
        l3 = f" FORCE : {self.force}\n"
        l4 = f" ARME : {self.arme}\n"
        l5 = f" ARMURE : {self.armure}\n"
        l6 = f" XP : {self.xp}\n"
        l7 = f" LVL : {self.lvl}"

        return l0 + l1 + l2 + l3 + l4 + l5 + l6 + l7

    
            

    