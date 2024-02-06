import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

BLACK, WHITE, GRAY, HOVER_COLOR = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)
font = pygame.font.Font("Slowdex.ttf", 25)
def create_button(x, y, width, height, text, default_color, hover_color, text_color, action):
    button_rect = pygame.Rect(x, y, width, height)
    button_color = hover_color if button_rect.collidepoint(pygame.mouse.get_pos()) else default_color

    pygame.draw.rect(screen, button_color, button_rect)
    pygame.draw.rect(screen, BLACK, button_rect, 2)

    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        action()
isJump = False
jumpCount = 10

run = True
colour = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (128, 0, 0),    # Maroon
    (0, 128, 0),    # Olive
    (0, 0, 128),    # Navy
    (128, 128, 128) # Gray
]
l = []
while run:
  screen.fill((0,0,0))
  for pos,i in enumerate(colour):
      create_button(120+(pos*25), 120, 25, 25, "" ,i , (255,255,255), (0,0,0), lambda: l.append(i))
  
  if len(l):
      screen.fill(l[0])
  create_button(250,250,50,50,"touch me", (0,200,0), (0,175,0), (255,255,255), lambda : l.append((0,200,0)))

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False

  pygame.display.flip()
pygame.quit()


#     keys = pygame.key.get_pressed()
    
#     if keys[pygame.K_LEFT] and x > vel: 
#         x -= vel

#     if keys[pygame.K_RIGHT] and x < 500 - vel - width:  
#         x += vel
        
#     if not(isJump): 
#         if keys[pygame.K_UP] and y > vel:
#             y -= vel

#         if keys[pygame.K_DOWN] and y < 500 - height - vel:
#             y += vel

#         if keys[pygame.K_SPACE]:
#             isJump = True
#     else:
#         if jumpCount >= -10:
#             y -= (jumpCount * abs(jumpCount)) * 0.5
#             jumpCount -= 1
#         else: 
#             jumpCount = 10
#             isJump = False
    
#     win.fill((0,0,0))
#     pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
#     pygame.display.update() 
    
# pygame.quit()





# import pygame
# import sys

# pygame.init()

# BLACK, WHITE, GRAY, HOVER_COLOR = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)
# screen_width, screen_height = 400, 300
# screen = pygame.display.set_mode((screen_width, screen_height))
# font = pygame.font.Font("Slowdex.ttf", 25)

# def create_button(x, y, width, height, text, default_color, hover_color, text_color, action):
#     button_rect = pygame.Rect(x, y, width, height)
#     button_color = hover_color if button_rect.collidepoint(pygame.mouse.get_pos()) else default_color

#     pygame.draw.rect(screen, button_color, button_rect)
#     pygame.draw.rect(screen, BLACK, button_rect, 2)

#     button_text = font.render(text, True, text_color)
#     text_rect = button_text.get_rect(center=button_rect.center)
#     screen.blit(button_text, text_rect)

#     if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
#         action()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.fill(WHITE)
#     create_button(50, 50, 100, 50, "Start", GRAY, HOVER_COLOR, BLACK, lambda: print("Game started!"))
#     create_button(150, 50, 100, 50, "Options", GRAY, HOVER_COLOR, BLACK, lambda: print("Options menu!"))
#     create_button(250, 50, 100, 50, "Quit", GRAY, HOVER_COLOR, BLACK, lambda: sys.exit())

#     pygame.display.flip()


# import pygame
# import webbrowser

# pygame.init()

# # Define colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Initialize Pygame window
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Clickable Link")

# # Define font and text
# font = pygame.font.Font(None, 36)
# text = font.render("Click here to open GitHub", True, BLACK)
# text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

# # Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if text_rect.collidepoint(event.pos):
#                 # Open the URL in a web browser when clicked
#                 webbrowser.open("https://github.com/DanyalAbbas")

#     # Clear the screen
#     screen.fill(WHITE)

#     # Draw the text
#     screen.blit(text, text_rect.topleft)

#     # Update the display
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()

# import pygame

# win = pygame.display.set_mode((500,500))
# background  = pygame.image.load("bg.png").convert()
# bg_width = background.get_width()

# print(bg_width)



# import pygame

# pygame.init()

# #define screen size
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# #create game window
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Masks")

# #define colours
# BG = (0, 0, 0)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# WHITE = (255, 255, 255)

# #hide mouse cursor
# pygame.mouse.set_visible(False)

# #create soldier
# soldier = pygame.image.load("cactus.png").convert_alpha()
# soldier_rect = soldier.get_rect()
# soldier_mask = pygame.mask.from_surface(soldier)
# mask_image = soldier_mask.to_surface()

# #create bullet and mask
# bullet = pygame.Surface((10, 10))
# bullet.fill(RED)
# bullet_mask = pygame.mask.from_surface(bullet)

# #game loop
# run = True
# while run:

#   #get mouse coordinates
#   pos = pygame.mouse.get_pos()

#   #update background
#   screen.fill(BG)

#   #check mask overlap
#   if soldier_mask.overlap(bullet_mask, (pos[0], pos[1])):
#     col = RED
#   else:
#     col = GREEN

#   #draw mask image
#   screen.blit(mask_image, (0, 0))

#   #draw rectangle
#   bullet.fill(col)
#   screen.blit(bullet, pos)

#   #event handler
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       run = False

#   #update display
#   pygame.display.flip()

# pygame.quit()