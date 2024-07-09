from random import randint
from time import sleep
def run(old_score:int, is_player:bool) -> int:
    '''Функция получает текущий результат игрока, создает случайное число и прибавляет его к текущему результату.
    в зависимости от аргумента is_player отображает сообщение '''
    number = randint(1, 11)
    new_score = old_score + number
    if is_player:
        print(f'Вы выбросили {number} очков')
        print(f'Теперь у вас {new_score} очков')
    else:
        print(f'Диллер бросил и набрал {new_score} очков')
    return new_score
def rulles(begin:str)-> None:
    '''Отображает правила игры'''
    if begin.lower() not in ['да', 'нет']:
        print(f'Я не понял( Ответьте еще раз')
    if 'да' in begin.lower():
        my_file = open('rules.txt', encoding='utf-8')
        print(my_file.read())
        sleep(13)
    else:
        return
def game():
    '''Логика игры "21"'''
    file_2 = open('start_information.txt', encoding='utf-8')
    print(file_2.read())
    gamer = 0
    casino = 0
    while 0 <= gamer < 21:
        if gamer == 0:
            gamer = run(gamer, is_player=True)
        else:
            answer = input('Бросаем еще?''\n')
            if 'да' in answer.lower():
                gamer = run(gamer, is_player=True)
            elif 'нет' in answer.lower():
                break
            else:
                print(f'Я не понял( Ответьте еще раз')
                continue
    if gamer == 21:
        print(f'Ура! Матч в твою пользу!')
    elif gamer > 21:
        print(f'Сорян, брат, но ты перебрал')
    else:
        while casino <= 16:
            casino = run(casino, is_player=False)
            sleep(2)
            if casino == 21:
                print(f'У дилера очко! ты проиграл(')
            elif casino > 21:
                print(f'Ура! Матч в твою пользу!')
            elif 16 < casino < 21:
                break
    if casino > gamer and casino < 21:
        print(f'По итогам подсчета у диллера {casino} очков, это больше чем у тебя. Увы')
    elif casino == gamer:
        print(f'у тебя и у диллера по {casino} очков! Ничья!')
    elif casino < gamer and gamer < 21:
        print(f'у тебя {gamer} очков! Твоя взяла!')


file_1 = open('start.txt', encoding='utf-8')
print(file_1.read())
sleep(1)
time = rulles(input('Хочешь сначала прочитать правила?' '\n'))
while True:
    game()
    input('Нажмите enter чтобы играть заново...')



