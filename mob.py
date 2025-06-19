from Entites import Entites
       
class paysan(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.loot = {25 : "baton", 1 : "armure de cuire"}
        self.force = 3
        self.sante = 20
        self.xp_drop = 1
        
class appreneis_chevalier(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.loot = {10 : "gros_baton", 1 : "cotte de maille"}
        self.force = 6
        self.sante = 40
        self.xp_drop = 10
    
class chevalier(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.loot = {5 : "epee", 1 : "armure de chevalier"}
        self.force = 12
        self.sante = 80
        self.xp_drop = 40