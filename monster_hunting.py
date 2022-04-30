import pygame
import time
import random
import monster_list


# basic intialization
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background = pygame.image.load('./desert.jpg')
background  = pygame.transform.scale(background, (1000, 600))
pygame.display.set_caption('monster_beat')
main_clock = pygame.time.Clock()


 #load monster
Goblins = monster_list.Goblins() #哥布林
FireSpirit = monster_list.FireSpirit() #火精靈
EvilWolf = monster_list.EvilWolf() #惡狼犬
Boss = monster_list.Boss() #魔獸首領

# function for display the HP
def display_player_HP(HP, full_HP):
    pygame.draw.rect(screen, BLACK, (700, 390, 250, 20))
    pygame.draw.rect(screen, RED, (700, 390, 250*HP/full_HP, 20))
def display_player_DEF(DEF, full_HP):
    pygame.draw.rect(screen, GREEN, (700, 390, 250*DEF/full_HP, 20))

def display_enemy_HP(HP, full_HP):
    pygame.draw.rect(screen, BLACK, (50, 50, 250, 20))
    pygame.draw.rect(screen, RED, (50, 50, 250*HP/full_HP, 20))

# main function
def main():
    class player(pygame.sprite.Sprite):
        draw = random.randint(1,3) # random choose first monster
        if draw == 1:
            chosen = Goblins
        elif draw == 2:
            chosen = FireSpirit
        else:
            chosen = EvilWolf
    

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                # display the process of game
                screen.fill(WHITE)
                screen.blit(background, (0,0))
                screen.blit(player.chosen.image, player.chosen.rect)
                screen.blit(Boss.image, Boss.rect)
                display_player_HP(player.chosen.lasting_HP, player.chosen.HP)
                display_player_DEF(player.chosen.DEF, player.chosen.HP)
                display_enemy_HP(Boss.lasting_HP, Boss.HP)
                pygame.display.update()
                time.sleep(0.5)


                # fight calculating
                Boss.lasting_HP = Boss.lasting_HP-player.chosen.ATK
                if player.chosen.DEF > Boss.ATK:
                    player.chosen.DEF -= Boss.ATK
                else:
                    player.chosen.lasting_HP -= (Boss.ATK-player.chosen.DEF)
                    player.chosen.DEF = 0
                print("敵方襲擊猛烈 "+player.chosen.name+"所剩血量:"+str(player.chosen.lasting_HP)+" 護盾:"+str(player.chosen.DEF))
                
                # judge the result of the fighting
                if Boss.lasting_HP<0:
                    Boss.lasting_HP = 0
                    print("大魔王戰死 勇者獲勝")
                    pygame.quit()
                if player.chosen.lasting_HP<0:
                    player.chosen.lasting_HP = 0
                    player.chosen.alive = False
                    print(player.chosen.name+"戰死")
                    if Goblins.alive==False and FireSpirit.alive==False and EvilWolf.alive==False:
                        print("大魔王勝利 你輸了")
                        pygame.quit()

                    while 1:
                         draw = random.randint(1,3) # random choose next monster
                         if draw == 1 and Goblins.alive == True:
                            player.chosen = Goblins
                            print(player.chosen.name+"上場")
                            break
                         elif draw == 2 and FireSpirit.alive == True:
                            player.chosen = FireSpirit
                            print(player.chosen.name+"上場")
                            break
                         elif draw == 3 and EvilWolf.alive == True:
                            player.chosen = EvilWolf
                            print(player.chosen.name+"上場")
                            break
                       

if __name__ == '__main__':
    main()