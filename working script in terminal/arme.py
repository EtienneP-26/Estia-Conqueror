class Arme(object):
    def __init__(self, nom:str = "mains", degats:int = 0):
        self.nom = nom
        self.degats = degats

    def __str__(self) -> str:
        return  f" {self.nom} : {self.degats} degats"
        