from colorama import init, Fore, Style
from random import choice

init()


def print_rules() -> None:
    print('Добро пожаловать на игру 5БУКВ!')
    print('У вас есть 6 попыток чтобы угадать слово')
    print(f'''Цветовые обозначения 
Буква есть в слове - {Fore.YELLOW}желтая {Style.RESET_ALL}
Буква на своем месте - {Fore.GREEN}зеленая {Style.RESET_ALL}
Буква встречается больше 1 раза - {Fore.BLUE}синяя {Style.RESET_ALL}
Буква на своем месте но встречается больше 1 раза - {Fore.MAGENTA}фиолетовая {Style.RESET_ALL}''')


def random_word_from_file(file_name: str) -> str:
    '''Функция возвращает из файла рандомное секретное слово, которое нужно угадать'''
    fp = open(file_name, encoding='utf-8')
    word_list = [i.strip() for i in fp if len(i.strip()) == 5]
    random_word = choice(word_list)
    return random_word.lower()

def init_start_data() -> tuple:
    '''Функция создает списки алфавитов для учета введенных букв,
    зи создает игровое поле с пустыми данными для начала игры'''
    letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
               'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    colored = letters.copy()
    pole = [['_', '_', '_', '_', '_'] for _ in range(6)]
    return letters, pole, colored


def print_all_words(all_words: list) -> None:
    for row in all_words:
        print(*row)

def print_start_message(round_num: int) -> None:
    if round_num > 1:
        print('Пока не угадал( Пробуй еще!')
    print(f'Раунд {round_num} из 6')


def input_player_word() -> str:
    while True:
        player_word = input('Введите слово' '\n')
        if player_word.isalpha() and len(player_word) == 5:
            return player_word.lower()
        else:
            print('Такого слова нет или оно не подходит')


def process_round_word(round_player_word: str, game_word: str) -> tuple:
    '''Функция красит буквы в слове игрока согласно правилам,
    чтобы игрок видеол какие буквы есть в секретном слове'''
    check_round_word = []
    letters_not_in = set()
    letters_in = set()
    for numb in range(5):
        round_letter = round_player_word[numb]
        if round_letter == game_word[numb] and game_word.count(round_letter) == 1:
            check_round_word.append(Fore.GREEN + round_letter + Style.RESET_ALL)
            letters_in.add(round_letter)
        elif round_letter == game_word[numb] and game_word.count(round_letter) > 1:
            check_round_word.append(Fore.MAGENTA + round_letter + Style.RESET_ALL)
            letters_in.add(round_letter)
        elif game_word.count(round_letter) > 1:
            check_round_word.append(Fore.BLUE + round_letter + Style.RESET_ALL)
            letters_in.add(round_letter)
        elif round_letter in game_word:
            check_round_word.append(Fore.YELLOW + round_letter + Style.RESET_ALL)
            letters_in.add(round_letter)
        else:
            check_round_word.append(round_letter)
            letters_not_in.add(round_letter)
    return check_round_word, letters_not_in, letters_in


def color_letters_not_in(letters_not_in: list, letters_in: list, avaliable_letters: list, colored_letters: list):
    '''в списках-алфавитах меняет буквы на цветные,
     чтобы игрок понимал какие буквы он уже ипользовал
     и какие из них есть в секретном слове а какие нет.'''
    for letter in letters_not_in:
        i = avaliable_letters.index(letter)
        colored_letters[i] = Fore.BLACK + letter + Style.RESET_ALL
    for letter in letters_in:
        i = avaliable_letters.index(letter)
        colored_letters[i] = Fore.CYAN + letter + Style.RESET_ALL


def print_color_letters_not_in(colored_letters: list):
    print('Выбывшие буквы')
    print(*colored_letters)


def new_word_in_pole(checked_word: str, all_words: list, round_num: int):
    '''Функция заменяет пустой ряд в поле на введенное слово
    с раскрашенными по цветам буквами'''
    all_words[round_num] = checked_word


def game():
    '''основная игра с циклом раундов и уловиями победы и проигрыша'''
    game_word = random_word_from_file('russian-mnemonic-words.txt')
    avaliable_letters, all_words, colored_letters = init_start_data()
    print_rules()
    for round_num in range(1, 7):
        print_start_message(round_num)
        print_color_letters_not_in(colored_letters)
        print_all_words(all_words)
        round_player_word = input_player_word()
        checked_word, letters_not_in, letters_in = process_round_word(round_player_word, game_word)
        color_letters_not_in(letters_not_in, letters_in, avaliable_letters, colored_letters)
        new_word_in_pole(checked_word, all_words, round_num - 1)
        if round_player_word == game_word:
            print_all_words(all_words)
            print(f'Ура, вы выиграли! Верное слово {Fore.GREEN} {round_player_word.upper()} {Style.RESET_ALL}')
            break
    else:
        print_color_letters_not_in(colored_letters)
        print_all_words(all_words)
        print('Ваши попытки закончились(')
        print(f'Слово этой игры - {game_word}')


while True:
    game()
    input('Нажмите enter чтобы играть заново...')
