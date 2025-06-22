from arme import Arme
from armure import Armure
from entités import Entités

class Goblin(Entités):
    def __init__(self, nom:str) -> None:
        Entités.__init__(self)
        self.race = "goblin"
        self.nom = nom
        self.force = 5


class Vampire(Entités):
    def __init__(self, nom:str) -> None:
        Entités.__init__(self)
        self.race = "vampire"
        self.nom = nom
        self.sante = 80
        self.sante_max = 80
    

class Squelette(Entités):
    def __init__(self, nom:str) -> None:
        Entités.__init__(self)
        self.race = "squelette"
        self.nom = nom
        