from Joueur import Joueur
from mob import *
from race import *


def choix_de_la_race():
    verif_choix = True
    while verif_choix:
        print('choix de la race : ')
        print('les differentes races sont \n1 - Gobelin\n2 - squelette\n3 - Orc\n4 - vampire\n5 - elf noir\n6 - centaure')
        choix = str(input('choix : '))
        r1=Gobelin()
        r2=Squelette()
        r3=Orc()
        r4=Vampire()
        r5=Elf_noir()
        r6=Centaure()
        if choix == "1":
            choix = r1
        elif choix == "2":
            choix = r2
        elif choix == "3":
            choix = r3
        elif choix == "4":
            choix = r4
        elif choix == "5":
            choix = r5
        elif choix == "6":
            choix = r6
        print(f'vous avez choisi {choix.nom_classe}')
        verif_choix = False if str(input("etes vous sur de ce choix (oui/non): ")) == "oui" else True
    return choix

joueur = choix_de_la_race()

print(joueur.en_vie())

print(joueur)