import logging
import csv

# Initialize Logging Settings
logging.basicConfig(
    format='%(asctime)s - %(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %I:%M',
    level=logging.INFO)

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

    def __init__(self, name, *args):
        ranks = args[0]

        self.name = name
        self.rank_n = ranks[0]
        self.rank_e = ranks[1]
        self.rank_s = ranks[2]
        self.rank_w = ranks[3]

        logging.info(f'Created card: {self.name}, {self.rank_n}, {self.rank_e}, {self.rank_s}, {self.rank_w}')

class Deck:
    '''
    Creates a Deck object from a Deck CSV file.
    CSV format is: name,rank_n,rank_e,_rank_s,rank_w
    Each line in the CSV is converted to a Card object.
    Each Card object is added to the Deck object.
    '''
    cards = None

    def __init__(self, deck_file):
        logging.info('Created deck')
        self.cards = []
        with open(deck_file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.cards.append(Card(row['name'], (row['rank_n'], row['rank_e'], row['rank_s'], row['rank_w'])))

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
        logging.info(f'Added {card} to hand')

    def length(self):
        return len(self.cards)

class GameBoard:
    '''
    Creates a GameBoard object.
    GameBoard coordinate layout is as follows:
            [0, 0] [1, 0] [2, 0]
            [0, 1] [1, 1] [2, 1]
            [0, 2] [1, 2] [2, 2]
    '''

    def __init__(self):
        pass


if __name__ == '__main__':
    logging.info('Debug mode active')

    player_deck = Deck('test_deck.csv')
    computer_deck = Deck('test_deck.csv')
    player_hand = Hand()
    # Adds cards from the player deck to the player hand.
    i = 0
    while i != 5:
        player_hand.add(player_deck.cards[i])
        print(player_hand.cards[i].name)
        i += 1


