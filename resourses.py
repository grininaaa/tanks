import pygame
import os

HEIGHT = 600
WIDTH = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
main_folder = os.path.dirname(__file__)
image_folder = os.path.join(main_folder, "image")

# изображения основного меню
fon_img = pygame.image.load(os.path.join(image_folder, 'back.jpg')).convert_alpha()
exit_btn_img = pygame.image.load(os.path.join(image_folder, 'exit.png')).convert_alpha()
opt_btn_img = pygame.image.load(os.path.join(image_folder, 'options.png')).convert_alpha()
play_btn_img = pygame.image.load(os.path.join(image_folder, 'play.png')).convert_alpha()
options_bckg = pygame.image.load(os.path.join(image_folder, 'bb.png')).convert_alpha()

# изображения препятствий
beton = pygame.image.load(os.path.join(image_folder, 'beton.png')).convert_alpha()
brick = pygame.image.load(os.path.join(image_folder, 'brick.png')).convert_alpha()
forest = pygame.image.load(os.path.join(image_folder, 'forest.png')).convert_alpha()
pol = pygame.image.load(os.path.join(image_folder, 'pol.png')).convert_alpha()
water = pygame.image.load(os.path.join(image_folder, 'water.png')).convert_alpha()
obstacles_list = [pol, forest, brick, water, beton]

#изображения танков
tankv1_img = pygame.image.load(os.path.join(image_folder, 'tankv1.png')).convert_alpha()


#изображения снаряда
missile_img = pygame.image.load(os.path.join(image_folder, 'missile.png')).convert_alpha()

level1_template = [[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                   [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                   [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
                   [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                   [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                   [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

#


