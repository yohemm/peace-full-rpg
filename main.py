from builtins import len

import pygame
import pickle

pygame.init()
cam_size_x = 1280
cam_size_y = 720

pygame.display.set_caption('Oriona')
screen = pygame.display.set_mode((cam_size_x, cam_size_y))


###################################### Fonction ######################################


################### SAUVEGARDE ###################


#Sauvegarde les avancées
def sauver(x, y, inventory, money, quests, items):
    data = {}
    data["x"] = x
    data["y"] = y
    data["inventory"] = inventory
    data["money"] = money
    data["quest"] = quests
    data["items"] = items
    data["camera_x"] = camera_x
    data["camera_y"] = camera_y
    with open("data.oriona", "wb") as fw:
        pickle.dump(data, fw)
        fw.close()


#Sauvegarde les avancées
def charger():
    with open("data.oriona", "rb") as fr:
        data = pickle.load(fr)
        fr.close()
    return data["x"], data["y"], data["inventory"], data["money"], data["quest"], data["items"], data["camera_x"], data["camera_y"]


################### ITEM ###################


# Acffiche l'inventaire
def blit_inventory():
    global inventory
    global bag_inventory_frame
    global bag_image
    bag_image = pygame.transform.scale(BAG_INVENTORY[bag_inventory_frame], (800, 800)).convert_alpha()
    if bag_inventory_frame == len(BAG_INVENTORY) - 1:
        message_on_mouse = ''
        nb_case = 8
        size_case = bag_image.get_width()//2 // nb_case
        police = pygame.font.Font(None, 40)
        mousse_x, mousse_y = pygame.mouse.get_pos()
        for case_y in range(nb_case * 2):
            for case_x in range(nb_case):
                if not 10 * case_y + case_x > len(inventory) - 1:
                    rect = (bag_image.get_width()//4 + case_x*size_case + (size_case - ORION.get_width())//2, bag_image.get_height()//4 + case_y*size_case)
                    if inventory[10 * case_y + case_x][0] == 'Orion':
                        bag_image.blit(ORION, rect)
                    elif inventory[10 * case_y + case_x][0] == 'Letter':
                        bag_image.blit(LETTER, rect)
                    elif inventory[10 * case_y + case_x][0] == 'Key':
                        bag_image.blit(KEY, rect)
                    elif inventory[10 * case_y + case_x][0] == 'Weed':
                        bag_image.blit(WEED, rect)
                    elif inventory[10 * case_y + case_x][0] == 'Spliff':
                        bag_image.blit(SPLIFF, rect)
                    elif inventory[10 * case_y + case_x][0] == 'Pouch':
                        bag_image.blit(POUCH, rect)
                    else:
                        bag_image.blit(ORION, rect)
                    if size_case + rect[0] + (screen.get_width() - bag_image.get_width()) // 2 >= mousse_x >= \
                            rect[0] + (screen.get_width() - bag_image.get_width()) // 2 and size_case + rect[
                        1] + screen.get_height() - bag_image.get_height() >= mousse_y >= rect[
                        1] + screen.get_height() - bag_image.get_height():
                        message_on_mouse = str( inventory[10 * case_y + case_x][0]) + ' x' + str(inventory[10 * case_y + case_x][1])
                        message = ''
                        mousse_affichage = police.render(message_on_mouse, 1, (0, 0, 0))
                    else:
                        message = str(inventory[10 * case_y + case_x][1])

                    affichage = police.render(message, 1, (0,0,0))
                    bag_image.blit(affichage, (bag_image.get_width()//4 + case_x*size_case + (size_case - police.size(message)[0]), bag_image.get_height()//4 + case_y*size_case + size_case - police.size(message)[1]))
                else:
                    break
        if not message_on_mouse == '':
            rect = pygame.rect.Rect((mousse_x - (screen.get_width() - bag_image.get_width()) // 2,
                                     abs(screen.get_height() - bag_image.get_height() - mousse_y) + 15),
                                    (mousse_affichage.get_width(), mousse_affichage.get_height()))
            surface = pygame.surface.Surface((rect.width, rect.height))
            surface.fill((125, 125, 125))
            surface.blit(mousse_affichage, (0, 0))
            bag_image.blit(surface, (rect.left, rect.top))
    else:
        bag_inventory_frame = Switch_frame(100, bag_inventory_frame)
    screen.blit(bag_image, ((screen.get_width() - bag_image.get_width())//2, screen.get_height() - bag_image.get_height()))


# Vérifie si l'item est dans l'inventaire
def check_item(item, nb):
    global inventory
    for stuff in inventory:
        if stuff[0] == item and stuff[1] >= nb:
            return True
    return False


# supprime un/des items dans l'inventaire
def del_item(item, nb):
    global inventory
    for case in range(len(inventory)):
        if inventory[case][0] == item:
            if inventory[case][1] > nb:
                inventory[case][1] -= nb
            elif inventory[case][1] == nb:
                del inventory[case]
            else:
                return False
            print(inventory)
            return True


# Ajoute un/des item dans l'inventaire
def take_item(item, nb):
    global inventory
    for stuff in inventory:
        if stuff[0] == item:
            stuff[1] += nb
            print('inventory :', inventory)
            return
    inventory.append([item, 1])
    print('inventory :', inventory)


# ajoute un item dans l'inventaire et le supprime de la map
def find_item():
    global items
    global all_pages
    finish = False
    while True:
        for item in range(len(items)):
            items[item][3] = range_calculator((x, y), items[item])
            if items[item][3] == True:
                take_item(items[item][2], 1)
                print('item in map :', items)
                del items[item]
                finish = False
                break
            finish = True
        if finish == True:
            return




################### ANIMATION ###################

# Change l'image de l'annimation
def Switch_frame(frame_rate, frame_animation):
    global current_time
    if pygame.time.get_ticks() - current_time > frame_rate:
        current_time = pygame.time.get_ticks()
        frame_animation += 1
    return frame_animation


# Animation des btns du menu
def menu():
    global btn_play
    global settings_frame
    global leave_frame
    global play_frame
    global btn_leave
    global btn_settings
    global is_paused

    mousse_x, mousse_y = pygame.mouse.get_pos()
    pos_play = (cam_size_x/2 - btn_play.get_width()/2, (cam_size_y/3 - btn_play.get_height()/2) - 20)
    pos_leave = (cam_size_x/2 - btn_leave.get_width()/2, (cam_size_y/3*2 - btn_leave.get_height()/2) + 20)
    pos_settings = (20, 20)
    screen.blit(btn_settings,pos_settings)
    screen.blit(btn_leave,pos_leave)
    screen.blit(btn_play,pos_play)

    if pos_play[0] < mousse_x < pos_play[0] + btn_play.get_width() and pos_play[1] < mousse_y < pos_play[1] + btn_play.get_height():
        if pygame.mouse.get_pressed()[0]:
            is_paused = False
        if not len(PLAY_ANIMATION) - 1 == play_frame % len(PLAY_ANIMATION) :
            play_frame = Switch_frame(100, play_frame)
        btn_play = PLAY_ANIMATION[play_frame % len(PLAY_ANIMATION)]
        btn_play = pygame.transform.scale(btn_play, (576, 240)).convert_alpha()
    elif not btn_play == pygame.transform.scale(PLAY_ANIMATION[0], (576, 240)).convert_alpha():
        play_frame = 0
        btn_play = PLAY_ANIMATION[0]
        btn_play = pygame.transform.scale(btn_play, (576, 240)).convert_alpha()

    if pos_leave[0] < mousse_x < pos_leave[0] + btn_leave.get_width() and pos_leave[1] < mousse_y < pos_leave[1] + btn_leave.get_height():
        if pygame.mouse.get_pressed()[0]:
            sauver(x,y,inventory,money,quests,items)
            pygame.quit()
        if not len(LEAVE_ANIMATION) - 1 == leave_frame % len(LEAVE_ANIMATION) :
            leave_frame = Switch_frame(100, leave_frame)
        btn_leave = LEAVE_ANIMATION[leave_frame % len(LEAVE_ANIMATION)]
        btn_leave = pygame.transform.scale(btn_leave, (576, 240)).convert_alpha()
    elif not btn_leave == pygame.transform.scale(LEAVE_ANIMATION[0], (576, 240)).convert_alpha():
        leave_frame = 0
        btn_leave = LEAVE_ANIMATION[0]
        btn_leave = pygame.transform.scale(btn_leave, (576, 240)).convert_alpha()

    if pos_settings[0] < mousse_x < pos_settings[0] + btn_leave.get_width() and pos_settings[1] < mousse_y < pos_settings[
        1] + btn_settings.get_height():
        if not len(SETTINGS_ANIMATION) - 1 == settings_frame % len(SETTINGS_ANIMATION):
            settings_frame = Switch_frame(100, settings_frame)
        btn_settings = SETTINGS_ANIMATION[settings_frame % len(SETTINGS_ANIMATION)]
        btn_settings = pygame.transform.scale(btn_settings, (96, 144)).convert_alpha()
    elif not btn_settings == pygame.transform.scale(SETTINGS_ANIMATION[0], (96, 144)).convert_alpha():
        settings_frame = 0
        btn_settings = SETTINGS_ANIMATION[0]
        btn_settings = pygame.transform.scale(btn_settings, (96, 144)).convert_alpha()


# Animation du joueur
def player_animation():
    global player
    global player_frame
    if is_runing:
        player_run_time = 50
    else:
        player_run_time = 100

    if is_dialogue:
        player_frame = Switch_frame(300, player_frame)
        player = IDLE[player_frame % len(IDLE)]
        player = pygame.transform.scale(player, (SIZE, SIZE)).convert_alpha()
    elif vx > 0:
        player_frame = Switch_frame(player_run_time, player_frame)
        player = WALK_RIGHT[player_frame % len(WALK_RIGHT)]
        player = pygame.transform.scale(player, (SIZE, SIZE)).convert_alpha()
    elif vx < 0:
        player_frame = Switch_frame(player_run_time, player_frame)
        player = WALK_LEFT[player_frame % len(WALK_LEFT)]
        player = pygame.transform.scale(player, (SIZE, SIZE)).convert_alpha()
    elif vy > 0:
        player_frame = Switch_frame(player_run_time, player_frame)
        player = WALK_DOWN[player_frame % len(WALK_DOWN)]
        player = pygame.transform.scale(player, (SIZE, SIZE)).convert_alpha()
    elif vy < 0:
        player_frame = Switch_frame(player_run_time, player_frame)
        player = WALK_UP[player_frame % len(WALK_UP)]
        player = pygame.transform.scale(player, (SIZE, SIZE)).convert_alpha()
    else:
        player_frame = Switch_frame(300, player_frame)
        player = IDLE[player_frame % len(IDLE)]
        player = pygame.transform.scale(player, (SIZE, SIZE)).convert_alpha()



################### SET BLOCK ###################



#Change l'image du fond d'une block
def under_block(pos_block_x, pos_block_y, x_map, y_map):
    id_list = [1,2,3,7,11]
    is_detected = int
    for id in id_list:
        if LEVELS[y_map][x_map + 1] == id:
            is_detected = id
            break
        elif LEVELS[y_map][x_map - 1] == id:
            is_detected = id
            break
        elif LEVELS[y_map + 1][x_map] == id:
            is_detected = id
            break
        elif LEVELS[y_map - 1][x_map] == id:
            is_detected = id
            break
    if is_detected == 1:
        screen.blit(GRASS, (pos_block_x, pos_block_y))
    elif is_detected == 2:
        screen.blit(SAND, (pos_block_x, pos_block_y))
    elif is_detected == 3:
        screen.blit(SNOW, (pos_block_x, pos_block_y))
    elif is_detected == 7:
        screen.blit(WATTER, (pos_block_x, pos_block_y))
    elif is_detected == 11:
        screen.blit(FLOOR, (pos_block_x, pos_block_y))
    else:
        screen.blit(GRASS, (pos_block_x, pos_block_y))


# Affiche tout les blocks
def init_map():
    for y_map, ligne in enumerate(LEVELS):
        for x_map, case in enumerate(ligne):
            pos_block_x = x_map * SIZE - camera_x
            pos_block_y = y_map * SIZE - camera_y
            if type(case) == list:
                if case[0] == 0:
                    screen.blit(ARROW, (pos_block_x, pos_block_y))
                else :
                    screen.blit(pygame.transform.flip(ARROW, True, False), (pos_block_x, pos_block_y))

            if case == 1:
            # id de l'herbe
                screen.blit(GRASS, (pos_block_x, pos_block_y))
            if case == 2:
            # id du sable
                screen.blit(SAND, (pos_block_x, pos_block_y))
            if case == 3:
            # id de la neige
                screen.blit(SNOW, (pos_block_x, pos_block_y))
            if case == 4:
            # id de le chemin
            ############ AVENUE ############
                if LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map - 1][
                    x_map] == 4 and LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map - 1][x_map - 1] == 4 and LEVELS[y_map + 1][x_map + 1] == 4 and LEVELS[y_map - 1][
                    x_map + 1] == 4 and LEVELS[y_map + 1][x_map - 1] == 4:
                    screen.blit(ROAD_SOIL[4], (pos_block_x, pos_block_y))
                else:
                    under_block(pos_block_x, pos_block_y, x_map, y_map)
                    # Croisement de 4 chemin


                    ############ CHEMIN SIMPLE ############
                    # coin en haut a droit
                    if LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map + 1][x_map + 1] == 4 and LEVELS[y_map - 1][x_map - 1] == 4 and LEVELS[y_map + 1][x_map - 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[7], 270), (pos_block_x, pos_block_y))

                    #coin en bas a gauche
                    elif  LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map + 1][x_map + 1] == 4 and LEVELS[y_map - 1][x_map - 1] == 4 and LEVELS[y_map - 1][x_map + 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[7], 90), (pos_block_x, pos_block_y))

                    # coin en haut a gauche
                    elif  LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map + 1][x_map + 1] == 4 and LEVELS[y_map + 1][x_map - 1] == 4 and LEVELS[y_map - 1][x_map + 1] == 4:
                        screen.blit(ROAD_SOIL[7], (pos_block_x, pos_block_y))

                    # coin avenue en bas a droite
                    elif LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map - 1][x_map + 1] == 4 and LEVELS[y_map - 1][x_map - 1] == 4 and LEVELS[y_map + 1][x_map - 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[7], 180), (pos_block_x, pos_block_y))

                    # croisement simple avenue route
                        #haut
                    elif LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map][
                        x_map - 1] == 4 and LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map + 1][x_map + 1] == 4 and LEVELS[y_map + 1][x_map - 1] == 4:
                        screen.blit(ROAD_SOIL[8], (pos_block_x, pos_block_y))

                        #bas
                    elif LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map][
                        x_map - 1] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map - 1][x_map + 1] == 4 and LEVELS[y_map - 1][x_map - 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[8], 180), (pos_block_x, pos_block_y))

                        # gauche
                    elif LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map - 1][
                        x_map] == 4 and LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map - 1][
                             x_map + 1] == 4 and LEVELS[y_map + 1][x_map + 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[8], 90), (pos_block_x, pos_block_y))

                        #droite
                    elif LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map - 1][
                        x_map] == 4 and LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map - 1][
                             x_map - 1] == 4 and LEVELS[y_map + 1][x_map - 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[8], 270), (pos_block_x, pos_block_y))



                    # bord de avenue haut
                    elif LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map + 1][
                        x_map] == 4 and LEVELS[y_map + 1][x_map + 1] == 4 and LEVELS[y_map + 1][x_map - 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[5], 270), (pos_block_x, pos_block_y))

                    # bord de avenue bas
                    elif LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map - 1][
                        x_map] == 4 and LEVELS[y_map - 1][x_map + 1] == 4 and LEVELS[y_map - 1][x_map - 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[5], 90), (pos_block_x, pos_block_y))

                    # bord de avenue gauche
                    elif LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map][
                        x_map + 1] == 4 and LEVELS[y_map + 1][x_map + 1] == 4 and LEVELS[y_map - 1][x_map + 1] == 4:
                        screen.blit(ROAD_SOIL[5], (pos_block_x, pos_block_y))

                    # bord de avenue coté droit
                    elif LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map][
                        x_map - 1] == 4 and LEVELS[y_map + 1][x_map - 1] == 4 and LEVELS[y_map - 1][x_map - 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[5], 180), (pos_block_x, pos_block_y))

                    elif LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map + 1][
                        x_map + 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[6], 270), (pos_block_x, pos_block_y))

                    elif LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map - 1][
                        x_map - 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[6], 90), (pos_block_x, pos_block_y))

                    elif LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map + 1][x_map] == 4 and LEVELS[y_map + 1][
                        x_map - 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[6], 180), (pos_block_x, pos_block_y))

                    elif LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map - 1][
                        x_map + 1] == 4:
                        screen.blit(ROAD_SOIL[6], (pos_block_x, pos_block_y))

                    elif LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map + 1][x_map] == 4:
                        screen.blit(ROAD_SOIL[1], (pos_block_x, pos_block_y))

                    # Croisement de 3 chemin
                    elif LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map - 1][x_map] == 4 :
                        screen.blit(ROAD_SOIL[2], (pos_block_x, pos_block_y))
                    elif LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map + 1][x_map] == 4 :
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[2], 180), (pos_block_x, pos_block_y))
                    elif LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map + 1][x_map] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[2], 270), (pos_block_x, pos_block_y))
                    elif LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map - 1][x_map] == 4 and LEVELS[y_map + 1][x_map] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[2], 90), (pos_block_x, pos_block_y))

                        # Croisement de 2 chemin
                    elif LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map - 1][x_map] == 4:
                        screen.blit(ROAD_SOIL[3], (pos_block_x, pos_block_y))
                    elif LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map - 1][x_map] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[3], 90), (pos_block_x, pos_block_y))
                    elif LEVELS[y_map][x_map - 1] == 4 and LEVELS[y_map + 1][x_map] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[3], 180), (pos_block_x, pos_block_y))
                    elif LEVELS[y_map][x_map + 1] == 4 and LEVELS[y_map + 1][x_map] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[3], 270), (pos_block_x, pos_block_y))

                        #Pas de croisement
                    elif LEVELS[y_map][x_map - 1] == 4 or LEVELS[y_map][x_map + 1] == 4:
                        screen.blit(pygame.transform.rotate(ROAD_SOIL[0], 90), (pos_block_x, pos_block_y))
                    else:
                        screen.blit(ROAD_SOIL[0], (pos_block_x, pos_block_y))
            if case == 4.3:
                screen.blit(ROAD_TOWN, (pos_block_x, pos_block_y))

            if case == 5:
            # id de le rocher
                under_block(pos_block_x, pos_block_y, x_map, y_map)
                screen.blit(ROCK, (pos_block_x, pos_block_y))
            if case == 6:
            # id de la falaise
                screen.blit(WATTER, (pos_block_x, pos_block_y))
            if case == 7:
            # id de l'eau
                screen.blit(WATTER, (pos_block_x, pos_block_y))
            if case == 8:
            # id de l'abre
                under_block(pos_block_x, pos_block_y, x_map, y_map)
                if LEVELS[y_map - 1][x_map] == 8 and not LEVELS[y_map + 1][x_map] == 8:
                    screen.blit(TREE[1], (pos_block_x, pos_block_y))
                else:
                    screen.blit(TREE[0], (pos_block_x, pos_block_y))
            if case == 9:
            # id des murs
                screen.blit(WALL, (pos_block_x, pos_block_y))
            if case == 10:
            # id des toits
                if LEVELS[y_map][x_map - 1] == 10 and LEVELS[y_map][x_map + 1] == 10:
                    screen.blit(ROOF[0], (pos_block_x, pos_block_y))


                elif LEVELS[y_map][x_map - 1] == 10:
                    under_block(pos_block_x, pos_block_y, x_map, y_map)
                    screen.blit(ROOF[2], (pos_block_x, pos_block_y))

                elif LEVELS[y_map][x_map + 1] == 10:
                    under_block(pos_block_x, pos_block_y, x_map, y_map)
                    screen.blit(ROOF[1], (pos_block_x, pos_block_y))

                else:
                    under_block(pos_block_x, pos_block_y, x_map, y_map)
                    screen.blit(ROOF[3], (pos_block_x, pos_block_y))
            if case == 11:
                screen.blit(FLOOR, (pos_block_x, pos_block_y))
            if case == 12:
                screen.blit(STAIR, (pos_block_x, pos_block_y))
            if case == 14:
                under_block(pos_block_x, pos_block_y, x_map, y_map)
                if LEVELS[y_map][x_map + 1] == 14:
                    screen.blit(CARPET, (pos_block_x, pos_block_y))
                else :
                    screen.blit(pygame.transform.flip(CARPET, True, False), (pos_block_x, pos_block_y))
            if case == 15:
                under_block(pos_block_x, pos_block_y, x_map, y_map)
                screen.blit(CHAIR, (pos_block_x, pos_block_y))
            if case == 16:
                under_block(pos_block_x, pos_block_y, x_map, y_map)
                screen.blit(FLOWER_POT, (pos_block_x, pos_block_y))
            if case == 17:
                under_block(pos_block_x, pos_block_y, x_map, y_map)
                if LEVELS[y_map][x_map + 1] == 17 and not LEVELS[y_map][x_map - 1] == 17:
                    screen.blit(DESK[0], (pos_block_x, pos_block_y))
                elif not LEVELS[y_map][x_map + 1] == 17 and LEVELS[y_map][x_map - 1] == 17:
                    screen.blit(DESK[2], (pos_block_x, pos_block_y))
                else:
                    screen.blit(DESK[1], (pos_block_x, pos_block_y))




################### COLLISION ###################

# Position du Joueur sur la map
def pos_map():
    x_map = x // SIZE
    y_map = y // SIZE
    return x_map, y_map

# Donne la listes des block autoure
def get_neighbour_blocks(x_map_start, y_map_start):
    blocks = list()
    for y_map in range(y_map_start, y_map_start + 2):
        for x_map in range(x_map_start, x_map_start + 2):
            try:
                if type(LEVELS[y_map][x_map]) is list or type(LEVELS[y_map][x_map]) is tuple or (LEVELS[y_map][x_map] == 5 or LEVELS[y_map][x_map] == 6 or LEVELS[y_map][x_map] == 7 or LEVELS[y_map][x_map] == 8 or LEVELS[y_map][x_map] == 9 or LEVELS[y_map][x_map] == 10 or LEVELS[y_map][x_map] == 13 or LEVELS[y_map][x_map] == 16 or LEVELS[y_map][x_map] == 17):
                    topleft = x_map * SIZE, y_map * SIZE
                    blocks.append(pygame.Rect((topleft), (SIZE, SIZE)))
            except IndexError:
                print('Erreur, Petit Tricheur')
    return blocks

# RENVOI A L'ANCIENNE COLLISION
def bloque_collision(old_pos, new_pos, vx, vy):
    old_rect = pygame.Rect(old_pos, (SIZE - 20, SIZE))
    new_rect = pygame.Rect(new_pos, (SIZE - 20, SIZE))
    x_map, y_map = pos_map()
    col_later = list()
    blocks = get_neighbour_blocks(x_map, y_map)
    for block in blocks:
        if not new_rect.colliderect(block):
            continue
        dx_correction, dy_correction = compute_prenetration(block, old_rect, new_rect)
        # Dans cette première phase, on n'ajuste que les pénétrations sur un
        # seul axe.
        if dx_correction == 0.0:
            new_rect.top += dy_correction
            vy = 0.0
        elif dy_correction == 0.0:
            new_rect.left += dx_correction
            vx = 0.0
        else:
            col_later.append(block)

        # Deuxième phase. On teste à présent les distances de pénétrations pour
        # les blocks qui en possédaient sur les 2 axes.
    for block in col_later:
        dx_correction, dy_correction = compute_prenetration(block, old_rect, new_rect)
        if dx_correction == dy_correction == 0.0:
            # Finalement plus de pénétration. Le new_rect a bougé précédemment
            # lors d'une résolution de collision
            continue
        if abs(dx_correction) < abs(dy_correction):
            # Faire la correction que sur l'axe X (plus bas)
            dy_correction = 0.0
        elif abs(dy_correction) < abs(dx_correction):
            # Faire la correction que sur l'axe Y (plus bas)
            dx_correction = 0.0
        if dy_correction != 0.0:
            new_rect.top += dy_correction
            vy = 0.0
        elif dx_correction != 0.0:
            new_rect.left += dx_correction
            vx = 0.0

    x, y = new_rect.topleft
    return x, y, vx, vy


#CALCULE LA DISTANCE PARCOURUT DANS LE BLOCK
def compute_prenetration(block, old_rect, new_rect):
    dx_correction = dy_correction = 0.0
    if old_rect.bottom <= block.top < new_rect.bottom:
        dy_correction = block.top - new_rect.bottom
    elif old_rect.top >= block.bottom > new_rect.top:
        dy_correction = block.bottom - new_rect.top
    if old_rect.right <= block.left < new_rect.right:
        dx_correction = block.left - new_rect.right
    elif old_rect.left >= block.right > new_rect.left:
        dx_correction = block.right - new_rect.left
    return dx_correction, dy_correction



################### PLAYER ACTION ###################
def set_pnj():
    global all_pages
    for pnj in PNJS:
            screen.blit(player, (pnj[0] * SIZE - camera_x, pnj[1] * SIZE - camera_y))
            if range_calculator((x,y), (pnj[0],pnj[1])):
                pnj[3] = True
                all_pages = pnj[2].split('ENDPAGE')
                for quest in quests:
                    if pnj[0] == 1 and pnj[1] == 2 and quest[0] == 1.00:
                        quest[1] = True
                        all_pages = "Si tu vois mon amis qui se nome GérondarENDPAGEOffre lui ca de ma part".split('ENDPAGE')
                    if pnj[0] == 10 and pnj[1] == 15 and quest[0] == 1.01:
                        if check_item('Letter', 2):
                            all_pages = "Merci, Tiens en guise de remerciment".split('ENDPAGE')
                            quest[1] = True
                        else:
                            all_pages = "Salut je suis Gérondar\nMon amis t'as donner un truc pour moi, dommage il a du en perdre au sudENDPAGEVas la chercher s'il te plait".split('ENDPAGE')

                dialogue(all_pages, 1)
                break
            else:
                pnj[3] = False

# TP LE JOUEUR A DES COORDONNE
def tp(pos_x, pos_y):
    global x
    global y
    global camera_x
    global camera_y
    global old_x
    global old_y
    global old_pos
    camera_x = pos_x - (cam_size_x //2)
    camera_y = pos_y - (cam_size_y // 2)

    x = pos_x * SIZE
    y = pos_y * SIZE

    old_x = x
    old_y = y
    old_pos = (old_x, old_y)


    print(x, ' ',y)


# CALCULE SI 2  ENTITE SON A LA MEME DISTANCE
def range_calculator(a, b):
    if (b[0] * SIZE - 16 < a[0] < b[0] * SIZE + SIZE + 16 and b[1] * SIZE - 16 < a[1] < b[1] * SIZE + SIZE + 16) or (b[0] * SIZE - 16 < a[0] + SIZE < b[0] * SIZE + SIZE + 16 and b[1] * SIZE - 16 < a[1] + SIZE < b[1] * SIZE + SIZE + 16):
        return True
    else:
        return False


# AFFICHAGE DU DIALOGUE
def dialogue(all_pages, parameter):
    global is_dialogue
    if not is_dialogue:
        return
    police = pygame.font.Font(None, 40)
    image = pygame.transform.scale(pygame.image.load("asset/dialogue.png"), (SIZE * 16, 2 * SIZE)).convert_alpha()
    rect = image.get_rect()
    rect.x = (cam_size_x - rect.width)/2
    rect.y = cam_size_y - rect.height
    final_lines = []
    requested_lines = all_pages[id_page].splitlines()
    accumulated_height = 0

    for line in requested_lines:
        if police.size(line)[0] > rect.width:
            words = line.split(' ')
            for word in words:
                if police.size(word)[0] >= rect.width:
                    print('Le mot ', word, ' est trop long pour etre afficher')
            accumulated_line = ''
            for word in words:
                test_line = accumulated_line + word + ' '
                if police.size(test_line)[0] >= rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + ' '
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_lines)
    for line in final_lines[0]:
        if accumulated_height + police.size(line)[1] >= rect.height:
            print('Un mots est trop haut pour etre afficher dans le texte')
        if line != "":
            affichage = police.render(line, 1, (0, 0, 0))
        if parameter == 0:
            image.blit(affichage, (0, accumulated_height))
        elif parameter == 1:
            image.blit(affichage, ((rect.width// 2) - (police.size(line)[0] // 2), accumulated_height))
        elif parameter == 2:
            image.blit(affichage, (rect.width - police.size(line)[0], accumulated_height))
        else:
            print('Le parametre du text est invalide')
        accumulated_height += police.size(line)[1]
    screen.blit(image, rect)
    return


def take_dor():
    global all_pages
    try:
        if type(LEVELS[y_map][x_map]) == list:
            print(len(LEVELS[y_map][x_map]))
            if check_item(LEVELS[y_map][x_map][2], 1):
                print('Petit prenneur de porte')
                tp(LEVELS[y_map][x_map][1][0], LEVELS[y_map][x_map][1][1])
            else:
                all_pages = "Il te manque une clef".split(
                    'ENDPAGE')
                dialogue(all_pages, 1)
        elif type(LEVELS[y_map][x_map]) == tuple:
            tp(LEVELS[y_map][x_map][1][0], LEVELS[y_map][x_map][1][1])
    except IndexError:
        print("Tricheur")






###################################### VARIABLE ######################################

################### SYSTEME ###################

SIZE = 64

is_dialogue = False

is_paused = True

all_pages = list()

money = 0

inventory = []

in_inventory = False

CLOCK = pygame.time.Clock()

# boucle du jeu
running = True

################### ASSET BLOCK ###################

ROCK = pygame.transform.scale(pygame.image.load('asset/tiles/Rock.png'), (SIZE, SIZE)).convert_alpha()

TREE = [
    pygame.transform.scale(pygame.image.load('asset/tiles/tree/simple/Tree.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/tree/simple/Tree2.png'), (SIZE, SIZE)).convert_alpha()
]

GRASS = pygame.transform.scale(pygame.image.load('asset/tiles/Grass.png'), (SIZE, SIZE)).convert()

WALL = pygame.transform.scale(pygame.image.load('asset/tiles/wall/Wall.png'), (SIZE, SIZE)).convert()

WATTER = pygame.transform.scale(pygame.image.load('asset/tiles/Water.png'), (SIZE, SIZE)).convert()

SAND = pygame.transform.scale(pygame.image.load('asset/tiles/Sand.png'), (SIZE, SIZE)).convert()

ROAD_SOIL = [
    pygame.transform.scale(pygame.image.load('asset/tiles/road/soil/0.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/road/soil/1.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/road/soil/2.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/road/soil/3.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/road/soil/4.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/road/soil/5.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/road/soil/6.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/road/soil/7.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/road/soil/8.png'), (SIZE, SIZE)).convert_alpha()
]

ROAD_TOWN = pygame.transform.scale(pygame.image.load('asset/tiles/road/town/0.png'), (SIZE, SIZE)).convert_alpha()

SNOW = pygame.transform.scale(pygame.image.load('asset/tiles/Snow.png'), (SIZE, SIZE)).convert()

ROOF = [
    pygame.transform.scale(pygame.image.load('asset/tiles/roof/red/Roof.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/roof/red/Roof1.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/roof/red/Roof2.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/roof/red/Roof3.png'), (SIZE, SIZE)).convert_alpha()
]

FLOOR = pygame.transform.scale(pygame.image.load('asset/tiles/indoor/floor.png'), (SIZE, SIZE)).convert()

STAIR = pygame.transform.scale(pygame.image.load('asset/tiles/indoor/stair.png'), (SIZE, SIZE)).convert()

CHAIR = pygame.transform.scale(pygame.image.load('asset/tiles/indoor/chair.png'), (SIZE, SIZE)).convert_alpha()

CARPET = pygame.transform.scale(pygame.image.load('asset/tiles/indoor/carpet.png'), (SIZE, SIZE)).convert_alpha()

ARROW = pygame.transform.scale(pygame.image.load('asset/tiles/indoor/arrow.png'), (SIZE, SIZE)).convert_alpha()

FLOWER_POT = pygame.transform.scale(pygame.image.load('asset/tiles/indoor/flower_pot.png'), (SIZE, SIZE)).convert_alpha()

DESK = [
    pygame.transform.scale(pygame.image.load('asset/tiles/indoor/desk/0.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/indoor/desk/1.png'), (SIZE, SIZE)).convert_alpha(),
    pygame.transform.scale(pygame.image.load('asset/tiles/indoor/desk/2.png'), (SIZE, SIZE)).convert_alpha()
]


################### ANIMATION ###################
Frame_rate = 100
current_time = 0

SETTINGS_ANIMATION = [
    pygame.image.load('asset/animation/menu/Settings/0.png'), pygame.image.load('asset/animation/menu/Settings/1.png'), pygame.image.load('asset/animation/menu/Settings/2.png'), pygame.image.load('asset/animation/menu/Settings/3.png'), pygame.image.load('asset/animation/menu/Settings/4.png'), pygame.image.load('asset/animation/menu/Settings/5.png'), pygame.image.load('asset/animation/menu/Settings/6.png'), pygame.image.load('asset/animation/menu/Settings/7.png'), pygame.image.load('asset/animation/menu/Settings/8.png'), pygame.image.load('asset/animation/menu/Settings/9.png'), pygame.image.load('asset/animation/menu/Settings/10.png'), pygame.image.load('asset/animation/menu/Settings/11.png'), pygame.image.load('asset/animation/menu/Settings/12.png')
]
PLAY_ANIMATION = [
    pygame.image.load('asset/animation/menu/Button2/0.png'), pygame.image.load('asset/animation/menu/Button2/1.png'), pygame.image.load('asset/animation/menu/Button2/2.png'), pygame.image.load('asset/animation/menu/Button2/3.png'), pygame.image.load('asset/animation/menu/Button2/4.png'), pygame.image.load('asset/animation/menu/Button2/5.png'), pygame.image.load('asset/animation/menu/Button2/6.png')
]
LEAVE_ANIMATION = [
    pygame.image.load('asset/animation/menu/Button1/0.png'), pygame.image.load('asset/animation/menu/Button1/1.png'), pygame.image.load('asset/animation/menu/Button1/2.png'), pygame.image.load('asset/animation/menu/Button1/3.png'), pygame.image.load('asset/animation/menu/Button1/4.png'), pygame.image.load('asset/animation/menu/Button1/5.png')
]

WALK_UP = [
pygame.image.load('asset/animation/sprites/player/Walk/up/0.png'), pygame.image.load('asset/animation/sprites/player/Walk/up/1-3.png'), pygame.image.load('asset/animation/sprites/player/Walk/up/2.png'), pygame.image.load('asset/animation/sprites/player/Walk/up/1-3.png')
]
WALK_DOWN = [
pygame.image.load('asset/animation/sprites/player/Walk/down/0.png'), pygame.image.load('asset/animation/sprites/player/Walk/down/1-3.png'), pygame.image.load('asset/animation/sprites/player/Walk/down/2.png'), pygame.image.load('asset/animation/sprites/player/Walk/down/1-3.png')
]
WALK_RIGHT = [
pygame.image.load('asset/animation/sprites/player/Walk/right/0.png'), pygame.image.load('asset/animation/sprites/player/Walk/right/1-3.png'), pygame.image.load('asset/animation/sprites/player/Walk/right/2.png'), pygame.image.load('asset/animation/sprites/player/Walk/right/1-3.png')
]
WALK_LEFT = [
pygame.image.load('asset/animation/sprites/player/Walk/left/0.png'), pygame.image.load('asset/animation/sprites/player/Walk/left/1-3.png'), pygame.image.load('asset/animation/sprites/player/Walk/left/2.png'), pygame.image.load('asset/animation/sprites/player/Walk/left/1-3.png')
]
IDLE = [
    pygame.image.load('asset/animation/sprites/player/idle/0.png'),pygame.image.load('asset/animation/sprites/player/idle/1.png')
]

BAG_INVENTORY = [
    pygame.image.load('asset/animation/inventory/0.png'), pygame.image.load('asset/animation/inventory/1.png'), pygame.image.load('asset/animation/inventory/2.png'), pygame.image.load('asset/animation/inventory/3.png'), pygame.image.load('asset/animation/inventory/4.png')
]

bag_inventory_frame = 0

leave_frame = 0

play_frame = 0

settings_frame = 0

player_frame = 0

################### ENTITY ###################

player = pygame.transform.scale(pygame.image.load('asset/animation/sprites/player/idle/0.png'), (SIZE, SIZE)).convert_alpha()

btn_settings = pygame.transform.scale(pygame.image.load('asset/animation/menu/Settings/0.png'), (96, 144)).convert_alpha()

btn_play = pygame.transform.scale(pygame.image.load('asset/animation/menu/Button2/0.png'), (576, 240)).convert_alpha()

btn_leave = pygame.transform.scale(pygame.image.load('asset/animation/menu/Button1/0.png'), (576, 240)).convert_alpha()

bag_image = pygame.transform.scale(pygame.image.load('asset/animation/inventory/0.png'), (800, 800)).convert_alpha()

PNJS = [
    [1, 2,
     "Appui sur les FLECHES DIRECTIONELLES pour te deplacer,\nTu peux passer se message en appuyant sur Z!ENDPAGETu peux aussi courrir en appuyant sur SHIFT.", False],
    [10, 15,
     "Appui sur les FLECHES DIRECTIONELLES pour te deplacer,\nTu peux passer se message en appuyant sur Z!ENDPAGETu peux aussi courrir en appuyant sur SHIFT.", False]
]

################### ITEM ###################

ORION = pygame.transform.scale(pygame.image.load('asset/item/Orion.png'), (SIZE // 2, SIZE // 2)).convert_alpha()

LETTER = pygame.transform.scale(pygame.image.load('asset/item/letter.png'), (SIZE // 2, SIZE // 2)).convert_alpha()

KEY = pygame.transform.scale(pygame.image.load('asset/item/key.png'), (SIZE // 2, SIZE // 2)).convert_alpha()

WEED = pygame.transform.scale(pygame.image.load('asset/item/weed.png'), (SIZE // 2, SIZE // 2)).convert_alpha()

SPLIFF = pygame.transform.scale(pygame.image.load('asset/item/spliff.png'), (SIZE // 2, SIZE // 2)).convert_alpha()

POUCH = pygame.transform.scale(pygame.image.load('asset/item/pouch.png'), (SIZE // 2, SIZE // 2)).convert_alpha()


items = [
    [10, 17, 'Orion', False],
    [10, 19, 'Pokeball', False],
    [22, 48, 'Letter', False],
    [23, 48, 'Light', False],
    [24, 48, 'Bird', False],
    [22, 47, 'Chicken', False],
    [22, 49, 'Tacos', False],
    [20, 48, 'Food', False],
    [21, 48, 'Poop', False],
    #[1, 2, 'Spliff', False],
    #[2, 2, 'Weed', False],
    #[3, 3, 'Pouch', False],

]


id_page = 0

LEVELS = [
    [12, 11, 11, 11, 11, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [11, 11, 15, 11, 11, 11, 7, 7, 7, 7, 7, 7, 7, 2, 1, 5, 1, 1, 5, 1, 1, 2, 7, 7, 2, 2, 1, 1, 1, 1, 8, 1, 1, 1, 3, 3, 3, 3,3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
    [11, 17, 17, 17, 11, 11, 7, 7, 7, 7, 7, 7, 7, 5, 1, 1, 5, 1, 1, 1, 1, 2, 7, 7, 7, 2, 5, 8, 1, 1, 8, 1, 8, 1, 3, 3, 3, 3,3, 3, 3, 3, 3, 3, 3, 8, 3, 3, 3, 3, 0],
    [11, 11, 11, 11, 11, 11, 7, 7, 7, 7, 7, 7, 7, 2, 5, 1, 1, 1, 1, 5, 2, 2, 7, 7, 7, 1, 1, 8, 1, 1, 1, 1, 8, 1, 3, 5, 3, 3,3, 4, 4, 4, 4, 3, 8, 3, 3, 8, 3, 8, 8, 0],
    [11, 11, 14, 14, 11, 11, 7, 5, 7, 7, 7, 7, 2, 4, 1, 1, 1, 1, 1, 8, 2, 7, 7, 7, 7, 8, 1, 1, 8, 1, 8, 1, 1, 1, 3, 5, 3, 3,4, 3, 3, 3, 3, 8, 3, 3, 8, 3, 3, 8, 0],
    [0, 7, (0,(2, 4)), (0,(2, 4)), 7, 5, 7, 7, 7, 7, 7, 7, 2, 4, 1, 5, 10, 1, 1, 1, 2, 7, 7, 7, 7, 1, 1, 1, 1, 1, 8, 8, 1, 1, 3, 3, 3, 3,4, 3, 3, 3, 3, 3, 3, 3, 8, 3, 8, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 5, 5, 7, 7, 4, 1, 10, 10, 10, 1, 1, 2, 7, 7, 7, 7, 2, 8, 1, 8, 1, 1, 8, 1, 1, 3, 3, 3,5, 4, 3, 3, 5, 3, 3, 3, 3, 8, 3, 8, 3, 0],
    [0, 7, 7, 7, 7, 7, 5, 7, 5, 7, 7, 7, 7, 4, 1, 9, 9, 9, 8, 1, 2, 7, 7, 7, 2, 2, 8, 1, 8, 1, 1, 1, 10, 1, 3, 5, 3, 3,4, 8, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
    [0, 7, 1, 8, 7, 7, 5, 7, 5, 7, 7, 2, 2, 4, 1, 9, (1,(2, 4)), 9, 8, 1, 2, 2, 7, 7, 7, 2, 1, 1, 1, 1, 1, 10, 10, 10,3, 3, 3, 3, 4, 8, 3, 3, 3, 3, 3, 3, 3, 3, 3, 8, 0],
    [0, 7, 1, 8, 7, 7, 5, 7, 7, 7, 7, 2, 2, 4, 1, 1, 4, 1, 1, 1, 1, 2, 7, 7, 2, 8, 1, 5, 10, 1, 1, 9, 9, 9, 3, 3, 3, 5,4, 3, 8, 3, 3, 3, 10, 3, 3, 8, 3, 8, 0],
    [0, 7, 1, 10, 1, 7, 7, 7, 7, 7, 7, 2, 2, 4, 4, 4, 4, 1, 1, 1, 1, 2, 7, 7, 2, 8, 1, 10, 10, 10, 1, 9, (1,(2, 4)), 9,3, 3, 5, 5, 4, 3, 8, 3, 3, 10, 10, 10, 3, 8, 3, 3, 0],
    [0, 7, 10, 10, 10, 1, 7, 7, 7, 7, 7, 2, 2, 1, 1, 1, 4, 1, 1, 1, 1, 2, 7, 7, 2, 1, 1, 9, 9, 9, 1, 1, 4, 1, 5, 3, 3,3, 4, 3, 3, 3, 3, 9, 9, 9, 3, 3, 3, 3, 0],
    [0, 7, 9, 9, 9, 1, 7, 7, 7, 8, 7, 7, 7, 2, 1, 1, 4, 1, 1, 10, 1, 1, 1, 7, 1, 1, 1, 9, (1,(2, 4)), 9, 1, 1, 4, 1, 3,3, 3, 3, 4, 8, 3, 3, 3, 9, (1,(2, 4)), 9, 3, 3, 3, 3, 0],
    [0, 7, 9, (1,(2, 4)), 9, 1, 7, 7, 1, 8, 7, 7, 7, 2, 1, 1, 4, 1, 10, 10, 10, 1, 1, 7, 1, 5, 1, 1, 4, 1, 1, 1, 4, 1,3, 3, 3, 3, 4, 8, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 0],
    [0, 7, 1, 4, 1, 7, 7, 7, 1, 7, 7, 7, 7, 2, 1, 1, 4, 1, 9, 9, 9, 1, 1, 7, 1, 5, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,4, 3, 3, 3, 3, 3, 4, 3, 3, 10, 3, 3, 0],
    [0, 7, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 4, 1, 9, (1,(2, 4)), 9, 1, 1, 7, 1, 1, 5, 1, 4, 1, 1, 1, 1, 1, 3, 3,3, 3, 3, 3, 3, 5, 3, 3, 4, 3, 10, 10, 10, 3, 0],
    [0, 7, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 7, 1, 1, 1, 1, 4, 1, 1, 10, 1, 1, 3, 7, 2, 3, 3,3, 3, 5, 3, 3, 4, 3, 9, 9, 9, 3, 0],
    [0, 7, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 7, 1, 1, 1, 1, 4, 1, 10, 10, 10, 8, 2, 7, 2,3, 5, 5, 3, 3, 3, 3, 4, 3, 9, (1,(2, 4)), 9, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 4, 4, 4, 7, 7, 7, 7, 7, 1, 4, 4, 1, 7, 7, 7, 1, 10, 1, 1, 4, 1, 9, 9, 9, 8, 2, 7, 2, 3,3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 3, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 4, 4, 4, 7, 7, 7, 7, 7, 2, 4, 4, 1, 7, 7, 7, 10, 10, 10, 1, 4, 1, 9, (1,(2, 4)), 9, 1, 3,7,2, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 4, 7, 7, 2, 2, 2, 7, 2, 5, 4, 1, 7, 2, 2, 9, 9, 9, 1, 4, 1, 1, 4, 1, 1, 8, 7, 2,5, 3, 3, 7, 3, 3, 4, 3, 3, 3, 3, 3, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 4, 7, 7, 8, 2, 2, 7, 5, 1, 4, 1, 7, 2, 1, 9, (1,(2, 4)), 9, 1, 4, 1, 1, 4, 8, 1, 8, 7,3,5, 3, 2, 7, 2, 2, 4, 3, 2, 2, 3, 3, 5, 0],
    [0, 7, 5, 5, 5, 5, 5, 7, 7, 7, 4, 7, 7, 8, 1, 8, 7, 1, 1, 4, 1, 7, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 7, 3,3, 3, 2, 7, 2, 2, 4, 3, 7, 2, 3, 3, 5, 0],
    [0, 7, 5, 7, 7, 7, 7, 7, 7, 7, 4, 7, 7, 2, 1, 8, 7, 1, 1, 4, 1, 7, 5, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 3, 7, 3,3, 3, 2, 7, 7, 7, 4, 7, 7, 2, 3, 2, 3, 0],
    [0, 7, 5, 7, 7, 7, 5, 7, 7, 7, 1, 7, 7, 2, 1, 2, 7, 7, 7, 4, 7, 7, 1, 1, 5, 1, 1, 1, 4, 1, 1, 1, 1, 1, 3, 7, 3,5, 5, 2, 7, 7, 7, 4, 7, 7, 7, 7, 7, 3, 0],
    [0, 7, 7, 7, 7, 5, 7, 7, 7, 7, 1, 7, 7, 5, 1, 2, 7, 7, 7, 4, 7, 7, 1, 5, 1, 1, 5, 1, 4, 4, 4, 4, 4, 4, 4, 7, 3,3, 3, 3, 7, 3, 3, 4, 2, 7, 7, 7, 7, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 7, 7, 2, 8, 2, 7, 2, 2, 4, 2, 7, 1, 1, 1, 1, 5, 1, 4, 1, 1, 1, 1, 1, 4, 7, 3,3, 3, 3, 7, 3, 3, 4, 2, 7, 7, 7, 7, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 2, 7, 7, 7, 2, 8, 2, 7, 2, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 4, 7, 7,7, 7, 3, 7, 3, 3, 4, 3, 3, 2, 7, 2, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 2, 7, 7, 1, 4, 1, 7, 1, 1, 1, 1, 1, 1, 4, 1, 1, 10, 1, 1, 4, 7, 7,7, 7, 7, 7, 5, 3, 4, 3, 3, 2, 7, 2, 3, 0],
    [0, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 1, 2, 7, 7, 1, 4, 1, 7, 1, 1, 1, 1, 5, 1, 4, 1, 10, 10, 10, 1, 4, 3,2, 2, 7, 7, 7, 5, 3, 4, 8, 3, 2, 7, 2, 3, 0],
    [0, 7, 7, 8, 7, 7, 7, 5, 7, 7, 7, 7, 7, 1, 1, 5, 1, 7, 1, 4, 1, 7, 1, 1, 5, 5, 1, 1, 4, 1, 9, 9, 9, 1, 4, 3, 3,2, 7, 2, 7, 2, 3, 4, 8, 3, 3, 7, 2, 3, 0],
    [0, 7, 7, 1, 1, 8, 7, 5, 7, 7, 5, 7, 7, 1, 5, 5, 1, 7, 1, 4, 1, 7, 1, 1, 5, 5, 1, 2, 4, 1, 9, (1,(2, 4)), 9, 1, 4,3, 3,3, 7, 2, 7, 2, 3, 4, 3, 3, 8, 7, 2, 3, 0],
    [0, 7, 7, 1, 10, 8, 7, 7, 5, 7, 7, 5, 7, 1, 1, 1, 1, 7, 1, 4, 1, 7, 1, 1, 1, 1, 2, 2, 4, 4, 4, 4, 1, 1, 4, 3, 3,3, 3, 3, 7, 2, 3, 4, 3, 3, 8, 7, 3, 3, 0],
    [0, 7, 7, 10, 10, 10, 7, 7, 7, 7, 7, 5, 7, 1, 1, 1, 1, 7, 1, 4, 1, 7, 7, 7, 7, 7, 7, 7, 4, 1, 1, 1, 1, 1, 4, 3,3, 3, 3, 3, 7, 3, 3, 4, 3, 3, 3, 7, 3, 3, 0],
    [0, 7, 7, 9, 9, 9, 2, 7, 7, 7, 7, 7, 7, 1, 1, 1, 5, 7, 1, 4, 1, 7, 7, 7, 7, 7, 7, 7, 4, 1, 1, 1, 5, 1, 4, 3, 3,3, 3, 3, 7, 3, 3, 4, 3, 8, 3, 7, 3, 3, 0],
    [0, 7, 2, 9, (1,(2, 4)), 9, 2, 7, 7, 7, 7, 7, 7, 1, 10, 1, 1, 7, 1, 4, 1, 7, 7, 7, 7, 7, 7, 7, 4, 7, 1, 1, 5, 1, 4,4,4, 4, 4, 4, 4, 4, 4, 4, 3, 8, 2, 7, 2, 3, 0],
    [0, 7, 8, 5, 4, 1, 7, 7, 7, 7, 7, 7, 2, 10, 10, 10, 1, 7, 1, 4, 2, 2, 2, 2, 1, 1, 1, 1, 4, 7, 1, 1, 5, 1, 3, 3,3, 3, 3, 3, 7, 4, 3, 10, 3, 3, 2, 7, 8, 3, 0],
    [0, 7, 8, 1, 4, 1, 7, 7, 7, 7, 7, 7, 2, 9, 9, 9, 1, 7, 1, 4, 2, 2, 2, 8, 1, 1, 1, 1, 4, 7, 2, 5, 1, 1, 3, 5, 5,5, 3, 2, 7, 4, 10, 10, 10, 3, 5, 7, 8, 3, 0],
    [0, 7, 7, 2, 4, 4, 7, 7, 7, 7, 7, 7, 7, 9, (1,(2, 4), 'Key'), 9, 1, 1, 1, 4, 1, 1, 1, 8, 1, 8, 5, 1, 4, 7, 2, 1, 1, 1, 3,3, 3,5, 3, 2, 7, 4, 9, 9, 9, 3, 3, 2, 2, 3, 0],
    [0, 7, 7, 7, 7, 4, 7, 7, 7, 7, 7, 7, 7, 1, 4, 1, 1, 1, 1, 4, 1, 1, 8, 1, 1, 8, 5, 1, 4, 7, 2, 1, 1, 1, 3, 3, 3,2, 2, 2, 7, 4, 9, (1,(2, 4)), 9, 3, 8, 2, 3, 3, 0],
    [0, 7, 7, 7, 7, 4, 7, 7, 7, 7, 7, 7, 7, 1, 4, 4, 4, 4, 4, 4, 1, 1, 8, 1, 1, 1, 1, 1, 4, 7, 7, 7, 7, 7, 7, 7, 7,7, 7, 7, 7, 4, 4, 4, 3, 3, 8, 3, 3, 5, 0],
    [0, 7, 7, 7, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 4, 7, 7, 7, 7, 7, 7, 7, 7,7, 7, 7, 7, 3, 3, 3, 3, 5, 3, 3, 5, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3,3, 3, 2, 2, 3, 3, 3, 3, 5, 3, 3, 5, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3,3, 3, 2, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 1, 5, 1, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 5, 1, 1, 1, 3, 3, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 1, 5, 1, 5, 5, 1, 1, 1, 5, 5, 1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 3, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

################### CAMERA ###################
camera_x = 0
camera_y = 0

x_move_map = 0
y_move_map = 0

is_move_map = False

################### MOVE ###################

x = 900
y = 360

old_pos = (x, y)

player_move = True

velocity = 9


################### QUEST ###################

quests = [[1.0, False], [1.8, False]]



###################################### INIT ######################################

try:
    x, y, inventory, money, quests, items, camera_x, camera_y = charger()
except EOFError:
    print("start without save")

x_map, y_map = pos_map()



###################################### MAIN BOUCLE ######################################

while running:
    screen.fill((0, 0, 0))
    init_map()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Fermeture')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_paused = not is_paused

            if event.key == pygame.K_e and not is_paused and not is_dialogue:
                in_inventory = not in_inventory
                bag_inventory_frame = 0

            if event.key == pygame.K_z and not is_paused and not in_inventory:
                find_item()

                if is_dialogue:
                    print(all_pages)
                    if id_page >= len(all_pages) - 1:
                        print('A')
                        is_dialogue = False
                        id_page = 0
                        player_move = True
                        for quest in quests:
                            if quest[1] == True:
                                if quest[0] == 1.00:
                                    take_item('Letter', 1)
                                    quest[0] += 0.01
                                    quest[1] = False
                                elif quest[0] == 1.01:
                                    if del_item('Letter', 2):
                                        quest[0] += 0.01
                                        money += 100
                                        take_item('Key', 1)
                                    quest[1] = False
                    else:
                        id_page += 1

                else:
                    for pnj in PNJS:
                        if pnj[3]:
                            player_move = False
                            is_dialogue = True

    keys_pressed = pygame.key.get_pressed()
    if not is_paused:
        if not in_inventory:
            set_pnj()
            take_dor()

            for item in items:
                if item[2] == 'Letter':
                    screen.blit(LETTER, (item[0] * SIZE + (LETTER.get_width() // 2) - camera_x, item[1] * SIZE + (LETTER.get_height() // 2) - camera_y))
                elif item[2] == 'Weed':
                    screen.blit(WEED, (item[0] * SIZE + (LETTER.get_width() // 2) - camera_x, item[1] * SIZE + (LETTER.get_height() // 2) - camera_y))
                elif item[2] == 'Spliff':
                    screen.blit(SPLIFF, (item[0] * SIZE + (LETTER.get_width() // 2) - camera_x, item[1] * SIZE + (LETTER.get_height() // 2) - camera_y))
                elif item[2] == 'Pouch':
                    screen.blit(POUCH, (item[0] * SIZE + (LETTER.get_width() // 2) - camera_x, item[1] * SIZE + (LETTER.get_height() // 2) - camera_y))
                elif item[2] == 'key':
                    screen.blit(KEY, (item[0] * SIZE + (LETTER.get_width() // 2) - camera_x, item[1] * SIZE + (LETTER.get_height() // 2) - camera_y))
                else:
                    screen.blit(ORION, (item[0] * SIZE + (ORION.get_width() // 2) - camera_x, item[1] * SIZE + (ORION.get_height() // 2) - camera_y))

            old_x, old_y = x, y
            is_runing = keys_pressed[pygame.K_LSHIFT]
            if player_move:
                if is_runing:
                    velocity = 18
                else:
                    velocity = 12
                vx = (keys_pressed[pygame.K_RIGHT] - keys_pressed[pygame.K_LEFT]) * velocity
                vy = (keys_pressed[pygame.K_DOWN] - keys_pressed[pygame.K_UP]) * velocity
                x += vx
                y += vy
                x_map, y_map = pos_map()

            if not camera_x + cam_size_x // 3 <= x <= camera_x + cam_size_x // 3 * 2:
                camera_x += vx
            if not camera_y + cam_size_y // 3 <= y <= camera_y + cam_size_y // 3 * 2:
                camera_y += vy
            player_animation()
            x, y, vx, vy = bloque_collision((old_x, old_y), (x, y), vx, vy)

            screen.blit(player, (x - camera_x, y - camera_y))
        else:
            blit_inventory()
    else:
        menu()

    pygame.display.flip()
    CLOCK.tick(30)
    pygame.display.update()