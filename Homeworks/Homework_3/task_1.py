# Задание 1:
#
# Контекст:
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
#
# Задача:
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

from typing import Union
from random import choice, randint


class Player:
    name = None
    char = None

    def __str__(self):
        return f'{self.name}'


class Human(Player):
    def __init__(self, name):
        self.name = name


class CPU(Player):
    def __init__(self):
        self.name = 'Компьютер'


class Game:
    table = [[None for _ in range(3)] for _ in range(3)]
    step = None

    def __init__(self, player_one: Union[Human, CPU], player_two: Union[Human, CPU]):
        self.player_one = player_one
        self.player_two = player_two
        if isinstance(player_two, CPU) and isinstance(player_one, CPU):
            player_two.name = 'Компьютер 2'

    def goes_first(self):
        drawing_of_lots = choice([self.player_one, self.player_two])
        self.step = drawing_of_lots
        if self.step == self.player_one:
            self.player_one.char = '❌'
            self.player_two.char = '🟢'
        else:
            self.player_two.char = '❌'
            self.player_one.char = '🟢'
        print(f'Первым ходит {drawing_of_lots}')

    def print_table(self):
        for i in self.table:
            print(f'{i}')

    def step_human(self):
        self.print_table()
        print(f'Ход игрока {self.step}')
        while True:
            human_input = input(f'Выбери строку и столбец через пробел, куда поставишь {self.step.char}: ').split()
            correct = self.check_input(human_input)
            if isinstance(correct, list):
                self.table[correct[0]][correct[1]] = self.step.char
                break
            else:
                print(f'{correct}')

    def step_cpu(self):
        self.print_table()
        print(f'Ход игрока {self.step}\n')
        while True:
            cpu_input = [randint(0, 2), randint(0, 2)]
            if self.table[cpu_input[0]][cpu_input[1]] is None:
                self.table[cpu_input[0]][cpu_input[1]] = self.step.char
                break

    def check_input(self, human_input):
        if len(human_input) == 2:
            try:
                line = int(human_input[0])
                column = int(human_input[1])
                if 0 < line <= 3 and 0 < column <= 3:
                    if self.table[line - 1][column - 1] is None:
                        return [line - 1, column - 1]
                    else:
                        return f'Эта ячейка уже занята.'
                else:
                    return f'Ячеек в высоту и ширину не может быть меньше 1 и больше 3.'
            except Exception as _ex:
                return f'Похоже, ты указал не числа.'
        else:
            return f'Ты должен указать 2 числа.'

    def check_win(self):
        if self.table[0][0] == self.step.char and self.table[1][0] == self.step.char \
                and self.table[2][0] == self.step.char \
                or self.table[0][1] == self.step.char and self.table[1][1] == self.step.char \
                and self.table[2][1] == self.step.char \
                or self.table[0][2] == self.step.char and self.table[1][2] == self.step.char \
                and self.table[2][2] == self.step.char \
                or self.table[0][0] == self.step.char and self.table[0][1] == self.step.char \
                and self.table[0][2] == self.step.char \
                or self.table[1][0] == self.step.char and self.table[1][1] == self.step.char \
                and self.table[1][2] == self.step.char \
                or self.table[2][0] == self.step.char and self.table[2][1] == self.step.char \
                and self.table[2][2] == self.step.char \
                or self.table[0][0] == self.step.char and self.table[1][1] == self.step.char \
                and self.table[2][2] == self.step.char \
                or self.table[0][2] == self.step.char and self.table[1][1] == self.step.char \
                and self.table[2][0] == self.step.char:
            return self.step

        count = 9
        for i in self.table:
            for j in i:
                if j is not None:
                    count -= 1
                    if count == 0:
                        return "Ничья!"

        return None

    def play(self):
        self.goes_first()
        while True:
            if isinstance(self.step, CPU):
                self.step_cpu()
            else:
                self.step_human()

            winner = self.check_win()
            if winner is None:
                if self.step == self.player_one:
                    self.step = self.player_two
                else:
                    self.step = self.player_one
            elif winner == 'Ничья!':
                print(f'{winner}')
                break
            else:
                print(f'Победил {winner}')
                self.print_table()
                break


g = Game(Human('Илья'), CPU())
g.play()
