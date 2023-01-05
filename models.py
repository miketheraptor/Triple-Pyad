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
    type = None # Player or Computer

    def __init__(self, type):
        self.deck = Deck(type) # Pass 'type' to Deck object so it knows its owner
        self.hand = Hand()
        self.type = type # Player or Computer

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

    def __init__(self, name, type, *args):
        ranks = args[0]

        self.name = name
        self.type = type # Who owns card - Player or Computer
        self.rank_n = ranks[0]
        self.rank_e = ranks[1]
        self.rank_s = ranks[2]
        self.rank_w = ranks[3]

        logging.info(f'For {self.type}, created card: {self.name}, {self.rank_n}, {self.rank_e}, {self.rank_s}, {self.rank_w}')

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



if __name__ == '__main__':
    # models.py was run directly, therefor:
    logging.info('Debug mode active')


    # === Player Initialization ===

    # Create the Player object
    player = Player('Player')

    # Set the Player object's deck
    player.deck.set('test_deck.csv')

    # Fill the Player object's hand with 5 cards from their deck
    # In the game itself, this should be done by player action
    i = 0
    while i != 5:
        player.hand.add(player.deck.cards[i])
        i += 1

    # === Computer Initialization ===

    # Repeat above steps for Computer player
    computer = Player('Computer')
    computer.deck.set('test_deck.csv')
    i = 0
    while i != 5:
        computer.hand.add(computer.deck.cards[i])
        i += 1

    # === GameBoard Initialization ===

    # Create a blank GameBoard object
    board = GameBoard()
    print(board.grid[0][0])

    # Place a card on the GameBoard grid
    board.add(computer.hand.cards[0], 0, 0)
    print(board.grid[0][0].name)