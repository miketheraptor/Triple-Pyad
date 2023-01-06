VERSION = '0.1'
RULESET = 'RANDOM'
PLAYER_COLOR = (0, 0, 255) # Blue
COMPUTER_COLOR = (255, 0, 0) # Red


import pygame
from pygame.locals import *
import logging
import csv


# Initialize Logging Settings
logging.basicConfig(
    format='%(asctime)s - %(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %I:%M',
    level=logging.INFO)


class GameBoard:
    '''
    Creates a GameBoard object.
    GameBoard grid position keys are as follows:
            [0][0] [0][1] [0][2]
            [1][0] [1][1] [1][2]
            [2][0] [2][1] [2][2]
    '''
    grid = None

    def __init__(self):

        self.grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def add(self, card, x_pos, y_pos):
        '''
        Add card to position
        '''
        self.grid[y_pos][x_pos] = card
        logging.info(f'Placed {card.name} on {y_pos}, {x_pos}')

class Player:
    '''
    Creates a Player object and associated
    deck and hand objects.
    '''
    deck = None
    hand = None
    player_type = None # Player or Computer

    def __init__(self, player_type):
        self.deck = Deck(player_type) # Pass 'player_type' to Deck object so it knows its owner
        self.hand = Hand()
        self.player_type = player_type # Player or Computer

    def play(self):
        pass

class Card:
    '''
    Creates a Card object with name and ranks.
    Ranks are entered as a tuple (n, e, s, w).
    '''
    name = None
    rank_n = None
    rank_e = None
    rank_s = None
    rank_w = None
    player_type = None

    def __init__(self, name, player_type, *args):
        ranks = args[0]

        self.name = name
        self.player_type = player_type # Who owns card - Player or Computer
        self.rank_n = ranks[0]
        self.rank_e = ranks[1]
        self.rank_s = ranks[2]
        self.rank_w = ranks[3]

        logging.info(f'For {self.player_type}, created card: {self.name}, {self.rank_n}, {self.rank_e}, {self.rank_s}, {self.rank_w}')

    def render(self, x, y, color):
        card_img = pygame.draw.rect(screen, (color), (x, y, 115, 145))


class Deck:
    '''
    Creates a Deck object from a Deck CSV file.
    CSV syntax is: name,rank_n,rank_e,_rank_s,rank_w
    Each line in the CSV is converted to a Card object.
    Each Card object is added to the Deck object.
    '''
    cards = None
    owner = None

    def __init__(self, type):
        self.cards = []
        self.type = type # Player or Computer

    def set(self, deck_file):
        with open(deck_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.cards.append(Card(row['name'], self.type, (row['rank_n'], row['rank_e'], row['rank_s'], row['rank_w'])))

class Hand:
    '''
    Creates a Hand object.
    '''
    cards = None

    def __init__(self):
        logging.info('Created hand')
        self.cards = []

    def add(self, card):
        self.cards.append(card)
        logging.info(f'Added {card.name} to hand')

    def length(self):
        return len(self.cards)

    # def render(self, x, y, color):
    #     x_offset = 0
    #     y_offset = 0
    #     for card in self.cards:
    #         print(card.name)
    #         card_img = pygame.draw.rect(screen, (color), (x + x_offset, y + y_offset, 115, 145))
    #         x_offset += 10
    #         y_offset += 40


def switch_player(current_player):
    if current_player == player:
        current_player = computer
    else:
        current_player = player

def main():
    # Initialize screen
    pygame.init()
    global screen
    screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption('Triple PyAd')

    # Initialize background
    bg_img = pygame.image.load('board.png')
    screen.blit(bg_img, (0, 0))

    # Initialize players
    global player
    global computer
    player = Player('Player')
    computer = Player('Computer')

    # Initialize decks
    player.deck.set('test_deck.csv')
    computer.deck.set('test_deck.csv')

    # Initialize hands
    if RULESET == 'RANDOM':
        i = 0
        while i != 5:
            player.hand.add(player.deck.cards[i])
            i += 1
        i = 0
        while i != 5:
            computer.hand.add(computer.deck.cards[i])
            i += 1

    # Initialize a card (rendered in Event loop)
    card_img = pygame.draw.rect(screen, (255, 0, 0), (30, 30, 115, 145))

    # Initialize clock
    clock = pygame.time.Clock()

    # Event loop
    while True:
        clock.tick(60) # limits game to 60 FPS
        for event in pygame.event.get():
            if event.type == QUIT: # This line is dependent on pygame.locals *
                return

        # Render background
        screen.blit(bg_img, (0, 0))

        # Render player's hand
        for card in player.hand.cards:
            card.render(30, 30, PLAYER_COLOR)

        # Render computer's hand
        for card in computer.hand.cards:
            card.render(560, 30, COMPUTER_COLOR)

        # Update the screen each frame
        pygame.display.flip()

if __name__ == '__main__':
    main()
