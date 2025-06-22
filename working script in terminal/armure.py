class Armure(object):
    def __init__(self, nom:str = "veste", defense:int = 0):
        self.nom = nom
        self.defense = defense

    def __str__(self) -> str:
        return f"{self.nom} : {self.defense} pts de defenses "