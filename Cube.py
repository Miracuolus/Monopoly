import random
class Cube:
    """Класс имитации броска кубиков"""
    def get_cube(self, shot = 2):
        """Функция имитация бросания кубика. Возвращает значение броска кубика(ов)"""
        rand = 0
        for i in range(0, shot):
            rand += random.randint(1,6)
        return rand

