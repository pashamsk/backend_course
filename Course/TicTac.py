class TicTacGame:
    """Игра в крестики - нолики человек с человеком"""

    board = list(range(1, 10))

    def show_board(self):
        """Вывод игрового поля"""
        for i in range(1, 10):
            if i % 3 == 0:
                print(' '.join(map(str, TicTacGame.board[i - 3: i])))

    def input_1(self, user):  # тест
        """Пользовательский ввод"""
        print(f'{user}, ваш ход')
        y = TicTacGame.validate_input(self, input())
        if y is None:
            return self.input_1(user)
        return y

    def validate_input(self, j):
        """Валидный ввод номера клетки"""
        try:
            k = int(j)
            if 0 < k < 10 and TicTacGame.board[k - 1] != ('x' or 'o'):
                return k
            print('введи число заново')
        except ValueError:
            print('это не число')

    def replace_1(self, x, point):
        """Меняет на доске соответствующий индекс на х или о"""
        TicTacGame.board.pop(x - 1)
        TicTacGame.board.insert(x - 1, point)

    def start_game(self):
        """Основная функция, сама игра"""
        usr_1 = input('игрок 1, введи свой ник\n')
        usr_2 = input('игрок 2, введи свой ник\n')
        self.flag = 0
        u_1 = []
        u_2 = []
        i = 0
        u_i = u_1
        self.show_board()
        while self.check_winner(u_i, i) is False and i < 9:
            if i % 2 == 0:
                x = self.input_1(usr_1)
                self.replace_1(x, 'x')
                u_1.append(x - 1)
                u_i = u_1
            else:
                y = self.input_1(usr_2)
                self.replace_1(y, 'o')
                u_2.append(y - 1)
                u_i = u_2
            i += 1
            self.show_board()
        if self.flag == 1:
            if u_i == u_1:
                print(f'{usr_1} выиграл')
            if u_i == u_2:
                print(f'{usr_2} выиграл')
        else:
            print('ничья')

    def check_winner(self, u_i, i):
        """Проверка выигрышной комбинации, начиная с 5го хода"""
        win = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [3, 4, 5], [6, 7, 8], [2, 4, 6], [2, 5, 8], [1, 4, 7]]
        if i > 4:
            enumerate()
            for _ in range(len(win)):
                if set(win[_]).issubset(u_i):
                    self.flag = 1
                    return True
        return False


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
