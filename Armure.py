datas = {
    "armure de cuire" : 2,
    "cotte de maille" :  5,
    "armure de chevalier" : 10
}

class Armure():
    def __init__(self) -> None:
        self.nom = ""
        self.defense = 0
        
    def equiper_armure(self, armure):
        global datas
        self.nom = armure
        self.defense = datas[armure]
        