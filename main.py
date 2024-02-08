# Name : Danyal Abbas
# Roll no : 78359
# Email: gamingindustry9@gmail.com
# ----------------------------------- # 

# Importing different libraries we will need

import pygame # For the main GUI based program 
import math # For Collision management by using distance formula
import sys # For exiting the program
import webbrowser # To open any link in the browser
import random # For randomly generating the enemies
from pygame import mixer # For music and sound effects


BLACK = (0, 0, 0)

# Initializing the pygame and mixer library
pygame.init()
mixer.init()

# making a Class for the window and different things related to it 
class Krekhead():
    def __init__(self):
        # initializing values of width, height, caption, images of window
        self.main_x = 0
        self.main_y = 0
        self.window_width = 1400
        self.window_height = 600
        self.caption = "KREKHED"
        self.theme = [(0,0,0)]
        self.img = pygame.image.load("Assets/ghost.png")
        self.sun = pygame.transform.scale(pygame.image.load("Assets/sun.png"), (100, 100))
        self.credit_img = pygame.image.load("Assets/credits.png")
        self.credit_rect = pygame.Rect(-3, -40, 120, 90)
        self.img_small = pygame.transform.scale(self.img, (50, 50))
        self.scroll = 0
        self.click_sound = mixer.Sound("Assets/click.mp3") 

    # Implementing the values and giving the window its width, height, image and icon
    def initialize(self):
        win = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(pygame.image.load("Assets/ghost.png"))
        return win

    # Creating a method for button, as we will be adding a lot of  buttons in the game
    def create_button(self, x, y, width, height, def_color,textfont, hover_color, text, text_color, action=False):
        font = pygame.font.Font(textfont, 35)
        button_rect = pygame.Rect(x, y, width, height)
        button_color = hover_color if button_rect.collidepoint(pygame.mouse.get_pos()) else def_color

        pygame.draw.rect(win, button_color, button_rect)
        pygame.draw.rect(win, BLACK, button_rect, 2)

        button_text = font.render(text, True, text_color)
        text_rect = button_text.get_rect(center=button_rect.center)
        win.blit(button_text, text_rect)

        if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            self.click_sound.play()
            action()
    
    # Method to handle background scrolling
    def scroll_thingey(self):
        background = pygame.image.load("Assets/bg.png").convert_alpha()
        bg_width = background.get_width()
        tiles = math.ceil((self.window_width / bg_width)) + 1

        for i in range(0, tiles):
            win.blit(background, (i * bg_width + self.scroll, 0))
        self.scroll -= 5
        if abs(self.scroll) > bg_width:
            self.scroll = 0

    # Method to render text
    def text_render(self, font, size, text, color, bg_color=None):
        f = pygame.font.Font(font, size)
        write = f.render(text, True, color, bg_color)
        return write

# Making another Class for the different screens in the game (Gameloop, Main Menu, Death screen, etc)
class Screens():
    def __init__(self):
        self.main_menu = True
        self.gameplay = False
        self.died = False
        self.options = False
        self.died_music = mixer.Sound("Assets/game_over.wav")
        self.colors_rgb = [
        (255, 0, 0),     # Red
        (0, 255, 0),     # Green
        (0, 0, 255),     # Blue
        (255, 255, 0),   # Yellow
        (255, 0, 255),   # Magenta
        (0, 255, 255),   # Cyan
        (128, 0, 0),     # Maroon
        (0, 128, 0),     # Olive
        (0, 0, 128),     # Navy
        (128, 128, 128),  # Gray
        (255, 165, 0),   # Orange
        (0, 128, 128),   # Teal
        (128, 0, 128),   # Purple
        (128, 128, 0),   # Olive
        (70, 130, 180),   # Steel Blue
        (255, 99, 71),    # Tomato
        (0, 139, 139),    # Dark Cyan
        (218, 112, 214),  # Orchid
        (255, 192, 203),  # Pink
        (173, 216, 230),  # Light Blue
        (240, 128, 128),  # Light Coral
        (152, 251, 152),  # Pale Green
        (255, 215, 0),    # Gold
        (255, 20, 147),   # Deep Pink
        (0, 255, 127),    # Spring Green
        (255, 69, 0),     # Red-Orange
        (0, 250, 154),    # Medium Spring Green
        (128, 0, 0),      # Dark Red
        (255, 218, 185),  # Peach
        (210, 105, 30),   # Chocolate
        (255, 250, 205),  # LemonChiffon
        (255, 192, 203),  # Pink
        (0, 191, 255),    # Deep Sky Blue
        (138, 43, 226),   # Blue Violet
        (255, 228, 196),  # Bisque
        (255, 140, 0),    # Dark Orange
        (0, 0, 139),      # Dark Blue
        (32, 178, 170),   # Light Sea Green
        (186, 85, 211),   # Medium Orchid
        (255, 182, 193),  # Light Pink
        (255, 255, 240),  # Ivory
        (0, 128, 0)       # Green
]


    # Different button functions that will be called when certain buttons are pressed
    def start_btn_func(self):
        self.died = False
        self.options = False
        self.main_menu = False
        self.gameplay = True
        return self.gameplay
    def menu_btn_func(self):
        self.main_menu = True
        player.score = 0
        player.x = 250
        player.move_right = False
        player.move_right = False
        player.isJump = False
        player.obstacles.clear()
        self.died = False
        self.gameplay = False
        self.options = False
        return self.main_menu
    def restart_btn_func(self):
        player.score = 0
        player.x = 250
        player.move_right = False
        player.move_right = False
        player.isJump = False
        player.obstacles.clear()
        self.died = False
        self.options = False
        self.main_menu = False
        self.gameplay = True   
        return screen.gameplay
    def option_btn_func(self):
        self.options = True
        self.main_menu = False
        self.died = False
        self.gameplay = False
        return self.options


      
    # The screen that will be shown when the player collides with any obstacle
    def DiedScreen(self):
        win.fill(krek.theme[-1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        win.blit(krek.text_render("Assets/Minecraft.ttf", 100, "YOU DIED", (255,255,255)), (450, 150))
        win.blit(krek.text_render("Assets/Slowdex.ttf", 50, f"Score : {player.score}", (255,255,255)), (585, 250))
        krek.create_button(465, 340, 250, 75, (255,255,255), "Assets/krek.ttf", (0,200,0), "Restart", (0,0,0), self.restart_btn_func)
        krek.create_button(715, 340, 250, 75, (255,255,255), "Assets/krek.ttf", (0,200,0), "Quit", (0,0,0), lambda : sys.exit())
        krek.create_button(568, 415, 300, 75, (255,255,255), "Assets/krek.ttf", (0,200,0), "Main Menu", (0,0,0),  self.menu_btn_func)

    # The Main Menu screen that will shown when the user launches the game
    def MainMenu(self):
        win.fill(krek.theme[-1])
        pygame.draw.rect(win, krek.theme[-1], krek.credit_rect)
        win.blit(pygame.transform.scale(krek.credit_img, (150, 150)), (-3, -40))
        win.blit(krek.text_render("Assets/Minecraft.ttf", 170, "KREKHED", (255, 255, 255)), (300, 175))
        krek.create_button(400, 375, 200, 100, (0, 255, 0), "Assets/Slowdex.ttf" ,(255, 0, 0), "Play", BLACK, self.start_btn_func)
        krek.create_button(600, 375, 200, 100, (0, 255, 0), "Assets/Slowdex.ttf" ,(255, 0, 0), "Options", BLACK, self.option_btn_func)
        krek.create_button(800, 375, 200, 100, (0, 255, 0), "Assets/Slowdex.ttf" ,(255, 0, 0), "Quit", BLACK, lambda: sys.exit())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if krek.credit_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed:
                    webbrowser.open("https://github.com/DanyalAbbas")
    
    def OptionsScreen(self):
        win.fill(krek.theme[-1])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        krek.create_button(30, 10, 100, 50, krek.theme[-1], "Assets/Stella.otf" ,(0, 200, 0), "< Back", (255,255,255), self.menu_btn_func)
        win.blit(krek.text_render("Assets/Stella.otf", 50,"Choose your colour", (255,255,255)), (450+120,65))
        for pos,i in enumerate(self.colors_rgb):
            krek.create_button(450+120+(pos*25) if pos <= 10 else (450+(-155)+(pos*25) if pos > 10 and pos <=20 else (450+(-405)+(pos*25) if pos > 20 and pos <=30 else (1+2))), 120 if pos <= 10 else (145 if pos > 10 and pos <= 20 else (170 if pos > 20 and pos <= 30 else(5000))), 25, 25, i ,"Assets/Stella.otf" , (255,255,255),"",(0,0,0) ,lambda: player.color.append(i))
        win.blit(krek.text_render("Assets/Stella.otf", 50,"Choose the colour theme of the game", (255,255,255)), (450,250))
        for pos,i in enumerate(self.colors_rgb):
            krek.create_button(450+120+(pos*25) if pos <= 10 else (450+(-155)+(pos*25) if pos > 10 and pos <=20 else (450+(-405)+(pos*25) if pos > 20 and pos <=30 else (1+2))), 310 if pos <= 10 else (335 if pos > 10 and pos <= 20 else (360 if pos > 20 and pos <= 30 else(5000))), 25, 25, i ,"Assets/Stella.otf" , (255,255,255),"",(0,0,0) ,lambda: krek.theme.append(i))
        



    # The screen that will be when the user presses "Play" Button
    def GameLoop(self):
        player.score += 0.1
        player.score = round(player.score, 1)
        if player.score >= 200:
            player.move_obstacles(15)
        else:
            player.move_obstacles()
        clock.tick(FPS)
        krek.scroll_thingey()
        win.blit(krek.sun.convert_alpha(), (100, 50))
        win.blit(krek.text_render('Assets/Slowdex.ttf', 25, f"SCORE : {player.score}", (0, 0, 0)), (600, 5))

        player.draw(win)
        player.draw_obstacles(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

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

        if player.is_collision():
            screen.gameplay = False
            screen.main_menu = False
            screen.died_music.play()
            screen.died = True

        if player.move_left and player.x > 10:
            player.move(-player.steps, 0)
        elif player.move_right and player.x < krek.window_width - 60:
            player.move(player.steps, 0)
        if player.isJump:
            mixer.music.load("Assets/jump1.mp3")
            mixer.music.play()
            player.jump()

        if random.randint(0, 320) < 5:
            player.obstacles.append(player.create_obstacle())

        player.obstacles = [obstacle for obstacle in player.obstacles if obstacle.x > -40]
# Making a Class for the player and enemy and everything to do with their movements, bliting, creation etc
class Krek():
    def __init__(self, main_x, main_y, x, y):
        self.x = x + main_x
        self.y = y + main_y
        self.width = 50
        self.height = 50
        self.color = [(200,0,0)]
        self.score = 0
        self.jump_height = 20
        self.gravity = 2
        self.jump_velocity = self.jump_height
        self.move_left = False
        self.move_right = False
        self.isJump = False
        self.steps = 6
        self.obstacles = []
        

    def create_character(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return rect

    def draw(self, win):
        rect = self.create_character()
        pygame.draw.rect(win, self.color[-1], rect)

    def move(self, x, y):
        self.x += x
        self.y += y

    def jump(self):
        self.y -= self.jump_velocity
        self.jump_velocity -= self.gravity
        if abs(self.jump_velocity) > self.jump_height:
            self.isJump = False
            self.jump_velocity = self.jump_height

    def create_obstacle(self):
        x = random.randint(1400, 2000)
        y = 560
        obstacle_rect = pygame.Rect(x, y, 35, 60)
        return obstacle_rect

    def move_obstacles(self, value = 10):
        for i in self.obstacles:
            i.x -= value

    def draw_obstacles(self, win):
        for i in self.obstacles:
            pygame.draw.rect(win, (0, 0, 200), i)

    def is_collision(self):
        for i in self.obstacles:
            distance = math.sqrt((math.pow(i.x - self.x, 2)) + (math.pow(i.y - self.y, 2)))
            if abs(distance) < 40:
                return True
        return False




# Creating instances for the different Classes
krek = Krekhead()
player = Krek(krek.main_x, krek.main_y, 250, 550)
screen = Screens()
win = krek.initialize()
clock = pygame.time.Clock()
FPS = 60

# The Main window loop for the program to keep running
run = True
while run:
    if screen.options:
        screen.OptionsScreen()
    elif screen.gameplay:
        screen.GameLoop()
    elif screen.main_menu:
        screen.MainMenu()  
    elif screen.died:
        screen.DiedScreen()
    

    """ for updating the screen after one iteration so that the
        changes that occur in the iteration are shown on the screen
    """
    pygame.display.flip()  

""" for closing the program when all the tasks are done, and all the conditions
    are met."""
pygame.quit()
