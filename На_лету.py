from random import choice

# lambda
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


# замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, mode='w', encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i) + '\n')

    return write_everything


write1 = get_advanced_writer('example.txt')
write1('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        elrem = choice(self.words)
        return elrem


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
