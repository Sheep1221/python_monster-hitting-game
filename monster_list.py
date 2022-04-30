import pygame

# announce object of monster
class Goblins(pygame.sprite.Sprite):  
    def __init__(self):
        super().__init__()
        self.name = '哥布林'
        self.raw_image = pygame.image.load('./Goblins.png')
        self.image = pygame.transform.scale(self.raw_image, (250, 250))
        self.rect   = self.image.get_rect() #return position
        self.rect.topleft = (400, 300)  #set position
        self.HP = 40
        self.lasting_HP = self.HP
        self.ATK = 15
        self.DEF = 0
        self.alive = True

class FireSpirit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = '火精靈'
        self.raw_image = pygame.image.load('./FireSpirit.png')
        self.image = pygame.transform.scale(self.raw_image, (250, 250))
        self.rect   = self.image.get_rect() #return position
        self.rect.topleft = (400, 300)  #set position
        self.HP = 80
        self.lasting_HP = self.HP
        self.ATK = 15
        self.DEF = 35
        self.alive = True

class EvilWolf(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = '惡狼犬'
        self.raw_image = pygame.image.load('./EvilWolf.png')
        self.image = pygame.transform.scale(self.raw_image, (250, 250))
        self.rect   = self.image.get_rect() #return position
        self.rect.topleft = (400, 300)  #set position
        self.HP = 50
        self.lasting_HP = self.HP
        self.ATK = 20
        self.DEF = 15
        self.alive = True

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = '大魔王'
        self.raw_image = pygame.image.load('./Boss.png')
        self.image = pygame.transform.scale(self.raw_image, (250, 250))
        self.rect   = self.image.get_rect() #return position
        self.rect.topleft = (400, 20)  #set position
        self.HP = 220
        self.lasting_HP = self.HP
        self.ATK = 30
        self.DEF = 0