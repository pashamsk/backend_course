from unittest import TestCase, main
from TicTac import TicTacGame
# import pyautogui as pag

class TestTicTac(TestCase):
    """Тесты класса TicTac"""

    def test_input_1(self):
        # # a = pag.press(['1', 'enter', '1', '0', 'enter', '-', '1', 'enter', 'q', 'w', 'e', 'enter', '_', '1', 'enter'])
        # # z = pag.press(['q', 'enter', '1', 'enter'])
        # # out = []
        # print('Введи 5')
        # a = TicTacGame.input_1(self, '1')
        # print('Введи 10, затем введи букву, затем введи 1')
        # b = TicTacGame.input_1(self, '1')
        # print('Введи -1, затем введи 1')
        # c = TicTacGame.input_1(self, '1')
        # self.assertEqual(a, 5)
        # self.assertEqual(b, 1)
        # self.assertEqual(c, 1)
        pass

    def test_validate_input(self): # запускать игру
        """Функция validate_input должна возвращать либо None, либо уникальное значение от 1 до 9"""
        self.assertIsNotNone(TicTacGame.validate_input('1'))
        self.assertIsNone(TicTacGame.validate_input('12'))
        self.assertIsNone(TicTacGame.validate_input('-1'))
        self.assertIsNone(TicTacGame.validate_input('wer2'))

    def test_replace_1(self):
        """Функция replace_1 заменяет i-тый член списка на х или о"""
        b = [1, 2, 3, 'x', 5, 6, 7, 8, 9]
        TicTacGame.replace_1(4, 'x')
        self.assertEqual(TicTacGame.board, b)

    def test_check_winner(self):
        a = [2, 4, 6]
        b = [1, 2, 4, 6]
        c = [1, 2, 3, 4, 8]
        d = [0, 3, 7]
        self.assertTrue(TicTacGame.check_winner(self, a, 5))
        self.assertFalse(TicTacGame.check_winner(self, a, 4))
        self.assertTrue(TicTacGame.check_winner(self, b, 5))
        self.assertFalse(TicTacGame.check_winner(self, c, 5))
        self.assertFalse(TicTacGame.check_winner(self, d, 5))


if __name__ == '__main__':
    main()
    Game = TicTacGame()
    Game.start_game()

