from Cube import *

class Player:
    """Класс для хранения имен игроков, а также счетчика шагов и денег"""
    def __init__(self, name, cub, money = 15000000, count = 0):
        self.name = name
        self.cub = cub
        self.money = money
        self.count = count

    def name_player(self):
        """Возвращает имя игрока"""
        return self.name

    def money_player(self):
        """Возвращает количество денег игрока"""
        return self.money

    def count_play(self, count = 0):
        """Возвращает ход игры"""
        count += 1
        return print('Ход игры: {0}'.format(count))

    def set_cub(self, cub):
        self.cub = cub

    def get_cub(self):
        return self.cub

def ifname(name, players):
    """Функция возвращает False если такого имени нет"""
    for player in players:
        if name == player.name_player():
            return True
    return False

def throw_cub(players):
    """Функция броска кубиков"""
    Cubic = Cube()
    for i in players:
        i.set_cub(Cubic.get_cube())
        print('Игрок {0} выбросил {1}'.format(i.name_player(), i.get_cub()))

def select_winers(players):
    """Возвращает список игроков с наибольшим значением броска кубика"""
    max_value = 0
    winers = []
    for player in players:
        if player.get_cub() > max_value:
            winers = []
            winers.append(player)
            max_value = player.get_cub()
        elif player.get_cub() == max_value:
            winers.append(player)
    return winers

def new_Players(win, players):
    """Список для создания нового списка игроков, начиная от игрока с максимальным броском кубика"""
    new_Players = []
    for player in players:
        if player.name_player() == win:
            #new_Players.append(player)
            index = players.index(player)
            #print(index)
            #print(len(players))
    for i in range(index , len(players)):
        new_Players.append(players[i])
        len_list = len(new_Players)
        #print(i)
    for j in players:
        if len(new_Players) < len(players):
            new_Players.append(j)
    #for k in new_Players:
    #    print(k.name_player())
    #print(len(new_Players))
    return new_Players


