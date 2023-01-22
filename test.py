import unittest

from triplepyad import Player

class TestPlayer(unittest.TestCase):
    '''
    Test that Player class creates a Player object with
    Player type and Player deck[] list generated from
    a CSV file as expected.
    '''
    def test_player_deck_list(self):

        # Create the Player object
        player_type = 'player'
        deck_file = 'test_deck.csv'
        test_player = Player(player_type, deck_file)

        # Check length of Player's deck[] list
        deck_list_length = len(test_player.deck)

        # Check the length of deck CSV file
        deck_file_length = 0
        with open(deck_file) as f:
            for row in f:
                deck_file_length += 1
        
        # Correct deck file length to account for
        # header and cards added to Player's hand[]
        deck_file_length -= 6

        # Confirm that Player's deck[] list has same
        # number of Card objects as deck CSV has lines
        self.assertEqual(deck_list_length, deck_file_length)

if __name__ == '__main__':
    unittest.main()