import pygame

class Card(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('card.png')
        self.rect = self.image.get_rect()
        self.dragging = False

    def update(self):
        pass

def main():

    # Initialize screen
    
    pygame.init()
    global screen
    screen = pygame.display.set_mode((700, 500))
    
    # Initialize background
    bg_img = pygame.image.load('board.png')
    
    # Initialize a card
    card = Card()
    card_group = pygame.sprite.Group()
    card_group.add(card)

    card2 = Card()
    card_group.add(card2)
    card2.rect.centerx = 200

    # Event loop
    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for card in card_group:
                    if event.button == 1:
                        if card.rect.collidepoint(event.pos):
                            card.dragging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = card.rect.centerx - mouse_x
                            offset_y = card.rect.centery - mouse_y
                
            elif event.type == pygame.MOUSEBUTTONUP:
                for card in card_group:
                    if event.button == 1:
                        card.dragging = False

            elif event.type == pygame.MOUSEMOTION:
                for card in card_group:
                    if card.dragging:
                        mouse_x, mouse_y = event.pos
                        card.rect.centerx = mouse_x + offset_x
                        card.rect.centery = mouse_y + offset_y

        pygame.display.flip()
        screen.blit(bg_img, (0, 0))
        card_group.draw(screen)
        card_group.update()

        
        
        clock.tick(60)

if __name__ == '__main__':
    main()



        