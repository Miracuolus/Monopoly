import random
class Error(Exception):
    def __init__(self, text, num):
        self.text = text
        self.num = num
"""
player1
player2
player3
player4
player5
player6"""
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
except ValueError:
    print('*Ошибка ! Необходимо вввести целое число')

def Cube():
    """Функция бросания двух кубиков"""
    rand = random.randint(1, 6)
    return print(rand + rand)
for i in range(1, all_player+1):
    Cube()
