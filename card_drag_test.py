import pygame
import logging

# Initialize Logging Settings
logging.basicConfig(
    format='%(asctime)s - %(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %I:%M',
    level=logging.INFO)


def main():
    # Initialize screen
    pygame.init()
    global screen
    screen = pygame.display.set_mode((700, 500))

    # Initialize background
    bg_img = pygame.image.load('board.png')
    screen.blit(bg_img, (0, 0))

    # Initialize draggable card
    card = pygame.rect.Rect(300, 300, 115, 145)
    card_dragging = False

    # Initialize font object
    font = pygame.font.SysFont('Arial', 25)

    # Main loop

    clock = pygame.time.Clock()

    running = True

    while running:

        screen.blit(bg_img, (0, 0))
        # events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if card.collidepoint(event.pos):
                        card_dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = card.x - mouse_x
                        offset_y = card.y - mouse_y
                
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    card_dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if card_dragging:
                    mouse_x, mouse_y = event.pos
                    card.x = mouse_x + offset_x
                    card.y = mouse_y + offset_y

        pygame.draw.rect(screen, (255, 0, 0), card)
        screen.blit(font.render('1234', True, (255, 255, 255)), (card.x, card.y))

        pygame.display.flip()

        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__':
    main()