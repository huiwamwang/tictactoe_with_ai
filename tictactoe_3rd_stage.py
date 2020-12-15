class Tictactoe:
    def __init__(self):
        self.ai_level = None
        self.dic = {'11': 0, '12': 1, '13': 2, '21': 3, '22': 4, '23': 5, '31': 6, '32': 7, '33': 8}
        self.menu()

    def printing(self):
        print("---------")
        for i in range(0, 9, 3):
            print(f'| {self.inp[i]} {self.inp[i+1]} {self.inp[i+2]} |')
        print("---------")
        self.check_status()

    def check_status(self):
        first = [self.inp[0] + self.inp[1] + self.inp[2], self.inp[3] + self.inp[4] + self.inp[5], self.inp[6] +
                 self.inp[7] + self.inp[8]]
        second = [self.inp[0] + self.inp[3] + self.inp[6], self.inp[1] + self.inp[4] + self.inp[7], self.inp[2] +
                  self.inp[5] + self.inp[8]]
        third = [self.inp[2] + self.inp[4] + self.inp[6]]
        fourth = [self.inp[0] + self.inp[4] + self.inp[8]]
        total = first + second + third + fourth
        if 'OOO' in total:
            print('O wins')
            self.menu()
        elif 'XXX' in total:
            print('X wins')
            self.menu()
        elif ' ' not in self.inp:
            print('Draw')
            self.menu()
        if self.ai_vs_p is not None:
            if self.ai_vs_p == 'ai_move':
                self.ai_vs_p = 'computer'
            elif self.ai_vs_p == 'player_move':
                self.ai_vs_p = 'human'
            elif self.ai_vs_p == 'human':
                self.ai_vs_p = 'computer'
            elif self.ai_vs_p == 'computer':
                self.ai_vs_p = 'human'
        self.user_input()

    def check_players(self):
        if self.versus[0] != 'user' and self.versus[1] != 'user':
            self.player = False
        elif self.versus[0] == 'user' and self.versus[1] == 'user':
            self.player = True
        elif self.versus[0] == 'user' and self.versus[1] != 'user':
            self.ai_vs_p = 'player_move'
        elif self.versus[0] != 'user' and self.versus[1] == 'user':
            self.ai_vs_p = 'ai_move'
        self.printing()

    def user_input(self):
        try:
            if self.player or self.ai_vs_p == 'human':
                input2 = [int(i) for i in input('Enter the coordinates: > ').split()]
                coord = ''.join([str(i) for i in input2])
                try:
                    if self.inp[self.dic[coord]] != ' ':
                        print('This cell is occupied! Choose another one!')
                        return self.user_input()
                    else:
                        return self.game(coord)
                except KeyError:
                    print('Coordinates should be from 1 to 3!')
                    return self.user_input()
            elif not self.player or self.ai_vs_p == 'computer':
                self.computer_input()
        except ValueError:
            print('You should enter numbers!')
            return self.user_input()

    def computer_input(self):
        print(f'Making move level "{self.ai_level}"')
        for key, value in self.dic.items():
            if value == self.inp.index(' '):
                self.game(key)

    def game(self, coord):
        if self.turns % 2:
            self.inp[self.dic[coord]] = 'X'
        else:
            self.inp[self.dic[coord]] = 'O'
        self.turns += 1
        self.printing()

    def menu(self):
        menu_input = input('Input command: ').lower().split()
        if menu_input[0] == 'exit':
            exit()
        elif len(menu_input) != 3:
            print('Bad parameters!')
            self.menu()
        else:
            self.versus = [menu_input[1], menu_input[2]]
            self.inp = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.turns = 1
            self.player = None
            self.ai_vs_p = None
            self.check_players()


Tictactoe()
