
datas = {
    "poings": 0,
    "baton": 2, 
    "gros_baton": 5, 
    "epee": 10
}

class Arme(object):
    def __init__(self) -> None:
        self.nom = "poings"
        self.degats = 0

    def equiper_arme(self, arme):
        global datas
        self.nom = arme
        self.degats = datas[arme]
