import pygame
import math
import sys
import webbrowser
import random
from pygame import mixer



pygame.init()

BLACK = (0,0,0)

class Krekhead():
    def __init__(self):

        self.main_x = 0
        self.main_y = 0
        self.window_width = 1400
        self.window_height = 600
        self.caption = "KREKHED"
        self.img = pygame.image.load("ghost.png")
        self.credit_img = pygame.image.load("credits.png")
        self.credit_rect = pygame.Rect(-3,-40, 120, 90)
        self.img_small = pygame.transform.scale(self.img, (50,50))
        self.obstacle_cactus = pygame.image.load("cactus.png")
        self.scroll = 0
        

    def initialize(self):
        win = pygame.display.set_mode((self.window_width,self.window_height))
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(pygame.image.load("ghost.png"))
        return win
    
    def check_for_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    def create_button(self, x, y, width, height, def_color, hover_color,text, text_color, action = False):

        font  = pygame.font.Font("Slowdex.ttf", 35)
        button_rect = pygame.Rect(x,y,width,height)
        button_color = hover_color if button_rect.collidepoint(pygame.mouse.get_pos()) else def_color

        pygame.draw.rect(win, button_color, button_rect)
        pygame.draw.rect(win, BLACK, button_rect, 2 )

        button_text = font.render(text, True, text_color)
        text_rect = button_text.get_rect(center= button_rect.center)
        win.blit(button_text, text_rect)

        if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            action()

    def scroll_thingey(self):
        background  = pygame.image.load("bg.png").convert_alpha()
        bg_width = background.get_width()
        tiles = math.ceil((self.window_width / bg_width)) + 1

        for i in range(0,tiles):
            win.blit(background , (i * bg_width + self.scroll, 0))
        self.scroll -= 5
        if abs(self.scroll) > bg_width:
            self.scroll = 0
    
    def text_render(self, font, size, text, color, bg_color = None):
        f = pygame.font.Font(font, size)
        write = f.render(text,True,color, bg_color)
        return write
    

class Screens():
    def __init__(self):
        pass
        



class Krek():
    def __init__(self,main_x,main_y,x,y):

        self.x = x+main_x
        self.y = y+main_y
        self.width = 50
        self.height = 50
        self.img_small = pygame.transform.scale(pygame.image.load("ghost.png"), (50,50))
        self.color = (255,255,0)
        self.score = 0
        self.jump_height = 20
        self.jump_velocity = self.jump_height
        self.move_left = False
        self.move_right = False
        self.isJump = False
        self.steps = 6
        self.enemy_x = random.randint(900,1400)
        self.enemy_y = 560 


    def create_character(self):
        rect = pygame.Rect(self.x,self.y,self.width,self.height)
        return rect


    def draw(self,win):
        rect = self.create_character()
        pygame.draw.rect(win,self.color,rect)
        win.blit(self.img_small, rect.center)


    def move(self,x,y):
        self.x += x
        self.y += y
    
    def jump(self,gravity):
        player.y -= self.jump_velocity
        self.jump_velocity -= gravity
        if abs(self.jump_velocity) > self.jump_height:
            self.isJump = False
            self.jump_velocity = self.jump_height

    def enemy(self,win):
        enemy_rect = pygame.Rect(self.enemy_x - 6,self.enemy_y, 35,50)
        pygame.draw.rect(win, (0,0,200),enemy_rect)
    
    def isCollision(self):
        distance = math.sqrt((math.pow(self.enemy_x-self.x,2)) + (math.pow(self.enemy_y-self.y,2)))
        if distance < 35:
            return True
        else:
            return False


# DIFFERENT SCREENS

def start():
    global gameplay
    gameplay = True
    return gameplay


mixer.music.load('bg_music.mp3')
mixer.music.play(-1)


krek = Krekhead()
player = Krek(krek.main_x,krek.main_y,250,550)
win = krek.initialize()
clock  = pygame.time.Clock()
FPS = 60
run = True
gameplay  = False





while run:
    if gameplay:
        player.enemy_x -= 7
        clock.tick(FPS)
        krek.scroll_thingey()
        # win.blit(img_small, (300, 100))
        win.blit(krek.text_render('Slowdex.ttf', 25, f"SCORE : {player.score}", (0,255,0), (0,0,0)), (600,25))



        win.blit(krek.text_render('freesansbold.ttf', 25, "nigga", (0,255,0), (0,0,0)), (krek.window_width-450, krek.window_height - 400))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.move_left = True
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.move_right = True
                    elif event.key == pygame.K_SPACE:
                        player.isJump = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.move_left = False
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.move_right = False
                    elif event.key == pygame.K_SPACE:
                        pass
        
        collison = player.isCollision()
        if collison:
            sys.exit()
        if player.x > player.enemy_x:
            player.score += 1
        if player.enemy_x < -40:
            player.enemy_x = 1450       
                    


        if player.move_left and player.x > 10:
            player.move(-player.steps,0)
        elif player.move_right and player.x < krek.window_width-60:
            player.move(player.steps,0)
        if player.isJump:
            player.jump(gravity = 2)
        

        player.draw(win)
        player.enemy(win)
    else:

        win.fill((0,0,0))
        pygame.draw.rect(win, (0,0,0), krek.credit_rect)
        win.blit(pygame.transform.scale(krek.credit_img, (150,150)), (-3,-40))
        win.blit(krek.text_render("Minecraft.ttf", 170, "KREKHED", (255,255,255)), (300,175))
        krek.create_button(400,375,200,100, (0,255,0), (255,0,0), "Play", BLACK,  start)
        krek.create_button(600,375,200,100, (0,255,0), (255,0,0), "Options", BLACK,  lambda: 5+1)
        krek.create_button(800,375,200,100, (0,255,0), (255,0,0), "Quit", BLACK,  lambda: sys.exit())
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if krek.credit_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed:
                        webbrowser.open("https://github.com/DanyalAbbas")

    pygame.display.flip()

pygame.quit()
    

        




