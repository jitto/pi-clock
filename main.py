#!/usr/bin/python

import pygame, sys, os, time
from pygame.locals import *

os.environ["SDL_FBDEV"] = "/dev/fb1"
#os.environ["SDL_MOUSEDRV"] = "TSLIB"
#os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"

pygame.init()

screen_width = 480
screen_height = 320

# set up the window
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption('OpenDisplayCase TFTTestScreen')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
CYAN  = (  0, 255, 255)
MAGENTA=(255,   0, 255)
YELLOW =(255, 255,   0)
GREY =(100, 100,   100)
 
# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

# Background
rect_box_width = screen_width/8
box = pygame.draw.rect(background, YELLOW, (rect_box_width, 0, rect_box_width, screen_height))
box = pygame.draw.rect(background, CYAN, ((rect_box_width*2), 0, rect_box_width, screen_height))
box = pygame.draw.rect(background, GREEN, ((rect_box_width*3), 0, rect_box_width, screen_height))
box = pygame.draw.rect(background, MAGENTA, ((rect_box_width*4), 0, rect_box_width, screen_height))
box = pygame.draw.rect(background, RED, ((rect_box_width*5), 0, rect_box_width, screen_height))
box = pygame.draw.rect(background, BLUE, ((rect_box_width*6), 0, rect_box_width, screen_height))
box = pygame.draw.rect(background, BLACK, ((rect_box_width*7), 0, rect_box_width, screen_height))

# Footer
rect_box_mini_heigt = 45
box = pygame.draw.rect(background, BLACK, (0, (screen_height-rect_box_mini_heigt), rect_box_width, rect_box_mini_heigt))
box = pygame.draw.rect(background, BLUE, ((rect_box_width*1), (screen_height-rect_box_mini_heigt), rect_box_width, rect_box_mini_heigt))
box = pygame.draw.rect(background, RED, ((rect_box_width*2), (screen_height-rect_box_mini_heigt), rect_box_width, rect_box_mini_heigt))
box = pygame.draw.rect(background, MAGENTA, ((rect_box_width*3), (screen_height-rect_box_mini_heigt), rect_box_width, rect_box_mini_heigt))
box = pygame.draw.rect(background, GREEN, ((rect_box_width*4), (screen_height-rect_box_mini_heigt), rect_box_width, rect_box_mini_heigt))
box = pygame.draw.rect(background, CYAN, ((rect_box_width*5), (screen_height-rect_box_mini_heigt), rect_box_width, rect_box_mini_heigt))
box = pygame.draw.rect(background, YELLOW, ((rect_box_width*6), (screen_height-rect_box_mini_heigt), rect_box_width, rect_box_mini_heigt))
box = pygame.draw.rect(background, WHITE, ((rect_box_width*7), (screen_height-rect_box_mini_heigt), rect_box_width, rect_box_mini_heigt))

# Header
GRADIENT_HEIGHT = 20
for i in range(screen_width):
    pygame.draw.line(background, GREY, ((3*i), 0), ((3*i), 0 + GRADIENT_HEIGHT))

# Text BG
rect_height = 60
rect_box = pygame.Rect((0,background.get_height()-rect_height-20), (background.get_width(),rect_height))
pygame.draw.rect(background, (WHITE), rect_box)     

# Display some text
font = pygame.font.Font(None, 42)
text = font.render("OpenDisplayCase", 1, (BLACK))
textpos = text.get_rect(centerx=background.get_width()/2,centery=background.get_height()-rect_height-2)
background.blit(text, textpos)

font1 = pygame.font.Font(None, 28)
text1 = font1.render("TFT Test Screen", 1, (GREY))
textpos1 = text1.get_rect(centerx=background.get_width()/2,centery=background.get_height()-32)
background.blit(text1, textpos1)

screen.blit(background, (0, 0))
pygame.display.flip()

running = True
# run the game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            running = False 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Pos: %sx%s\n" % pygame.mouse.get_pos())
            if textpos.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
                running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
    pygame.display.update()

