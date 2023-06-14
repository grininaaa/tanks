import pygame.transform

from resourses import *


class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos


"""
direction:
    0 - вверх
    1- вправо
    2 - вниз
    3 - влево
    
    """


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = tankv1_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2 + 200)
        self.speed = 1
        self.direction = 0
        self.shadow = Button(self.image, self.rect.center)

    def move(self, obstacles_group):
        pressed_button = pygame.key.get_pressed()
        if pressed_button[pygame.K_w]:
            self.shadow.rect.y = self.rect.y - self.speed
            if self.can_move(obstacles_group):
                self.rect.y -= self.speed
                if self.rect.top < 0:
                    self.rect.top = 0
            if self.direction != 0:
                self.image = tankv1_img
            self.direction = 0
        elif pressed_button[pygame.K_a]:
            self.shadow.rect.x = self.rect.x - self.speed
            if self.can_move(obstacles_group):
                self.rect.x -= self.speed
                if self.rect.left < 0:
                    self.rect.left = 0
            if self.direction != 3:
                self.image = pygame.transform.rotate(tankv1_img, 90)
            self.direction = 3
        elif pressed_button[pygame.K_s]:
            self.shadow.rect.y = self.rect.y + self.speed
            if self.can_move(obstacles_group):
                self.rect.y += self.speed
                if self.rect.bottom > HEIGHT:
                    self.rect.bottom = HEIGHT
            if self.direction != 2:
                self.image = pygame.transform.rotate(tankv1_img, 180)
            self.direction = 2
        elif pressed_button[pygame.K_d]:
            self.shadow.rect.x = self.rect.x + self.speed
            if self.can_move(obstacles_group):
                self.rect.x += self.speed
                if self.rect.right > WIDTH:
                    self.rect.right = WIDTH
            if self.direction != 1:
                self.image = pygame.transform.rotate(tankv1_img, 270)
            self.direction = 1
        self.shadow.rect.center = self.rect.center

    def can_move(self, obstacles_group):
        if len(pygame.sprite.spritecollide(self.shadow, obstacles_group, False, None)) != 0:
            return False
        return True


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = 1
        self.direction = 0

    def update(self):
        pass

    """
    создать алгоритм перемещения противника
    
    двумерный массив расположения препятствий 
        
        """


# тип 0 - пустота.
# тип 1 - лес
# тип 2 - кирпич
# тип 3 - вода
# тип 4 - бетон
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = obstacles_list[type]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_img
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = 1
        self.direction = direction

    """
    direction:
        0 - вверх
        1- вправо
        2 - вниз
        3 - влево

        """
    def update(self):
        if self.direction == 0:
            self.rect.y -= self.speed
        elif self.direction == 1:
            self.rect.x += self.speed
        elif self.direction == 2:
            self.rect.y += self.speed
        elif self.direction == 3:
            self.rect.x -= self.speed
        if 0 > self.rect.x or self.rect.x > WIDTH or 0 > self.rect.y or self.rect.y > WIDTH:
            self.kill()






