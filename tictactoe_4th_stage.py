import random


class Tictactoe:
    def __init__(self):
        self.dic = {'11': 0, '12': 1, '13': 2, '21': 3, '22': 4, '23': 5, '31': 6, '32': 7, '33': 8}
        self.combinations = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        self.menu()

    def printing(self):
        print("---------")
        for item in range(0, 9, 3):
            print(f'| {self.inp[item]} {self.inp[item+1]} {self.inp[item+2]} |')
        print("---------")
        self.check_status()

    def check_status(self):
        for combination in self.combinations:
            if self.inp[combination[0]] == self.inp[combination[1]] == self.inp[combination[2]] and \
                    self.inp[combination[0]] != ' ':
                print(f'{self.inp[combination[0]]} wins')
                self.menu()
        if ' ' not in self.inp:
            print('Draw')
            self.menu()
        self.game()

    def game(self):
        self.next_move = next(self.iterator)
        if self.next_move == 'user':
            self.user_input()
        else:
            self.computer_input()

    def user_input(self):
        try:
            coord_inp = [int(_) for _ in input('Enter the coordinates: > ').split()]
            coord = ''.join([str(_) for _ in coord_inp])
            try:
                if self.inp[self.dic[coord]] != ' ':
                    print('This cell is occupied! Choose another one!')
                    return self.user_input()
                else:
                    return self.move(coord)
            except KeyError:
                print('Coordinates should be from 1 to 3!')
                return self.user_input()
        except ValueError:
            print('You should enter numbers!')
            return self.user_input()

    def computer_input(self):
        print(f'Making move level "{self.next_move}"')
        if self.next_move == 'easy':
            self.random()
        elif self.next_move == 'medium':
            for comb in self.combinations:
                if (self.inp[comb[0]] == self.inp[comb[1]] != ' ' and self.inp[comb[2]] == ' ') or \
                        (self.inp[comb[1]] == self.inp[comb[2]] != ' ' and self.inp[comb[0]] == ' ') or \
                        (self.inp[comb[0]] == self.inp[comb[2]] != ' 'and self.inp[comb[1]] == ' '):
                    for i in comb:
                        print('all is good')
                        if self.inp[i] == ' ':
                            self.move(list(self.dic.keys())[i])
            print('something wrong')
            self.random()

    def random(self):
        while True:
            choice = random.choice(list(self.dic.values()))
            if self.inp[choice] == ' ':
                self.move(list(self.dic.keys())[choice])
            else:
                continue

    def move(self, coord):
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
            self.versus = [menu_input[1], menu_input[2]] * 10
            self.iterator = iter(self.versus)
            self.inp = [' ' for _ in range(9)]
            self.turns = 1
            self.printing()


Tictactoe()
