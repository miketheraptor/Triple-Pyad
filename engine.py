from enum import Enum
from models import *
import pygame

class GameState(Enum):
    PLAYING = 0
    ENDED = 1

class TriplePyadEngine:
    player1 = None
    player2 = None
    current_player = None
    state = None

def __init__(self):

    # === Initialize Player 1 ('Player'), Deck, and Hand ===
    self.player1 = Player('Player')
    self.player1.deck.set('test_deck.csv')
    i = 0
    while i != 5:
        player.hand.add(player.deck.cards[i])
        i += 1

    # === Initialize Player 2 ('Computer'), Deck, and Hand ===
    self.player2 = Player('Computer')
    self.player2.deck.sec('test_deck.csv')
    self.currentPlayer = self.player1
    i = 0
    while i != 5:
        computer.hand.add(computer.deck.cards[i])
        i += 1

    self.state = GameState.PLAYING

def switch_player(self):
    if self.current_player == self.player1:
        self.current_player = self.player2
    else:
        self.current_player = self.player1

