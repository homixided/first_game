import sys
import time


def print_text_by_char(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

print_text_by_char('Введите ЖЕНСКОЕ имя вашего персонажа.')
name = input()
hp = 10
items = {
    'bandage': False,
    'key': False,
    'armor': False,
    'kitchen_knife': False,
    'wall_sword': False,
    'apple_juice': False,
}