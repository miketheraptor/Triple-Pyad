import pygame
from models import *
from engine import *


pygame.init()
bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption('Triple Pyad')

def render_game(window):
    window.fill((255, 255, 255))

# game_engine = TriplePyadEngine()

run = True
while run:
    render_game(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

