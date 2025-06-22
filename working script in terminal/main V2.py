from entités import Entités
from race import Goblin
from race import Vampire
from race import Squelette
from humain import Humain
from humain import Chevalier
from arme import Arme
from armure import Armure
from humain import Tyranoporc

import sys
from random import randint
import pandas as pnd
from time import sleep
from time import perf_counter

nom_joueur = ""
objets = pnd.read_json("objets.json")


def delete_last_line(n:int):
    for i in range (n):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

def smooth_print(txt:str=" "):
    time_cooldown = 0.1
    nb_lignes = txt.count("\n") if "\n" in txt else 1
    for lettre in range(len(txt)):
        print(txt[:lettre])
        sleep(time_cooldown)
        delete_last_line(nb_lignes)
    print(txt, end = "")


delete_last_line(2)

################################################ init perso et bot #######################################################

def choix_combat():
    while True:
        smooth_print("que faire :\n - attaque\n - fuire")
        choix = str(input()).lower()
        if choix == "1" or choix == "attaque" or choix == "a" or choix == "att" or choix == "attaquer" or choix == "attaqué":
            return "attaque"
        elif choix == "2" or choix == "fuire" or choix == "f" or choix == "fui" or choix == "fuite":
            return "fuite"
        else : smooth_print("erreur entrée")

def ennemi_attaque():
        chance_attaque = randint(1,4)
        if chance_attaque == 1:
            return "échoué"
        return "attaque"

def boss_attaque():
        chance_attaque = randint(1,10)
        if chance_attaque == 1:
            return "échoué"
        elif chance_attaque == 3 or chance_attaque == 6 :
            return "critique"
        return "attaque"

def fin_jeu():
    global jeu
    global temps_de_jeu_debut
    global J1
    delete_last_line(6)
    smooth_print("Vous etes mort")
    temps_de_jeu_fin = perf_counter()
    temps_de_jeu = float(str(temps_de_jeu_fin - temps_de_jeu_debut)[:len(str(temps_de_jeu_fin))-6])
    print("         LOSE         \n")
    print(f"vous avez fini le jeu en {temps_de_jeu//3600} h {temps_de_jeu//60-3600*(temps_de_jeu//3600)} m {temps_de_jeu-(60*(temps_de_jeu//60)+3600*(temps_de_jeu//3600))} s")
    print(J1)
    jeu = False    

partir = True
jeu = True

############################################### jeu #################################################

while jeu:
    temps_de_jeu_debut = perf_counter()

    nom_joueur = str(input("Cher \nentrez votre nom : "))
    delete_last_line(2)
    smooth_print(f"Cher {nom_joueur},\nnous vous informons que le tout puissant Roi Démon vous fait l'honneur à vous pauvre\n")


    smooth_print("1 - goblin (+XP/-attaque)\n2 - vampire(+regeneration santé/-sante)\n3 - squelette(aucun bonus)\n")
    race_joueur = str(input("")).lower()
    if race_joueur == "1" or race_joueur == "goblin" or race_joueur == "g":
        J1 = Goblin(nom_joueur)
    if race_joueur == "2" or race_joueur == "vampire" or race_joueur == "v":
        J1 = Vampire(nom_joueur)
    if race_joueur == "3" or race_joueur == "squelette" or race_joueur == "s":
        J1 = Squelette(nom_joueur)
    
    delete_last_line(8)

    smooth_print(f"Cher {nom_joueur},\nnous vous informons que le tout puissant Roi Démon, Belzebuth, vous fait l'honneur à vous pauvre {J1.race} inferieur, de vous e̶x̶p̶l̶o̶i̶t utiliser a des fins militaires en vous ordonnant de capturer le royaume d'Estia. Cependant, je tiens à vous prevenir méfier vous du Tyranoporc.")
    input("pressez une touche")
    delete_last_line(6)

    while partir:
        smooth_print("choix : \n - partir à l'aventure\n - rester chez soi")
        choix = str(input()).lower()
        if choix == "partir à l'aventure" or choix == "partir à l'aventure" or choix == "partir" or choix == "l'aventure" or choix == "aventure" or choix == "1" or choix == "p":
            delete_last_line(4)
            smooth_print("Vous partez alors à l'aventure, les cheuveux au vent")
            input("pressez une touche")
            delete_last_line(4)
            smooth_print("Après être sorti du monde des demons, un humain vous voit et vous attaque instantanement")
            input("pressez une touche")
            delete_last_line(4)
            combat = True

            h1 = Humain()

            while combat:
                # attaque de l'ennemi
                chance_attaque = ennemi_attaque()
                if chance_attaque == "attaque":
                    h1.attaque(J1)
                    smooth_print(f"l'humain vous a attaqué et vous a retiré {h1.force} de santé")
                elif chance_attaque == "échoué":
                    smooth_print("l'humain vous a loupé")

                input("pressez une touche")
                delete_last_line(4)
                smooth_print(f"votre santé : {J1.sante}")
                smooth_print(f"santé de l'ennemi : {h1.sante}")

                # attaque du joueur
                choix = choix_combat()
                if choix == "attaque":
                    J1.attaque(h1)
                elif choix == "fuite":
                    combat = False
                    smooth_print("vous avez fuit")
                    break
                else : smooth_print("erreur d'entrée")

                delete_last_line(4)

                if h1.sante <= 0:
                    combat = False
                    smooth_print("vous avez tuer l'humain. Bravo !")
                    smooth_print("l'humain a fait tomber un baton")
                    prendre = input("prendre ? : ").lower()
                    if prendre == "o" or prendre == "oui" or prendre == "p" or prendre == "prendre":
                        J1.arme = Arme(objets["armes"]["baton"]["nom"], objets["armes"]["baton"]["degats"])
                        smooth_print("vous avez pris le baton")
                        input("pressez une touche")
                    elif prendre == "n" or prendre == "non":
                        J1.arme = Arme()
                        smooth_print("vous avez pris le baton")
                        input("pressez une touche")
                    else : 
                        smooth_print("erreur d'entrée")
                        input("pressez une touche")
                    
                if J1.sante <= 0:
                    combat = False
                    fin_jeu()

            if J1.sante <= 0:
                break

            input("pressez une touche")
            delete_last_line(8)

            # deuxieme combat
            
            smooth_print("Après avoir fait une courte pause vous décidez de repartir vers Estia. C'est alors que vous recroisez un humain et que vous decidez de l'attaquer")
            input("pressez une touche")
            delete_last_line(8)

            combat = True

            h2 = Humain()

            while combat:
                # attaque de l'ennemi
                chance_attaque = ennemi_attaque()
                if chance_attaque == "attaque":
                    h2.attaque(J1)
                    smooth_print(f"l'humain vous a attaqué et vous a retiré {h2.force} de santé")
                elif chance_attaque == "échoué":
                    smooth_print("l'humain vous a loupé")
                
                input("pressez une touche")
                delete_last_line(8)
                smooth_print(f"votre santé : {J1.sante}")
                smooth_print(f"santé de l'ennemi : {h2.sante}")

                # attaque du joueur
                choix = choix_combat()
                if choix == "attaque" or choix == "att" or choix == "a" or choix == "attaquer" or choix == "attaqué":
                    J1.attaque(h2)
                elif choix == "fuite" or choix == "f" or choix == "fuire":
                    combat = False
                    smooth_print("vous avez fuit")
                    break
                else : smooth_print("erreur d'entrée")

                delete_last_line(4)

                if h2.sante <= 0:
                    combat = False
                    smooth_print("vous avez tuer l'humain. Bravo !")

                if J1.sante <= 0:
                    combat = False
                    fin_jeu()

            if J1.sante <= 0:
                break
            
            input("pressez une touche")
            delete_last_line(8)

            # troisieme combat
            smooth_print("Vous prenez alors la forêt menant vers Estia, et sur votre chemin vous croisez un humain desorienté et plutôt que de lui venir en aide vous en profitez pour l'attaquer")
            input("pressez une touche")
            delete_last_line(8)

            combat = True

            h3 = Humain()

            while combat:
                # attaque de l'ennemi
                chance_attaque = ennemi_attaque()
                if chance_attaque == "attaque":
                    h3.attaque(J1)
                    smooth_print(f"l'humain vous a attaqué et vous a retiré {h3.force} de santé")
                elif chance_attaque == "échoué":
                    smooth_print("l'humain vous a loupé")

                input("pressez une touche")
                delete_last_line(8)
                smooth_print(f"votre santé : {J1.sante}")
                smooth_print(f"santé de l'ennemi : {h3.sante}")

                # attaque du joueur
                choix = choix_combat()
                if choix == "attaque" or choix == "att" or choix == "a" or choix == "attaquer" or choix == "attaqué":
                    J1.attaque(h3)
                elif choix == "fuite" or choix == "f" or choix == "fuire":
                    combat = False
                    smooth_print("vous avez fuit")
                    break
                else : smooth_print("erreur d'entrée")

                delete_last_line(4)

                if h3.sante <= 0:
                    combat = False
                    smooth_print("vous avez tuer l'humain. Bravo !")
                    smooth_print("l'humain a fait tomber un objet mysterieux")
                    prendre = input("prendre ? : ").lower()
                    if prendre == "o" or prendre == "oui" or prendre == "p" or prendre == "prendre":
                        J1.item = 1
                        smooth_print("vous avez pris l'objet mysterieux")
                        input("pressez une touche")
                    elif prendre == "n" or prendre == "non":
                        smooth_print("vous avez pris l'objet mysterieux")
                        input("pressez une touche")
                    else : 
                        smooth_print("erreur d'entrée")
                        input("pressez une touche")
                    
                if J1.sante <= 0:
                    combat = False
                    fin_jeu()
 
            if J1.sante <= 0:
                break

            delete_last_line(8)

            smooth_print("Après ce combat vous rencontrez un marchand\nMarchand : Bien le bonjour cher voyageur, on peut voir que vous êtes un fiere guerrier, qui se bat avec ....\nun baton !?\nCa tombe bien !!! J'ai un baton digne votre de votre grandeur\nLE SAINT BATON !!!!!")
            input("pressez une touche")
            delete_last_line(1)
            marchand = str(input("êtes vous intéressé (nécessaire -> un objet mysterieux): ")).lower()
                
            if J1.item == 1:
                if marchand == "oui" or marchand == "o" or marchand == "i" or marchand == "interesse" or marchand == "intéressé":
                   J1.arme = Arme(objets["armes"]["le Saint Baton"]["nom"], objets["armes"]["le Saint Baton"]["degats"])
                   J1.item = 0
                   delete_last_line(4)
                   smooth_print("vous prenez alors le Saint Baton")
                   input("pressez une touche")
                   delete_last_line(4)
                elif marchand == "non" or marchand == "n":
                   delete_last_line(4)
                   smooth_print("vous avez refusé le Saint Baton")
                   input("pressez une touche")
                   delete_last_line(4)
                else : smooth_print("erreur d'entrée")
            else: smooth_print("vous n'avais pas l'item nécessaire") 

            input("pressez une touche")
            delete_last_line(4)

            # quatrieme combat
            
            smooth_print("")

            combat = True

            c1 = Chevalier()

            while combat:
                # attaque de l'ennemi
                chance_attaque = ennemi_attaque()
                if chance_attaque == "attaque":
                    c1.attaque(J1)
                    smooth_print(f"l'humain vous a attaqué et vous a retiré {c1.force} de santé")
                elif chance_attaque == "échoué":
                    smooth_print("l'humain vous a loupé")

                input("pressez une touche")
                delete_last_line(8)
                smooth_print(f"votre santé : {J1.sante}")
                smooth_print(f"santé de l'ennemi : {c1.sante}")

                # attaque du joueur
                choix = choix_combat()
                if choix == "attaque" or choix == "att" or choix == "a" or choix == "attaquer" or choix == "attaqué":
                    J1.attaque(c1)
                elif choix == "fuite" or choix == "f" or choix == "fuire":
                    combat = False
                    smooth_print("vous avez fuit")
                    break
                else : smooth_print("erreur d'entrée")

                delete_last_line(4)

                if c1.sante <= 0:
                    combat = False
                    smooth_print("vous avez tuer l'humain. Bravo !")
                    smooth_print("le chevalier fait tomber des fragments d'armure")
                    prendre = input("prendre ? : ").lower()
                    if prendre == "o" or prendre == "oui" or prendre == "p" or prendre == "prendre":
                        J1.item = 2
                        smooth_print("vous avez pris fragments d'armure")
                    elif prendre == "n" or prendre == "non":
                        smooth_print("vous avez pris l'objet mysterieux")
                    else : smooth_print("erreur d'entrée")
                    
                if J1.sante <= 0:
                    combat = False
                    fin_jeu()

            if J1.sante <= 0:
                break
        
            input("pressez une touche")
            delete_last_line(8)
            
            smooth_print("Vous arrivez finalement dans le marché d'Estia et un nain forgeron vous interpelle\nNain Forgeron : Bakn galikh aventurier,\nje propose deux type d'armure\n - un manteau\n - une cotte de maille")
            forgeron = str(input("êtes vous intéressé (nécessaire -> fragments d'armure): ")).lower()
                
            if J1.item == 2:
                if forgeron == "manteau" or forgeron == "m":
                   J1.armure = Armure(objets["armures"]["manteau"]["nom"], objets["armures"]["manteau"]["defence"])
                   J1.item = 0
                   delete_last_line(8)
                   smooth_print("vous prenez alors manteau")
                elif forgeron == "cotte de mailles" or forgeron == "c" or forgeron == "cdm" or forgeron == "cotte" or forgeron == "mailles" or forgeron == "maille":
                   J1.armure = Armure(objets["armures"]["cotte de mailles"]["nom"], objets["armures"]["cotte de mailles"]["defence"])
                   J1.item = 0
                   delete_last_line(8)
                   smooth_print("vous prenez alors cotte de mailles")
                elif forgeron == "non" or forgeron == "n":
                    delete_last_line(8)
                    smooth_print ("vous refusez sont offre et continuez")
                else : smooth_print("erreur d'entrée")
            else: smooth_print("vous n'avais pas l'item nécessaire") 

            delete_last_line(8)
            input("pressez une touche")
            delete_last_line(4)

            smooth_print("Au sol, vous apercevez une pomme très rouge")
            choix = input("que faire manger la pomme ou continuer : ").lower()
            if choix == "m" or choix == "manger" or choix == "mange" or choix == "manger la pomme" or choix == "pomme" or choix == "la pomme" or choix == "mange la pomme" or choix == "mangé la pomme":
                smooth_print("vous manger la pomme est vous vous sentez comme remis de tout ce qui c'est passé de puis le début de votre voyage")
                J1.sante = J1.sante_max
            else : smooth_print("vous faite comme si vous ne l'aviez pas vue et continuer votre chemin")

            delete_last_line(8)
            input("pressez une touche")
            delete_last_line(4)

            smooth_print("Vous sortez du marché et vous vous rapprochez du château jusqu'à ce que vous arriviez à la porte par laquelle vous entrez sans hésitation")
            input("pressez une touche")
            delete_last_line(4)
            
            #combat de boss
            smooth_print("Dans la cour château se tenait une imposante créature mistérieuse et qui dégage une pression incroyable est-ce un T-rex ? Non est-ce un porc ? Non plus. C'est donc un Tyranoporc la créature la plus puissante de Estia")
            input("pressez une touche")
            delete_last_line(4)

            combat = True

            t1 = Tyranoporc()

            while combat:
                # attaque de l'ennemi
                chance_attaque = boss_attaque()
                if chance_attaque == "attaque":
                    t1.attaque(J1)
                    smooth_print(f"le Tyranoporc vous a attaqué et vous a retiré {t1.force} de santé")
                elif chance_attaque == "critique":
                    t1.attaque_critique(J1)
                    smooth_print(f"le Tyranoporc vous a attaqué avec une puissante attaque et vous a retiré {t1.force_critique} de santé")
                elif chance_attaque == "échoué":
                    smooth_print("le Tyranoporc vous a loupé")

                input("pressez une touche")
                delete_last_line(4)
                smooth_print(f"votre santé : {J1.sante}")
                smooth_print(f"santé de l'ennemi : {t1.sante}")

                # attaque du joueur
                choix = choix_combat()
                if choix == "attaque" or choix == "att" or choix == "a" or choix == "attaquer" or choix == "attaqué":
                    J1.attaque(t1)
                elif choix == "fuite" or choix == "f" or choix == "fuire":
                    combat = False
                    fuite_boss = True
                    smooth_print("vous avez tentez de fuire et le Tyranoporc vous a écrasé")
                    fin_jeu()
                    break
                else : smooth_print("erreur d'entrée")

                delete_last_line(8)

                if t1.sante <= 0:
                    combat = False
                    smooth_print("Après un rude combat acharné vous ressortez vainqueur d'un duel dont vous vous souviendrez toute votre vie")
                    
                if J1.sante <= 0:
                    combat = False
                    fin_jeu()
            
            if J1.sante <= 0:
                break

            if fuite_boss:
                break

            # fin du jeu 
            delete_last_line(8)
            temps_de_jeu_fin = perf_counter()
            temps_de_jeu = float(str(temps_de_jeu_fin - temps_de_jeu_debut)[:len(str(temps_de_jeu_fin))-6])
            smooth_print("Vous entrez dans la grande salle du château et le Roi est assis sur son trône au bout de celle-ci\nVous le défiez\nIl se lève et s'approche de vous de manière menacante\nEn decendant des marches, il se prends les pieds dans sa chappe, tombe et se brise la nuque")
            input("pressez une touche")
            delete_last_line(6)
            smooth_print(f"Belzebuth, surpris qu'un simple {J1.race} ai pu reussir cette tache et vous nomme alors Chevalier du Roi Démon et vous confie la direction du Royaume d'Estia")
            input("pressez une touche")
            delete_last_line(6)
            smooth_print("         WIN         \n")
            smooth_print(f"vous avez fini le jeu en {temps_de_jeu//3600} h {temps_de_jeu//60-3600*(temps_de_jeu//3600)} m {temps_de_jeu-(60*(temps_de_jeu//60)+3600*(temps_de_jeu//3600))} s")
            smooth_print(J1)
            jeu = False
            break

        elif choix == "rester chez soi" or choix == "chez soi" or choix == "rester" or choix == "2" or choix == "r":
            smooth_print("vous n'avez pas respectez les demandes de Belzebuth, il vous a condamné à mort")
            input("pressez une touche")
            delete_last_line(4)
            fin_jeu()
            break
        else : smooth_print("erreur d'entrée")