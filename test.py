import pygame
import pickle

# On initialise pygame
pygame.init()


clock = pygame.time.Clock()

map_x = int(input('Entrez la longeur de la map en block : '))
map_y = int(input('Entrez la hauteur de la map en block : '))
map_list = list()
for y in range(map_y):
    map_list.append(list())
    for x in range(map_x):
        map_list[y].append(0)
id = int(input('Selectionner un id : '))
pygame.display.set_caption('CREATION MAP')
screen_size = (1300, 700)
if screen_size[0] // map_x > screen_size[1] // map_y:
    size = screen_size[0] // map_x
else:
    print('OK')
    size = screen_size[1] // map_y
intsize = size
screen = pygame.display.set_mode(screen_size)

x = 0
y = 0

ROCK = pygame.image.load('asset/tiles/Rock.png')

TREE = pygame.image.load('asset/tiles/tree/simple/Tree.png')

GRASS = pygame.image.load('asset/tiles/Grass.png')

WALL = pygame.image.load('asset/tiles/wall/Wall.png')

WATTER = pygame.image.load('asset/tiles/Water.png')

SAND = pygame.image.load('asset/tiles/Sand.png')

ROAD_SOIL = pygame.image.load('asset/tiles/road/soil/0.png')

ROAD_TOWN = pygame.image.load('asset/tiles/road/town/0.png')

SNOW = pygame.image.load('asset/tiles/Snow.png')

ROOF = pygame.image.load('asset/tiles/roof/red/Roof.png')

resulte = ""

continuer = True
while continuer:
    mousse_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                id = int(input('Selectionner un id : '))

            if event.key == pygame.K_EQUALS:
                size *= 1.1

            elif event.key == pygame.K_6:
                size *= 0.9

            if event.key == pygame.K_UP:
                y += 1 * size
            elif event.key == pygame.K_DOWN:
                y -= 1 * size

            if event.key == pygame.K_LEFT:
                x += 1 * size
            elif event.key == pygame.K_RIGHT:
                x -= 1 * size
#SAVE
            if event.key == pygame.K_s:
                with open('map.txt', 'w') as files:
                    for line in map_list:
                        resulte += str(line) + '\n'
                    files.write(resulte)
                    files.close()
                    print('save')
            intsize = int(size)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousse_click = True

    for i in range(map_x):
        for j in range(map_y):
            pos = (i*intsize + x, j*intsize + y)
            pygame.draw.line(screen,(64,64,64), pos,((i*intsize)+intsize + x, j*intsize + y))
            pygame.draw.line(screen,(64,64,64), pos,(i*intsize + x, (j*intsize)+intsize + y))
            if mousse_click:
                if j * intsize + y < pygame.mouse.get_pos()[1] < (j * intsize)+intsize + y and i * intsize + x< pygame.mouse.get_pos()[0] < (i * intsize)+intsize +x:
                    map_list[j][i] = id
    for j in range(len(map_list)):
        for i in range(len(map_list[j])):
            pos = (i*intsize + x, j*intsize + y)
            if map_list[j][i] == 1:
                screen.blit(pygame.transform.scale(GRASS, (intsize, intsize)).convert(), pos)
            elif map_list[j][i] == 2:
                screen.blit(pygame.transform.scale(SAND, (intsize, intsize)).convert(), pos)
            elif map_list[j][i] == 3:
                screen.blit(pygame.transform.scale(SNOW, (intsize, intsize)).convert(), pos)
            elif map_list[j][i] == 4:
                screen.blit(pygame.transform.scale(ROAD_SOIL, (intsize, intsize)).convert(), pos)
            elif map_list[j][i] == 5:
                screen.blit(pygame.transform.scale(ROCK, (intsize, intsize)).convert(), pos)
            elif map_list[j][i] == 6:
                screen.blit(pygame.transform.scale(WATTER, (intsize, intsize)).convert(), pos)
            elif map_list[j][i] == 8:
                screen.blit(pygame.transform.scale(TREE, (intsize, intsize)).convert(), pos)
            elif map_list[j][i] == 9:
                screen.blit(pygame.transform.scale(WALL, (intsize, intsize)).convert(), pos)
            elif map_list[j][i] == 10:
                screen.blit(pygame.transform.scale(ROOF, (intsize, intsize)).convert(), pos)


    pygame.display.flip()
    clock.tick(20)
    pygame.display.update()
    screen.fill((0, 0, 0))
