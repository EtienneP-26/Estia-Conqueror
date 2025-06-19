import pygame,time
import subprocess
from Entites import Entites

# Initialisation
pygame.init()

# Paramètres de la fenêtre
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Adventure Game")
screen.fill([0, 192, 77])

# Chargement de l'image du personnage

player = Entites()
player_size = player.taille

player_standing_L = pygame.image.load(player.img_psL)
player_standing_L = pygame.transform.scale(player_standing_L, (player_size, player_size+50))
 
player_standing_R = pygame.image.load(player.img_psR)
player_standing_R = pygame.transform.scale(player_standing_R, (player_size, player_size+50))
 
player_standing_L_running_1 = pygame.image.load(player.img_psL_running_1)
player_standing_L_running_1 = pygame.transform.scale(player_standing_L_running_1, (player_size, player_size+50))
 
player_standing_L_running_2 = pygame.image.load(player.img_psL_running_2)
player_standing_L_running_2 = pygame.transform.scale(player_standing_L_running_2, (player_size, player_size+50))
 
player_standing_R_running_1 = pygame.image.load(player.img_psR_running_1)
player_standing_R_running_1 = pygame.transform.scale(player_standing_R_running_1, (player_size, player_size+50))
 
player_standing_R_running_2 = pygame.image.load(player.img_psR_running_2)
player_standing_R_running_2 = pygame.transform.scale(player_standing_R_running_2, (player_size, player_size+50))


# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
gray = (100, 100, 100)
bush_color = (55, 255, 55)

font = pygame.font.Font(None, 36)

# Bouton
button_width = 150
button_height = 50
button_x = 650
button_y = 40
button_color = gray
button_text = "inventory"
button_font = pygame.font.Font(None, 36)
def inventory():
    print(player.inventaire)

# Personnage

player_x = (screen_width - player_size) // 2
player_y = (screen_height - player_size) // 2
player_speed = player.vitesse
  
time_btw_mvt = 250
mvt_event = pygame.USEREVENT + 1
pygame.time.set_timer(mvt_event,time_btw_mvt)


bush = (150,350)
bush_life = 100
chest = (375, 540, 80, 40)
chest_contour = (365, 530, 100, 60)

# Boucle principale
running = True
clock = pygame.time.Clock()

player_img_affiché = player_standing_L
run = 1
direction = "L"
count_time = 1
time_digits = 2
start_movement_time = 0
en_mvt = False
score = 0
nb_vie = 3
visuel_vie = ""
tps_btw_mvt = 1
cooldown_btw_act = 2
count_cooldown_btw_act = 1

while running:
    screen.fill(white)
    if bush_life > 0 :
        pygame.draw.circle(screen, bush_color, (bush[0], bush[1]), 20)
    pygame.draw.rect(screen, (100, 35, 10), chest_contour)
    pygame.draw.rect(screen, (200, 100, 0), chest)

    all_keys_released = all(event.type == pygame.KEYUP for event in pygame.event.get(pygame.KEYUP))
    if all_keys_released :
        if en_mvt == False:
            if direction == "L":
                player_img_affiché = player_standing_L
            if direction == "R":    
                player_img_affiché = player_standing_R
        else : en_mvt = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                inventory()


    # Gérer les déplacements du personnage
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] or keys[pygame.K_LEFT]:
        player_x -= player_speed
        direction = "L"
        en_mvt = True
        """if movement_possible :
            if run == 1 :
                player_img_affiché = player_standing_L_running_1
                run = 2
            elif run == 2 :
                player_img_affiché = player_standing_L_running_2
                run = 1
            movement_possible = False"""

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_x += player_speed
        direction = "R"
        en_mvt = True
        """if movement_possible :
            if run == 1 :
                player_img_affiché = player_standing_R_running_1
                run = 2
            elif run == 2 :
                player_img_affiché = player_standing_R_running_2
                run = 1  
            movement_possible = False"""

    if keys[pygame.K_z] or keys[pygame.K_UP]:
        player_y -= player_speed
        en_mvt = True
        """if movement_possible :
            if run == 1 and direction == "L":
                player_img_affiché = player_standing_L_running_1
                run = 2
            elif run == 2 and direction == "L":
                player_img_affiché = player_standing_L_running_2
                run = 1
            elif run == 1 and direction == "R":
                player_img_affiché = player_standing_R_running_1
                run = 2
            elif run == 2 and direction == "R":
                player_img_affiché = player_standing_R_running_2
                run = 1   
            movement_possible = False  """

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_y += player_speed
        en_mvt = True
        """if movement_possible :
            if run == 1 and direction == "L":
                player_img_affiché = player_standing_L_running_1
                run = 2
            elif run == 2 and direction == "L":
                player_img_affiché = player_standing_L_running_2
                run = 1
            elif run == 1 and direction == "R":
                player_img_affiché = player_standing_R_running_1
                run = 2
            elif run == 2 and direction == "R":
                player_img_affiché = player_standing_R_running_2
                run = 1
            movement_possible = False"""

    if bush_life > 0 :    
        if bush[0]-50 - player_size < player_x < bush[0]+50 and bush[1]-50 - player_size < player_y < bush[1]+50 :
            aff_interacte = font.render(f"[E]", True, black)
            aff_interacte_rect = aff_interacte.get_rect(center=(bush[0]+10, bush[1]+10))
            screen.blit(aff_interacte, aff_interacte_rect)
            if keys[pygame.K_e]:
                if count_cooldown_btw_act >= cooldown_btw_act:
                    print("joueur a interagie avec buisson")
                    count_cooldown_btw_act = 1
                else : count_cooldown_btw_act += 1

        if bush[0]-player.distance_attaque - player_size < player_x < bush[0]+player.distance_attaque and bush[1]-player.distance_attaque - player_size < player_y < bush[1]+player.distance_attaque :
            aff_interacte = font.render(f"[A]", True, black)
            aff_interacte_rect = aff_interacte.get_rect(center=(bush[0]+10, bush[1]+10))
            screen.blit(aff_interacte, aff_interacte_rect)
            if keys[pygame.K_a]:
                if count_cooldown_btw_act >= cooldown_btw_act:
                    bush_life -= 10
                    if bush_life <= 0 :
                        score += 10
                        player.inventaire.ajout_inventaire("baton", 2, None)
                        player.inventaire.ajout_inventaire("baie", 1, None)
                    aff_enemi_life = font.render(f"{bush_life}", True, black)
                    aff_enemi_life_rect = aff_enemi_life.get_rect(center=(bush[0], bush[1]-10))
                    screen.blit(aff_enemi_life, aff_enemi_life_rect)
                    count_cooldown_btw_act = 1
                else : count_cooldown_btw_act += 1

    if chest[0]-50 - player_size < player_x < chest[0]+chest[2]+50 and chest[1]-50 - player_size < player_y < chest[1]+chest[3]+50 :
        aff_interacte = font.render(f"[E]", True, black)
        aff_interacte_rect = aff_interacte.get_rect(center=(chest[0]+chest[2]+10, chest[1]+chest[3]+10))
        screen.blit(aff_interacte, aff_interacte_rect)
        if keys[pygame.K_e]:
            if count_cooldown_btw_act >= cooldown_btw_act:
                print("joueur a interagie avec chest")
                count_cooldown_btw_act = 1
            else : count_cooldown_btw_act += 1

    if en_mvt :
        if tps_btw_mvt >= 3:
            if run == 1 and direction == "L":
                player_img_affiché = player_standing_L_running_1
                run = 2
            elif run == 2 and direction == "L":
                player_img_affiché = player_standing_L_running_2
                run = 1
            elif run == 1 and direction == "R":
                player_img_affiché = player_standing_R_running_1
                run = 2
            elif run == 2 and direction == "R":
                player_img_affiché = player_standing_R_running_2
                run = 1
            tps_btw_mvt = 1
        else : tps_btw_mvt += 1

    if keys[pygame.K_h] :
        if count_cooldown_btw_act >= cooldown_btw_act:
            print("help")
            count_cooldown_btw_act = 1
        else : count_cooldown_btw_act += 1

    
    aff_score = font.render(f"SCORE : {score}", True, black)
    aff_score_rect = aff_score.get_rect(center=(720, 20))
    screen.blit(aff_score, aff_score_rect)

    for vie in range(nb_vie):
        visuel_vie += "V "

    aff_vie = font.render(f"{visuel_vie}", True, black)
    aff_vie_rect = aff_vie.get_rect(center=(60, 20))
    screen.blit(aff_vie, aff_vie_rect)

    visuel_vie = ""

    # Empêcher le personnage de sortir de l'écran
    player_x = max(0, min(player_x, screen_width - player_size))
    player_y = max(0, min(player_y, screen_height - player_size+10))

    # Dessiner le bouton
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    text_surface = button_font.render(button_text, True, black)
    text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(text_surface, text_rect)

    # Afficher l'image du personnage
    screen.blit(player_img_affiché, (player_x, player_y))
    time.sleep(0.05)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
