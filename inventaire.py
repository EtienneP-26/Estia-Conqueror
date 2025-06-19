class Inventaire(object):
    def __init__(self) -> None:
        self.taille_inventaire = 5
        self.nb_objets = 0
        self.nom_ressources_inventaire = [None for i in range(self.taille_inventaire)]
        self.nombre_ressources_inventaire = [None for i in range(self.taille_inventaire)]
        self.ressources_classes_inventaire = [None for i in range(self.taille_inventaire)]

    def augmentation_inventaire(self, taille_en_plus):
        for i in range(self.taille_inventaire):
            self.nom_ressources_inventaire.append(None)
            self.nombre_ressources_inventaire.append(None)
            self.ressources_classes_inventaire.append(None)
            self.taille_inventaire += 1

    def ajout_inventaire(self, nom, nb, classe):
        if self.nb_objets < self.taille_inventaire:
            self.nom_ressources_inventaire[self.nb_objets] = nom
            self.nombre_ressources_inventaire[self.nb_objets] = nb
            self.ressources_classes_inventaire[self.nb_objets] = classe
            self.nb_objets += 1
        else :
            print("Inventaire est plein !")

    def __str__(self) -> str:
        txt_return = "INVENTAIRE : \n"
        for i in range(self.taille_inventaire):
            if self.nom_ressources_inventaire[i] != None:
                txt_return += str(self.nom_ressources_inventaire[i]) + " : " + str(self.nombre_ressources_inventaire[i]) + "\n"
        return txt_return
            