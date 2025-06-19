from Entites import Entites
from race import*
class Joueur(Entites):
    def __init__(self, race):
        race.__init__(self)
        self.race = race
        self.inventaire = []