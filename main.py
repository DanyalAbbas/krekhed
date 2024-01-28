import pygame
import math

pygame.init()

class Krekhead():
    def __init__(self):

        self.main_x = 0
        self.main_y = 0
        self.window_width = 1400
        self.window_height = 600
        self.caption = "KREKHED"

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
    
class Krek():
    def __init__(self,main_x,main_y,x,y):

        self.x = x+main_x
        self.y = y+main_y
        self.width = 50
        self.height = 50
        self.color = (255,255,0)


    def create_character(self):
        rect = pygame.Rect(self.x,self.y,self.width,self.height)
        return rect


    def draw(self,win):
        rect = self.create_character()

        pygame.draw.rect(win,self.color,rect)

    def move(self,x,y):
        self.x += x
        self.y += y
    
    def jump(self,gravity):  
        global isJump, jump_velocity, jump_height
        player.y -= jump_velocity
        jump_velocity -= gravity
        if jump_velocity < - jump_height:
            isJump = False
            jump_velocity = jump_height


krek = Krekhead()
win = krek.initialize()

background  = pygame.image.load("bg.png").convert()
bg_width = background.get_width()
tiles = math.ceil((krek.window_width / bg_width)) + 1
scroll = 0

img = pygame.image.load("ghost.png")
img_small = pygame.transform.scale(img, (50,50))

clock  = pygame.time.Clock()
FPS = 60

player = Krek(krek.main_x,krek.main_y,250,550)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Test 1', True, (0, 255, 0), (0, 0, 128))
run = True
move_left = False
move_right = False
steps = 6
isJump = False
jump_height = 20
jump_velocity = jump_height
gravity = 2



while run:
    clock.tick(FPS)
    for i in range(0,tiles):
        win.blit(background, (i * bg_width + scroll ,0))
        win.blit(img_small, (300, 100))

    # scroll background
    scroll -= 5

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    win.blit(text, (krek.window_width-450, krek.window_height - 400))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_SPACE:
                    isJump = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_SPACE:
                    pass
                


    if move_left:
        player.move(-steps,0)
    elif move_right:
        player.move(steps,0)
    if isJump:
        player.jump(gravity)
    

    player.draw(win)



    pygame.display.flip()

pygame.quit()
    

        




