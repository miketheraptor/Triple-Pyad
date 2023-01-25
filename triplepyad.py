'''
Triple PyAd by MikeTheRpator

The classic JRPG game Triple Triad from Final Fantasy rewritten in PyGame.
'''


VERSION = '0.1.0'


import csv
import logging
import pygame
from random import randint


# === CONSTANTS ===

# Game Settings

DEBUG_MODE = True
FPS = 60
RULESET = 'RANDOM'


# Initialize Logging Settings

if DEBUG_MODE:
    logging_lvl = logging.INFO
else:
    logging_lvl = logging.CRITICAL

logging.basicConfig(
    format='%(asctime)s - %(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %I:%M',
    level=logging_lvl)


class Card:
    '''
    Creates a Card object with name and ranks.

    Attributes:
        name: A str containing the card's name
        n_value: An int containing the card's top rank
        e_value: An int containing the card's right rank
        s_value: An int containing the card's bottom rank
        w_value: An int containing the card's left rank
        owner: A str containing 'player' or 'computer'
        is_dragging: Boolean indicating if card is being dragged
    '''

    def __init__(self, name, n_value, e_value, s_value, w_value, owner):

        self.name = name
        self.n_value = n_value
        self.e_value = e_value
        self.s_value = s_value
        self.w_value = w_value
        self.owner = owner
        self.is_selected = False

        logging.info(
            f'Created Card: {self.name}, {self.n_value}, {self.e_value}, {self.s_value}, {self.w_value}, {self.owner}'
            )

    def render(self, x_pos, y_pos):
        '''
        Render the Card object to the screen.
        '''

        # Set the Card's background color based on its associated Player object

        if self.owner == 'player':
            color = (0, 0, 255)
        elif self.owner == 'computer':
            color = (255, 0, 0)
        elif self.owner == 'test_player' or 'test_computer':
            color = (50, 50, 50)
        else:
            logging.critical('Card owner not recognized.')
            color = (0, 0, 0)

        # Initialize the Font object for the rank text

        font = pygame.font.SysFont('Arial', 15)

        # ===  Draw the Card and Font ===
        
        # If the card being draw is the selected card, offset its position by x_offset

        if self.is_selected:
            x_offset = 15
        else:
            x_offset = 0

        # Draw the cards with name and ranks
        self.card_rect = pygame.draw.rect(screen, (color), (x_pos - x_offset, y_pos, 115, 145))
        screen.blit(font.render(self.n_value, True, (255, 255, 255)), (x_pos - x_offset + 20, y_pos+5))
        screen.blit(font.render(self.e_value, True, (255, 255, 255)), (x_pos - x_offset + 35, y_pos+20))
        screen.blit(font.render(self.s_value, True, (255, 255, 255)), (x_pos - x_offset + 20, y_pos+35))
        screen.blit(font.render(self.w_value, True, (255, 255, 255)), (x_pos - x_offset + 5, y_pos+20))
        screen.blit(font.render(self.name, True, (255, 255, 255)), (x_pos - x_offset + 5, y_pos+125))


class Player:
    '''
    Creates a Player object with a deck and a hand.

    Attributes:
        deck: A list containing all Card objects in a Player's deck
        hand: A list containing all Card objects in a Player's hand
        player_type: A str containing 'player' or 'computer'
    '''

    def __init__(self, player_type, deck_file):
        self.deck = []
        self.hand = []
        self.player_type = player_type
        self.deck_file = deck_file

        self.set_deck(deck_file)

        # If RULESET is RANDOM, generate random hand[]
        if RULESET == 'RANDOM':
            self.set_hand()

    def set_deck(self, deck_file):
        '''
        Uses a CSV file to generate Card objects and fills the Player's deck[] with them.

        The CSV headers are: name, rank_n, rank_e, rank_s, rank_w
        Each line in the CSV is converted to a Card object.
        Each Card object is added to the Player's deck[] list.

        Attributes:
            deck_file: A path to a csv file containing values for the cards in the player's deck.
        '''
        with open(deck_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.deck.append(Card(row['name'], row['rank_n'], row['rank_e'], row['rank_s'], row['rank_w'], self.player_type))

    def set_hand(self):
        '''
        Adds Card objects from the Player's deck[] list to the Player's hand[] list
        based on current RULESET.
        '''
        if RULESET == 'RANDOM':
            while len(self.hand) != 5:
                value = randint(0, len(self.deck)-1)
                rand_card = self.deck[value]
                self.hand.append(self.deck[value])
                self.deck.remove(self.deck[value])
                logging.info(f'Added {rand_card.name} to {self.player_type} hand.')
        else:
            logging.critical('RULESET not recognized.')




def main():

    #################################################
    ### ====== BEGIN INITIALIZATION/SETUP  ====== ###
    # Everything in here fires only once on launch  #


    # Initialize pygame

    pygame.init()

    # Initialize the main screen object

    global screen
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Triple PyAd')

    # Initialize the background gameboard image

    bg_img = pygame.image.load('board.png')

    # Initialize players

    player = Player('player', 'test_deck.csv')
    computer = Player('computer', 'test_deck.csv')

    # Initialize clock
    
    clock = pygame.time.Clock()


    ### ====== END INITIALIZATION/SETUP ====== ###
    ##############################################












    ##############################################
    ### ======     BEGIN GAME LOOP      ====== ###
    # Everything in here fires every frame

    while True:

        # Set the game's FPS rate

        clock.tick(FPS)

        # Event listener

        for event in pygame.event.get():

            # Do if window is closed

            if event.type == pygame.QUIT:
                return

            # Do if left mouse button is clicked

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for card in player.hand:

                        if card.is_selected == True:
                            card.is_selected = False
                        
                        if card.card_rect.collidepoint(event.pos):
                            card.is_selected = True
                            logging.info(f'{card.name} card selected')

        # Render background to screen

        screen.blit(bg_img, (0,0))

        # = Render cards to screen = #

        # P1 Hand

        y_offset = 0
        i = 0
        for card in player.hand:
            player.hand[i].render(700, 25 + y_offset)
            i += 1
            y_offset += 150


        # P2 Hand

        y_offset = 0
        i = 0
        for card in computer.hand:
            computer.hand[i].render(190, 25 + y_offset)
            i += 1
            y_offset += 150

        # Cards on board



        # Update the screen each frame

        pygame.display.flip()

    ### ======      END GAME LOOP       ====== ###
    ##############################################



if __name__ == '__main__':
    main()