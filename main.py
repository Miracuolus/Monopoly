import random
from Cube import *
from Player import *
class Error(Exception):
    def __init__(self, text, num):
        self.text = text
        self.num = num

Owner = 28
Change = 16
Treachure = 16
GreenHouse = 32
RedHotel = 12


try:
    all_player = int(input('Сколько игроков играет (не более 6 человек)? - '))
    if all_player > 6 or all_player <= 0:
        try:
            raise Error('*Ошибка! Число должно быть от 1 до 6', all_player)
        except Error:
            print('*Ошибка! Число должно быть от 1 до 6')
            exit()
    else:
        print('Введите имена игроков')
        Players = []
        for i in range(1, all_player+1):
            name = input('Введите имя {0} игрока: '.format(i))
            while ifname(name, Players):
                print('Имя {0} уже существует, задайте другое имя'.format(name))
                name = input('Введите имя {0} игрока: '.format(i))
            Players.append(Player(name, 0))
except (ValueError, NameError):
    print('*Ошибка ! Необходимо вввести целое число')
    exit()

throw_cub(Players)

winers = select_winers(Players)

for win in winers:
    print('Игрок {0} выбросил максимальное значение = {1}'.format(win.name_player(), win.get_cub()))
while len(winers) != 1:
    throw_cub(winers)
    winers = select_winers(winers)
    for win in winers:
        print('Игрок {0} выбросил максимальное значение = {1}'.format(win.name_player(), win.get_cub()))



