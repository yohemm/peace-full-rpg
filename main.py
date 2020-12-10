import pygame

pygame.init()
cam_size_x = 1280
cam_size_y = 720

pygame.display.set_caption('RPG TEST')
screen = pygame.display.set_mode((cam_size_x, cam_size_y))


# Fonction
def under_block(pos_block_x, pos_block_y, x_map, y_map):
    id_list = [1,2,3,7]
    is_detected = int
    for id in id_list:
        if Levels[0][y_map][x_map + 1] == id:
            is_detected = id
            break
        elif Levels[0][y_map][x_map - 1] == id:
            is_detected = id
            break
        elif Levels[0][y_map + 1][x_map ] == id:
            is_detected = id
            break
        elif Levels[0][y_map - 1][x_map ] == id:
            is_detected = id
            break
    if is_detected == 1:
        screen.blit(grass, (pos_block_x, pos_block_y))
    elif is_detected == 2:
        screen.blit(sand, (pos_block_x, pos_block_y))
    elif is_detected == 3:
        screen.blit(snow, (pos_block_x, pos_block_y))
    elif is_detected == 7:
        screen.blit(watter, (pos_block_x, pos_block_y))
    else:
        screen.blit(grass, (pos_block_x, pos_block_y))




def init_map():
    for y_map, ligne in enumerate(Levels[0]):
        for x_map, case in enumerate(ligne):
            pos_block_x = x_map * size - camera_x
            pos_block_y = y_map * size - camera_y
            if case == 1:
            # id de l'herbe
                screen.blit(grass, (pos_block_x, pos_block_y))
            if case == 2:
            # id du sable
                screen.blit(sand, (pos_block_x, pos_block_y))
            if case == 3:
            # id de la neige
                screen.blit(snow, (pos_block_x, pos_block_y))
            if case == 4:
            # id de le chemin
                under_block(pos_block_x, pos_block_y, x_map, y_map)
                # Croisement de 4 chemin
                if Levels[0][y_map][x_map - 1] == 4 and Levels[0][y_map][x_map + 1] == 4 and Levels[0][y_map - 1][x_map] == 4 and Levels[0][y_map + 1][x_map] == 4:
                    screen.blit(way1, (pos_block_x, pos_block_y))

                # Croisement de 3 chemin
                elif Levels[0][y_map][x_map - 1] == 4 and Levels[0][y_map][x_map + 1] == 4 and Levels[0][y_map - 1][x_map] == 4 :
                    screen.blit(way2, (pos_block_x, pos_block_y))
                elif Levels[0][y_map][x_map - 1] == 4 and Levels[0][y_map][x_map + 1] == 4 and Levels[0][y_map + 1][x_map] == 4 :
                    screen.blit(pygame.transform.rotate(way2, 180), (pos_block_x, pos_block_y))
                elif Levels[0][y_map][x_map + 1] == 4 and Levels[0][y_map - 1][x_map] == 4 and Levels[0][y_map + 1][x_map] == 4:
                    screen.blit(pygame.transform.rotate(way2, 270), (pos_block_x, pos_block_y))
                elif Levels[0][y_map][x_map - 1] == 4 and Levels[0][y_map - 1][x_map] == 4 and Levels[0][y_map + 1][x_map] == 4:
                    screen.blit(pygame.transform.rotate(way2, 90), (pos_block_x, pos_block_y))

                    # Croisement de 2 chemin
                elif Levels[0][y_map][x_map + 1] == 4 and Levels[0][y_map - 1][x_map] == 4:
                    screen.blit(way3, (pos_block_x, pos_block_y))
                elif Levels[0][y_map][x_map - 1] == 4 and Levels[0][y_map - 1][x_map] == 4:
                    screen.blit(pygame.transform.rotate(way3, 90), (pos_block_x, pos_block_y))
                elif Levels[0][y_map][x_map - 1] == 4 and Levels[0][y_map + 1][x_map] == 4:
                    screen.blit(pygame.transform.rotate(way3, 180), (pos_block_x, pos_block_y))
                elif Levels[0][y_map][x_map + 1] == 4 and Levels[0][y_map + 1][x_map] == 4:
                    screen.blit(pygame.transform.rotate(way3, 270), (pos_block_x, pos_block_y))

                    #Pas de croisement
                elif Levels[0][y_map][x_map - 1] == 4 or Levels[0][y_map][x_map + 1] == 4:
                    screen.blit(pygame.transform.rotate(way, 90), (pos_block_x, pos_block_y))
                else:
                    screen.blit(way, (pos_block_x, pos_block_y))
            if case == 5:
            # id de le rocher
                under_block(pos_block_x, pos_block_y, x_map, y_map)
                screen.blit(rock, (pos_block_x, pos_block_y))
            if case == 6:
            # id de la falaise
                screen.blit(fall, (pos_block_x, pos_block_y))
            if case == 7:
            # id de l'eau
                screen.blit(watter, (pos_block_x, pos_block_y))
            if case == 8:
            # id de l'abre
                under_block(pos_block_x, pos_block_y, x_map, y_map)
                if Levels[0][y_map-1][x_map] == 8 and not Levels[0][y_map+1][x_map] == 8:
                    screen.blit(tree2, (pos_block_x, pos_block_y))
                else:
                    screen.blit(tree, (pos_block_x, pos_block_y))
            if case == 9:
            # id des murs
                screen.blit(wall, (pos_block_x, pos_block_y))
            if case == 10:
            # id des toits
                if Levels[0][y_map][x_map - 1] == 10 and Levels[0][y_map][x_map + 1] == 10:
                    screen.blit(roof, (pos_block_x, pos_block_y))


                elif Levels[0][y_map][x_map - 1] == 10:
                    under_block(pos_block_x, pos_block_y, x_map, y_map)
                    screen.blit(roof2, (pos_block_x, pos_block_y))

                elif Levels[0][y_map][x_map + 1] == 10:
                    under_block(pos_block_x, pos_block_y, x_map, y_map)
                    screen.blit(roof1, (pos_block_x, pos_block_y))

                else:
                    under_block(pos_block_x, pos_block_y, x_map, y_map)
                    screen.blit(roof3, (pos_block_x, pos_block_y))


def pos_map():
    x_map = x // size
    y_map = y // size
    return x_map, y_map


def get_neighbour_blocks(x_map_start, y_map_start):
    blocks = list()
    for y_map in range(y_map_start, y_map_start + 2):
        for x_map in range(x_map_start, x_map_start + 2):
            try:
                if not type(Levels[0][y_map][x_map]) is tuple:
                    if Levels[0][y_map][x_map] >= 5:
                        topleft = x_map * size, y_map * size
                        blocks.append(pygame.Rect((topleft), (size, size)))
            except IndexError:
                print('Erreur, Petit Tricheur')
    return blocks


def bloque_collision(old_pos, new_pos, vx, vy):
    old_rect = pygame.Rect(old_pos, (size - 10, size - 10))
    new_rect = pygame.Rect(new_pos, (size - 10, size - 10))
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

    x = pos_x
    y = pos_y

    old_x = x
    old_y = y
    old_pos = (old_x, old_y)


    print(x, ' ',y)

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


def dialogue(all_pages, parameter):
    global is_dialogue
    if not is_dialogue:
        return
    police = pygame.font.Font(None, 20)
    rect = pygame.rect.Rect(30, cam_size_y - 100, cam_size_x - 100, 75)
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
        surface = pygame.Surface(rect.size)
        surface.fill((0, 0, 0))
        for line in final_lines[0]:
            if accumulated_height + police.size(line)[1] >= rect.height:
                print('Un mots est trop hait pour etre afficher dnas le texte')
            if line != "":
                affichage = police.render(line, 1, (255, 255, 255))
            if parameter == 0:
                surface.blit(affichage, (0, accumulated_height))
            elif parameter == 1:
                surface.blit(affichage, ((rect.width - surface.get_width()) // 2, accumulated_height))
            elif parameter == 2:
                surface.blit(affichage, (rect.width - surface.get_width(), accumulated_height))
            else:
                print('Le parametre du text est invalide')
            accumulated_height += police.size(line)[1]
        screen.blit(surface, rect)
    return


# VARIABLE
size = 64
clock = pygame.time.Clock()
rock = pygame.image.load('asset/Rock.png')
rock = pygame.transform.scale(rock, (size, size)).convert_alpha()
tree = pygame.image.load('asset/Tree.png')
tree = pygame.transform.scale(tree, (size, size)).convert_alpha()
tree2 = pygame.image.load('asset/Tree2.png')
tree2 = pygame.transform.scale(tree2, (size, size)).convert_alpha()
grass = pygame.image.load('asset/Grass.png')
grass = pygame.transform.scale(grass, (size, size)).convert()
wall = pygame.image.load('asset/Wall.png')
wall = pygame.transform.scale(wall, (size, size)).convert()
wall1 = pygame.image.load('asset/Wall1.png')
wall1 = pygame.transform.scale(wall1, (size, size)).convert()
wall2 = pygame.image.load('asset/Wall2.png')
wall2 = pygame.transform.scale(wall2, (size, size)).convert()
wall3 = pygame.image.load('asset/Wall3.png')
wall3 = pygame.transform.scale(wall3, (size, size)).convert()
wall4 = pygame.image.load('asset/Wall4.png')
wall4 = pygame.transform.scale(wall4, (size, size)).convert()
wall5 = pygame.image.load('asset/Wall5.png')
wall5 = pygame.transform.scale(wall5, (size, size)).convert()
watter = pygame.image.load('asset/Water.png')
watter = pygame.transform.scale(watter, (size, size)).convert()
sand = pygame.image.load('asset/Sand.png')
sand = pygame.transform.scale(sand, (size, size)).convert()
way = pygame.image.load('asset/Way.png')
way = pygame.transform.scale(way, (size, size)).convert_alpha()
way1 = pygame.image.load('asset/Way1.png')
way1 = pygame.transform.scale(way1, (size, size)).convert_alpha()
way2 = pygame.image.load('asset/Way2.png')
way2 = pygame.transform.scale(way2, (size, size)).convert_alpha()
way3 = pygame.image.load('asset/Way3.png')
way3 = pygame.transform.scale(way3, (size, size)).convert_alpha()
fall = pygame.image.load('asset/Fall.png')
fall = pygame.transform.scale(fall, (size, size)).convert()
snow = pygame.image.load('asset/Snow.png')
snow = pygame.transform.scale(snow, (size, size)).convert()
roof = pygame.image.load('asset/Roof.png')
roof = pygame.transform.scale(roof, (size, size)).convert_alpha()
roof1 = pygame.image.load('asset/Roof1.png')
roof1 = pygame.transform.scale(roof1, (size, size)).convert_alpha()
roof2 = pygame.image.load('asset/Roof2.png')
roof2 = pygame.transform.scale(roof2, (size, size)).convert_alpha()
roof3 = pygame.image.load('asset/Roof3.png')
roof3 = pygame.transform.scale(roof3, (size, size)).convert_alpha()

id_page = 0
Levels = [
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 5, 1, 1, 5, 1, 1, 2, 7, 7, 2, 2, 1, 1, 1, 1, 8, 1, 1, 1, 3, 3, 3,
         3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 1, 1, 5, 1, 1, 1, 1, 2, 7, 7, 7, 2, 5, 8, 1, 1, 8, 1, 8, 1, 3, 3, 3,
         3, 3, 3, 3, 3, 3, 3, 3, 8, 3, 3, 3, 3, 0],
        [0, 7, 5, 7, 5, 7, 7, 7, 7, 7, 7, 7, 7, 2, 5, 1, 1, 1, 1, 5, 2, 2, 7, 7, 7, 1, 1, 8, 1, 1, 1, 1, 8, 1, 3, 5, 3,
         3, 3, 3, 3, 3, 3, 3, 3, 8, 3, 3, 8, 3, 0],
        [0, 7, 5, 7, 7, 7, 7, 5, 5, 7, 7, 7, 7, 2, 1, 1, 1, 1, 5, 8, 2, 7, 7, 7, 7, 8, 1, 1, 8, 5, 1, 1, 1, 1, 3, 5, 3,
         3, 4, 4, 4, 4, 3, 8, 3, 3, 8, 3, 8, 8, 0],
        [0, 7, 7, 7, 7, 7, 7, 5, 7, 7, 7, 7, 2, 4, 1, 1, 1, 1, 1, 8, 2, 7, 7, 7, 7, 8, 1, 1, 8, 1, 8, 1, 1, 1, 3, 5, 3,
         3, 4, 3, 3, 3, 3, 8, 3, 3, 8, 3, 3, 8, 0],
        [0, 7, 5, 7, 7, 5, 7, 7, 7, 7, 7, 7, 2, 4, 1, 5, 10, 1, 1, 1, 2, 7, 7, 7, 7, 1, 1, 1, 1, 1, 8, 8, 1, 1, 3, 3, 3,
         3, 4, 3, 3, 3, 3, 3, 3, 3, 8, 3, 8, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 5, 5, 7, 7, 4, 1, 10, 10, 10, 1, 1, 2, 7, 7, 7, 7, 2, 8, 1, 8, 1, 1, 8, 1, 1, 3, 3,
         3, 5, 4, 3, 3, 5, 3, 3, 3, 3, 8, 3, 8, 3, 0],
        [0, 7, 7, 7, 7, 7, 5, 7, 5, 7, 7, 7, 7, 4, 1, 9, 9, 9, 8, 1, 2, 7, 7, 7, 2, 2, 8, 1, 8, 1, 1, 1, 10, 1, 3, 5, 3,
         3, 4, 8, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 7, 1, 8, 7, 7, 5, 7, 5, 7, 7, 2, 2, 4, 1, 9, (200, 500), 9, 8, 1, 2, 2, 7, 7, 7, 2, 1, 1, 1, 1, 1, 10, 10, 10, 3, 3,
         3, 3, 4, 8, 3, 3, 3, 3, 3, 3, 3, 3, 3, 8, 0],
        [0, 7, 1, 8, 7, 7, 5, 7, 7, 7, 7, 2, 2, 4, 1, 1, 4, 1, 1, 1, 1, 2, 7, 7, 2, 8, 1, 5, 10, 1, 1, 9, 9, 9, 3, 3, 3,
         5, 4, 3, 8, 3, 3, 3, 10, 3, 3, 8, 3, 8, 0],
        [0, 7, 1, 10, 1, 7, 7, 7, 7, 7, 7, 2, 2, 4, 4, 4, 4, 1, 1, 1, 1, 2, 7, 7, 2, 8, 1, 10, 10, 10, 1, 9, (100,400), 9, 3,
         3, 5, 5, 4, 3, 8, 3, 3, 10, 10, 10, 3, 8, 3, 3, 0],
        [0, 7, 10, 10, 10, 1, 7, 7, 7, 7, 7, 2, 2, 1, 1, 1, 4, 1, 1, 1, 1, 2, 7, 7, 2, 1, 1, 9, 9, 9, 1, 1, 4, 1, 5, 3,
         3, 3, 4, 3, 3, 3, 3, 9, 9, 9, 3, 3, 3, 3, 0],
        [0, 7, 9, 9, 9, 1, 7, 7, 7, 8, 7, 7, 7, 2, 1, 1, 4, 1, 1, 10, 1, 1, 1, 7, 1, 1, 1, 9, (400, 900), 9, 1, 1, 4, 1, 3, 3,
         3, 3, 4, 8, 3, 3, 3, 9, (1300, 900), 9, 3, 3, 3, 3, 0],
        [0, 7, 9, (900, 1300), 9, 1, 7, 7, 1, 8, 7, 7, 7, 2, 1, 1, 4, 1, 10, 10, 10, 1, 1, 7, 1, 5, 1, 1, 4, 1, 1, 1, 4, 1, 3, 3,
         3, 3, 4, 8, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 0],
        [0, 7, 1, 4, 1, 7, 7, 7, 1, 7, 7, 7, 7, 2, 1, 1, 4, 1, 9, 9, 9, 1, 1, 7, 1, 5, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4,
         4, 4, 3, 3, 3, 3, 3, 4, 3, 3, 10, 3, 3, 0],
        [0, 7, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 4, 1, 9, (0, 1600), 9, 1, 1, 7, 1, 1, 5, 1, 4, 1, 1, 1, 1, 1, 3, 3, 3,
         3, 3, 3, 3, 5, 3, 3, 4, 3, 10, 10, 10, 3, 0],
        [0, 7, 7, 1, 7, 7, 7, 7, 7, 7, 4, 7, 4, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 7, 1, 1, 1, 1, 4, 1, 1, 10, 1, 1, 3, 7, 2,
         3, 3, 3, 3, 5, 3, 3, 4, 3, 9, 9, 9, 3, 0],
        [0, 7, 7, 1, 7, 7, 7, 7, 7, 7, 4, 7, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 7, 1, 1, 1, 1, 4, 1, 10, 10, 10, 8, 2, 7,
         2, 3, 5, 5, 3, 3, 3, 3, 4, 3, 9, (0, 1600), 9, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 4, 7, 7, 7, 7, 7, 7, 1, 4, 4, 1, 7, 7, 7, 1, 10, 1, 1, 4, 1, 9, 9, 9, 8, 2, 7, 2,
         3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 3, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 4, 7, 7, 7, 7, 7, 7, 2, 4, 4, 1, 7, 7, 7, 10, 10, 10, 1, 4, 1, 9, (0, 1600), 9, 1, 3, 7,
         2, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 4, 7, 7, 2, 2, 2, 7, 2, 5, 4, 1, 7, 2, 2, 9, 9, 9, 1, 4, 1, 1, 4, 1, 1, 8, 7, 2,
         5, 3, 3, 7, 3, 3, 4, 3, 3, 3, 3, 3, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 4, 7, 7, 8, 2, 2, 7, 5, 1, 4, 1, 7, 2, 1, 9, (0, 1600), 9, 1, 4, 1, 1, 4, 8, 1, 8, 7, 3,
         5, 3, 2, 7, 2, 2, 4, 3, 2, 2, 3, 3, 5, 0],
        [0, 7, 5, 5, 5, 5, 5, 7, 7, 7, 4, 7, 7, 8, 1, 8, 7, 1, 1, 4, 1, 7, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 7, 3,
         3, 3, 2, 7, 2, 2, 4, 3, 7, 2, 3, 3, 5, 0],
        [0, 7, 5, 7, 7, 7, 7, 7, 7, 7, 4, 7, 7, 2, 1, 8, 7, 1, 1, 4, 1, 7, 5, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 3, 7, 3,
         3, 3, 2, 7, 7, 7, 4, 7, 7, 2, 3, 2, 3, 0],
        [0, 7, 5, 7, 7, 7, 5, 7, 7, 7, 1, 7, 7, 2, 1, 2, 7, 7, 7, 4, 7, 7, 1, 1, 5, 1, 1, 1, 4, 1, 1, 1, 1, 1, 3, 7, 3,
         5, 5, 2, 7, 7, 7, 4, 7, 7, 7, 7, 7, 3, 0],
        [0, 7, 7, 7, 7, 5, 7, 7, 7, 7, 1, 7, 7, 5, 1, 2, 7, 7, 7, 4, 7, 7, 1, 5, 1, 1, 5, 1, 4, 4, 4, 4, 4, 4, 4, 7, 3,
         3, 3, 3, 7, 3, 3, 4, 2, 7, 7, 7, 7, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 7, 7, 2, 8, 2, 7, 2, 2, 4, 2, 7, 1, 1, 1, 1, 5, 1, 4, 1, 1, 1, 1, 1, 4, 7, 3,
         3, 3, 3, 7, 3, 3, 4, 2, 7, 7, 7, 7, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 2, 7, 7, 7, 2, 8, 2, 7, 2, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 4, 7, 7,
         7, 7, 3, 7, 3, 3, 4, 3, 3, 2, 7, 2, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 2, 7, 7, 1, 4, 1, 7, 1, 1, 1, 1, 1, 1, 4, 1, 1, 10, 1, 1, 4, 7, 7,
         7, 7, 7, 7, 5, 3, 4, 3, 3, 2, 7, 2, 3, 0],
        [0, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 1, 2, 7, 7, 1, 4, 1, 7, 1, 1, 1, 1, 5, 1, 4, 1, 10, 10, 10, 1, 4, 3,
         2, 2, 7, 7, 7, 5, 3, 4, 8, 3, 2, 7, 2, 3, 0],
        [0, 7, 7, 8, 7, 7, 7, 5, 7, 7, 7, 7, 7, 1, 1, 5, 1, 7, 1, 4, 1, 7, 1, 1, 5, 5, 1, 1, 4, 1, 9, 9, 9, 1, 4, 3, 3,
         2, 7, 2, 7, 2, 3, 4, 8, 3, 3, 7, 2, 3, 0],
        [0, 7, 7, 1, 1, 8, 7, 5, 7, 7, 5, 7, 7, 1, 5, 5, 1, 7, 1, 4, 1, 7, 1, 1, 5, 5, 1, 2, 4, 1, 9, (300, 900), 9, 1, 4, 3, 3,
         3, 7, 2, 7, 2, 3, 4, 3, 3, 8, 7, 2, 3, 0],
        [0, 7, 7, 1, 10, 8, 7, 7, 5, 7, 7, 5, 7, 1, 1, 1, 1, 7, 1, 4, 1, 7, 1, 1, 1, 1, 2, 2, 4, 4, 4, 4, 1, 1, 4, 3, 3,
         3, 3, 3, 7, 2, 3, 4, 3, 3, 8, 7, 3, 3, 0],
        [0, 7, 7, 10, 10, 10, 7, 7, 7, 7, 7, 5, 7, 1, 1, 1, 1, 7, 1, 4, 1, 7, 7, 7, 7, 7, 7, 7, 4, 1, 1, 1, 1, 1, 4, 3,
         3, 3, 3, 3, 7, 3, 3, 4, 3, 3, 3, 7, 3, 3, 0],
        [0, 7, 7, 9, 9, 9, 2, 7, 7, 7, 7, 7, 7, 1, 1, 1, 5, 7, 1, 4, 1, 7, 7, 7, 7, 7, 7, 7, 4, 1, 1, 1, 5, 1, 4, 3, 3,
         3, 3, 3, 7, 3, 3, 4, 3, 8, 3, 7, 3, 3, 0],
        [0, 7, 2, 9, (1200, 800), 9, 2, 7, 7, 7, 7, 7, 7, 1, 10, 1, 1, 7, 1, 4, 1, 7, 7, 7, 7, 7, 7, 7, 4, 7, 1, 1, 5, 1, 4, 4,
         4, 4, 4, 4, 4, 4, 4, 4, 3, 8, 2, 7, 2, 3, 0],
        [0, 7, 8, 5, 4, 1, 7, 7, 7, 7, 7, 7, 2, 10, 10, 10, 1, 7, 1, 4, 2, 2, 2, 2, 1, 1, 1, 1, 4, 7, 1, 1, 5, 1, 3, 3,
         3, 3, 3, 3, 7, 4, 3, 10, 3, 3, 2, 7, 8, 3, 0],
        [0, 7, 8, 1, 4, 1, 7, 7, 7, 7, 7, 7, 2, 9, 9, 9, 1, 7, 1, 4, 2, 2, 2, 8, 1, 1, 1, 1, 4, 7, 2, 5, 1, 1, 3, 5, 5,
         5, 3, 2, 7, 4, 10, 10, 10, 3, 5, 7, 8, 3, 0],
        [0, 7, 7, 2, 4, 4, 7, 7, 7, 7, 7, 7, 7, 9, (300,100), 9, 1, 1, 1, 4, 1, 1, 1, 8, 1, 8, 5, 1, 4, 7, 2, 1, 1, 1, 3, 3, 3,
         5, 3, 2, 7, 4, 9, 9, 9, 3, 3, 2, 2, 3, 0],
        [0, 7, 7, 7, 7, 4, 7, 7, 7, 7, 7, 7, 7, 1, 4, 1, 1, 1, 1, 4, 1, 1, 8, 1, 1, 8, 5, 1, 4, 7, 2, 1, 1, 1, 3, 3, 3,
         2, 2, 2, 7, 4, 9, (300, 700), 9, 3, 8, 2, 3, 3, 0],
        [0, 7, 7, 7, 7, 4, 7, 7, 7, 7, 7, 7, 7, 1, 4, 4, 4, 4, 4, 4, 1, 1, 8, 1, 1, 1, 1, 1, 4, 7, 7, 7, 7, 7, 7, 7, 7,
         7, 7, 7, 7, 4, 4, 4, 3, 3, 8, 3, 3, 5, 0],
        [0, 7, 7, 7, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 4, 7, 7, 7, 7, 7, 7, 7, 7,
         7, 7, 7, 7, 3, 3, 3, 3, 5, 3, 3, 5, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3,
         3, 3, 2, 2, 3, 3, 3, 3, 5, 3, 3, 5, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3,
         3, 3, 2, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 1, 5, 1, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 5, 1, 1, 1, 3, 3, 5,
         5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 1, 5, 1, 5, 5, 1, 1, 1, 5, 5, 1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 3, 5, 5,
         5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 3, 3, 3,
         3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3,
         3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ]
]

camera_x = 0
camera_y = 0

player = pygame.image.load('asset/Player.png')
player = pygame.transform.scale(player, (size - 10, size - 10)).convert_alpha()

x_move_map = 0
y_move_map = 0
is_move_map = False

x = 640
y = 360

tp(400, 964)
old_pos = (x, y)
velocity = 8
player_move = True

is_dialogue = False

all_pages = list()

pnjs = [[1, 2,
         "Appui sur les FLECHES DIRECTIONELLES pour te deplacer,\nTu peux passer se message en appuyant sur Z!ENDPAGETu peux aussi courrir en appuyant sur SHIFT."],
        [3, 6,
         "Appui sur les FLECHES DIRECTIONELLES pour te deplacer,\nTu peux passer se message en appuyant sur Z!ENDPAGETu peux aussi courrir en appuyant sur SHIFT."]]

#   BOUCLE DU JEU
running = True
while running:
    screen.fill((0, 0, 0))
    init_map()
    x_map, y_map = pos_map()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Fermeture')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if is_dialogue:
                    if id_page >= len(all_pages) - 1:
                        is_dialogue = False
                        id_page = -1
                        player_move = True
                    id_page += 1
                elif player_in_range_pnj:
                    player_move = False
                    is_dialogue = True

    keys_pressed = pygame.key.get_pressed()
    old_x, old_y = x, y
    is_runing = keys_pressed[pygame.K_LSHIFT]
    if player_move:
        if is_runing:
            velocity = 9
        else:
            velocity = 6
        vx = (keys_pressed[pygame.K_RIGHT] - keys_pressed[pygame.K_LEFT]) * velocity
        vy = (keys_pressed[pygame.K_DOWN] - keys_pressed[pygame.K_UP]) * velocity
        x += vx
        y += vy
    if not camera_x + cam_size_x // 3 <= x <= camera_x + cam_size_x // 3 * 2:
        camera_x += vx
    if not camera_y + cam_size_y // 3 <= y <= camera_y + cam_size_y // 3 * 2:
        camera_y += vy
    x, y, vx, vy = bloque_collision((old_x, old_y), (x, y), vx, vy)

    screen.blit(player, (x - camera_x, y - camera_y))

    for pnj in pnjs:
        screen.blit(player, (pnj[0] * size - camera_x, pnj[1] * size - camera_y))
        if abs(x - pnj[0] * size) < 100 and abs(y - pnj[1] * size) < 100:
            all_pages = pnj[2].split('ENDPAGE')
            dialogue(all_pages, 1)
            player_in_range_pnj = True
            break
        else:
            player_in_range_pnj = False

    for ligne in enumerate(Levels[0]):
        for case in enumerate(ligne):
            if case is int and case == 8:
                screen.blit(tree2,(x*size ,  (y-1) * size))

    if type(Levels[0][y_map][x_map]) is tuple:
        print('Petit prenneur de porte')
        tp(Levels[0][y_map][x_map][0], Levels[0][y_map][x_map][1])

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
