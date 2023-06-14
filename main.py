import sys
from classes import *
import random


def main():
    global screen
    buttons_group = pygame.sprite.Group()
    exit_btn = Button(exit_btn_img, (WIDTH // 2, HEIGHT // 2))
    play_btn = Button(play_btn_img, (WIDTH // 2, HEIGHT // 2 - 100))
    opt_btn = Button(opt_btn_img, (WIDTH // 2, HEIGHT // 2 + 100))
    buttons_group.add(exit_btn, play_btn, opt_btn)
    while True:
        screen.blit(fon_img, fon_img.get_rect())
        buttons_group.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pose = pygame.mouse.get_pos()
                if exit_btn.rect.collidepoint(mouse_pose):
                    print("Вы нажали кнопку выхода.")
                    sys.exit()
                elif play_btn.rect.collidepoint(mouse_pose):
                    play()
                elif opt_btn.rect.collidepoint(mouse_pose):
                    options()


def play():
    global screen
    fps = 60
    pygame_clock = pygame.time.Clock()
    tank_group = pygame.sprite.Group()
    missile_group = pygame.sprite.Group()
    player_tank = Player()
    tank_group.add(player_tank)
    obstacles_group = pygame.sprite.Group()
    for i in range(len(level1_template)):
        for j in range(len(level1_template)):
            if level1_template[i][j] == 1:
                type = random.randint(1, 4)
                landscape = Obstacle(type, (j * 40, i * 40))
                obstacles_group.add(landscape)

    while True:
        pygame_clock.tick(fps)
        screen.blit(options_bckg, options_bckg.get_rect())
        obstacles_group.draw(screen)
        player_tank.move(obstacles_group)
        missile_group.update()
        missile_group.draw(screen)
        tank_group.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    missile_group.add(Bullet(player_tank.direction, player_tank.rect.center))
                    print(missile_group)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pose = pygame.mouse.get_pos()
                if player_tank.rect.collidepoint(mouse_pose):
                    print("Вы нажали кнопку выхода.")
                    return



def options():
    global screen
    screen.blit(options_bckg, options_bckg.get_rect())
    buttons_group = pygame.sprite.Group()
    back_btn = Button(exit_btn_img, (WIDTH // 2, HEIGHT // 2))
    buttons_group.add(back_btn)
    buttons_group.draw(screen)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pose = pygame.mouse.get_pos()
                if back_btn.rect.collidepoint(mouse_pose):
                    print("Вы нажали кнопку выхода.")
                    return


main()
