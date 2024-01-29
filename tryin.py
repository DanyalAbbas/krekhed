# import pygame
# pygame.init()

# win = pygame.display.set_mode((500,500))
# pygame.display.set_caption("First Game")

# x = 50
# y = 50
# width = 40
# height = 60
# vel = 5

# isJump = False
# jumpCount = 10

# run = True

# while run:
#     pygame.time.delay(100)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

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





import pygame
import sys

pygame.init()

BLACK, WHITE, GRAY, HOVER_COLOR = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0)
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    create_button(50, 50, 100, 50, "Start", GRAY, HOVER_COLOR, BLACK, lambda: print("Game started!"))
    create_button(150, 50, 100, 50, "Options", GRAY, HOVER_COLOR, BLACK, lambda: print("Options menu!"))
    create_button(250, 50, 100, 50, "Quit", GRAY, HOVER_COLOR, BLACK, lambda: sys.exit())

    pygame.display.flip()

