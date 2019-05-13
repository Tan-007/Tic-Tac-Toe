""" VERSION 1.0.0 """
# TIC TAC TOE

try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass
	
# Importing necessary modules
import pygame, time, sys


# Check errors
# Pygame.init returns suc. process and errors in tuple
check_errors = pygame.init()
if check_errors[1] > 0:
    print('Error(s) found..Exiting')
    sys.exit(-1)
else:
    print('initialization successful..')

# Play surface
play_surface = pygame.display.set_mode((420, 520))

# Colours
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 128)
play_surface.fill(white)

# Game board
pygame.draw.line(play_surface, black, (10, 140), (410, 140), 5)
pygame.draw.line(play_surface, black, (10, 280), (410, 280), 5)
pygame.draw.line(play_surface, black, (140, 10), (140, 410), 5)
pygame.draw.line(play_surface, black, (280, 10), (280, 410), 5)

# Player1 symbol
P1font = pygame.font.SysFont('monaco', 24, True)
P1surface = P1font.render('Player 1:', True, blue)
P1rect = P1surface.get_rect()
P1rect.bottomleft = (20, 480)
play_surface.blit(P1surface, P1rect)
pygame.draw.circle(play_surface, blue, (140, 470), 20, 3)

# Player2 symbol
P2font = pygame.font.SysFont('monaco', 24, True)
P2surface = P2font.render('Player 2:',True, red)
P2rect = P2surface.get_rect()
P2rect.bottomright = (330, 480)
play_surface.blit(P2surface, P2rect)
pygame.draw.line(play_surface, red, (350, 450), (380, 480), 4)
pygame.draw.line(play_surface, red, (380, 450), (350, 480), 4)

pygame.display.flip()

# Player1 Takes the turn first
player1 = True

#Rectangle initial
in_rect1 = 'NULL'
in_rect2 = 'NULL'
in_rect3 = 'NULL'
in_rect4 = 'NULL'
in_rect5 = 'NULL'
in_rect6 = 'NULL'
in_rect7 = 'NULL'
in_rect8 = 'NULL'
in_rect9 = 'NULL'

# Dimensions of each circle
circle1 = (70, 70)
circle2 = (210, 70)
circle3 = (340, 70)
circle4 = (70, 210)
circle5 = (210, 210)
circle6 = (350, 210)
circle7 = (70, 340)
circle8 = (210, 340)
circle9 = (340, 340)

# Dimensions for Crosses
cross1 = ((30, 30), (110, 110), (110, 30), (30, 110))
cross2 = ((170, 30), (250, 110), (250, 30), (170, 110))
cross3 = ((310, 30), (390, 110), (390, 30), (310, 110))
cross4 = ((30, 170), (110, 250), (110, 170), (30, 250))
cross5 = ((170, 170), (250, 250), (250, 170), (170, 250))
cross6 = ((310, 170), (390, 250), (390, 170), (310, 250))
cross7 = ((30, 310), (110, 390), (110, 310), (30, 390))
cross8 = ((170, 310), (250, 390), (250, 310), (170, 390))
cross9 = ((310, 310), (390, 390), (390, 310), (310, 390))

# Rectangles
rect1 = pygame.Rect(10, 10, 130, 130)
rect2 = pygame.Rect(150, 10, 130, 130)
rect3 = pygame.Rect(290, 10, 130, 130)
rect4 = pygame.Rect(10, 150, 130, 130)
rect5 = pygame.Rect(150, 150, 130, 130)
rect6 = pygame.Rect(290, 150, 130, 130)
rect7 = pygame.Rect(10, 290, 130, 130)
rect8 = pygame.Rect(150, 290, 130, 130)
rect9 = pygame.Rect(290, 290, 130, 130)
list_rect = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9]

# Function to draw circle
def draw_circle(pos):
    pygame.draw.circle(play_surface, blue, (pos), 50, 5)
    global player1
    player1 = False
    return 'CIRCLE'

# Function to draw Cross
def draw_cross(pos1, pos2, pos3, pos4):
    pygame.draw.line(play_surface, red, pos1, pos2, 5)
    pygame.draw.line(play_surface, red, pos3, pos4, 5)
    global player1
    player1 = True
    return 'CROSS'

# Player1 Wins
def player1_wins():
    play_surface.fill(white)
    GOfont = pygame.font.SysFont('comicsansms', 48, True)
    GOsurface = GOfont.render('Player 1 Wins!', True, blue)
    GOrect = GOsurface.get_rect()
    GOrect.midtop = (220, 150)
    play_surface.blit(GOsurface, GOrect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Player 2 wins
def player2_wins():
    play_surface.fill(white)
    GOfont = pygame.font.SysFont('comicsansms', 48, True)
    GOsurface = GOfont.render('Player 2 Wins!', True, red)
    GOrect = GOsurface.get_rect()
    GOrect.midtop = (220, 150)
    play_surface.blit(GOsurface, GOrect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Game draw
def game_draw():
    play_surface.fill(white)
    GOfont = pygame.font.SysFont('comicsansms', 76, True)
    GOsurface = GOfont.render('Game Draw!', True, black)
    GOrect = GOsurface.get_rect()
    GOrect.midtop = (220, 150)
    play_surface.blit(GOsurface, GOrect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Function to CHECK WIN
def check_win():
    if in_rect1 == 'CIRCLE' and in_rect2 == 'CIRCLE' and in_rect3 == 'CIRCLE':
        player1_wins()
    elif in_rect4 == 'CIRCLE' and in_rect5 == 'CIRCLE' and in_rect6 == 'CIRCLE':
        player1_wins()
    elif in_rect7 == 'CIRCLE' and in_rect8 == 'CIRCLE' and in_rect9 == 'CIRCLE':
        player1_wins()
    elif in_rect1 == 'CIRCLE' and in_rect4 == 'CIRCLE' and in_rect7 == 'CIRCLE':
        player1_wins()
    elif in_rect2 == 'CIRCLE' and in_rect5 == 'CIRCLE' and in_rect8 == 'CIRCLE':
        player1_wins()
    elif in_rect3 == 'CIRCLE' and in_rect6 == 'CIRCLE' and in_rect9 == 'CIRCLE':
        player1_wins()
    elif in_rect1 == 'CIRCLE' and in_rect5 == 'CIRCLE' and in_rect9 == 'CIRCLE':
        player1_wins()
    elif in_rect3 == 'CIRCLE' and in_rect5 == 'CIRCLE' and in_rect7 == 'CIRCLE':
        player1_wins()

    elif in_rect1 == 'CROSS' and in_rect2 == 'CROSS' and in_rect3 == 'CROSS':
        player2_wins()
    elif in_rect4 == 'CROSS' and in_rect5 == 'CROSS' and in_rect6 == 'CROSS':
        player2_wins()
    elif in_rect7 == 'CROSS' and in_rect8 == 'CROSS' and in_rect9 == 'CROSS':
        player2_wins()
    elif in_rect1 == 'CROSS' and in_rect4 == 'CROSS' and in_rect7 == 'CROSS':
        player2_wins()
    elif in_rect2 == 'CROSS' and in_rect5 == 'CROSS' and in_rect8 == 'CROSS':
        player2_wins()
    elif in_rect3 == 'CROSS' and in_rect6 == 'CROSS' and in_rect9 == 'CROSS':
        player2_wins()
    elif in_rect1 == 'CROSS' and in_rect5 == 'CROSS' and in_rect9 == 'CROSS':
        player2_wins()
    elif in_rect3 == 'CROSS' and in_rect5 == 'CROSS' and in_rect7 == 'CROSS':
        player2_wins()
    elif in_rect1 is not 'NULL' and in_rect2 is not 'NULL' and in_rect3 is not 'NULL' \
            and in_rect4 is not 'NULL' and in_rect5 is not 'NULL' and in_rect6 is not 'NULL' \
            and in_rect7 is not 'NULL' and in_rect8 is not 'NULL' and in_rect9 is not 'NULL':
        game_draw()

# MAIN LOGIC
def main():

    global in_rect1, in_rect2, in_rect3, in_rect4, in_rect5, in_rect6, in_rect7, in_rect8, in_rect9

    while True:
        i = 0 # decides the rectangle pointed out by the user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pos = pygame.mouse.get_pos()
        (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()
        for rect in list_rect[0:9]:
            i += 1
            if rect.collidepoint(pos) & pressed1 :
                if in_rect1 is 'NULL' and i == 1:
                    in_rect1 = draw_cross(cross1[0], cross1[1], cross1[2], cross1[3]) if player1 == False else draw_circle(circle1)
                if in_rect2 is 'NULL' and i == 2:
                    in_rect2 = draw_cross(cross2[0], cross2[1], cross2[2], cross2[3]) if player1 == False else draw_circle(circle2)
                if in_rect3 is 'NULL' and i == 3:
                    in_rect3 = draw_cross(cross3[0], cross3[1], cross3[2], cross3[3]) if player1 == False else draw_circle(circle3)
                if in_rect4 is 'NULL' and i == 4:
                    in_rect4 = draw_cross(cross4[0], cross4[1], cross4[2], cross4[3]) if player1 == False else draw_circle(circle4)
                if in_rect5 is 'NULL' and i == 5:
                    in_rect5 = draw_cross(cross5[0], cross5[1], cross5[2], cross5[3]) if player1 == False else draw_circle(circle5)
                if in_rect6 is 'NULL' and i == 6:
                    in_rect6 = draw_cross(cross6[0], cross6[1], cross6[2], cross6[3]) if player1 == False else draw_circle(circle6)
                if in_rect7 is 'NULL' and i == 7:
                    in_rect7 = draw_cross(cross7[0], cross7[1], cross7[2], cross7[3]) if player1 == False else draw_circle(circle7)
                if in_rect8 is 'NULL' and i == 8:
                    in_rect8 = draw_cross(cross8[0], cross8[1], cross8[2], cross8[3]) if player1 == False else draw_circle(circle8)
                if in_rect9 is 'NULL' and i == 9:
                    in_rect9 = draw_cross(cross9[0], cross9[1], cross9[2], cross9[3]) if player1 == False else draw_circle(circle9)

        check_win()
        pygame.display.flip()

if __name__ == '__main__':
    main()
