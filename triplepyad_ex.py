import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Triple Pyad')

WHITE = (255, 255, 255)

FPS = 60
VEL = 5
CARD_SIZE = (175, 225)

CARD = pygame.image.load(os.path.join('Assets', 'card.png'))
CARD = pygame.transform.rotate(pygame.transform.scale(CARD, CARD_SIZE), 90)

def draw_window(card):
    WIN.fill((WHITE))
    WIN.blit(CARD, (card.x, card.y))
    pygame.display.update()

def card_movement(keys, card):
    if keys[pygame.K_a]: # LEFT
        card.x -= VEL
    if keys[pygame.K_d]: # RIGHT
        card.x += VEL
    if keys[pygame.K_w]: # UP
        card.y -= VEL
    if keys[pygame.K_s]: # DOWN
        card.y += VEL

def main():
    active_card = pygame.Rect(100, 300, 175, 225)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        card_movement(keys_pressed, active_card)
        draw_window(active_card)

    pygame.quit()

if __name__ == "__main__":
    main()