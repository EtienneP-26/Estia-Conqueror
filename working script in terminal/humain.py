from arme import Arme
from entités import Entités

class Humain(Entités):
    def __init__(self) -> None:
        Entités.__init__(self)
        self.nom =  "humain"
        self.sante = 30
        self.force = 5

class Chevalier(Entités):
    def __init__(self) -> None:
        Entités.__init__(self)
        self.type = "mini-boss"
        self.nom =  "chevalier"
        self.sante = 100
        
class Tyranoporc(Entités):
    def __init__(self ) -> None:
        Entités.__init__(self)
        self.type = "boss"
        self.nom = "Tyranoporc"
        self.sante = 200
        self.force = 15
        self.force_critique = 30

    def attaque_critique(self, ennemi):
        if ennemi.armure.nom == "manteau":
            ennemi.sante -= 1
        else : ennemi.sante -= self.force_critique - ennemi.armure.defense

        