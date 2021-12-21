import unittest
from src.gra import Game


class Game_test(unittest.TestCase):

    def setUp(self):
        game = Game("Jacek", "Wojtas")
        self.game = game

    def test_check_init_val_player1(self):
        self.assertEqual(self.game.player1_name, "Jacek")

    def test_check_init_val_player2(self):
        self.assertEqual(self.game.player2_name, "Wojtas")

    def test_change_player_success(self):
        self.game.change_player()
        self.assertEqual(self.game.next, 2)

    def test_change_player_success2(self):
        self.game.change_player()
        self.game.change_player()
        self.assertEqual(self.game.next, 1)

    def test_move1(self):
        self.assertEqual(self.game.move(1), [
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0]])

    def test_move2(self):
        self.game.move(2)
        self.assertEqual(self.game.move(1), [
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [2, 1, 0, 0, 0, 0, 0]])

    def tearDown(self):
        self.game = None
