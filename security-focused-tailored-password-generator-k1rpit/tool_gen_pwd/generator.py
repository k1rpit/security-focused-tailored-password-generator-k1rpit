from secrets import *
from uuid import uuid4
import string

str_list = list(string.ascii_letters)
int_list = list(string.digits)
sym_list = list(string.punctuation)
strHex_list = list(string.hexdigits)

replacement_dictionary_hard = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero',
     'a': choice(list(sym_list)),
    's': choice(list(sym_list)),
    'd': choice(list(sym_list)),
    'f': choice(list(sym_list)),
    'g': choice(list(sym_list)),
    'h': choice(list(sym_list)),
    'j': choice(list(sym_list)),
    'k': choice(list(sym_list)),
    'l': choice(list(sym_list)),
    '!': choice(list(sym_list)),
    '@': choice(list(sym_list)),
    '#': choice(list(sym_list)),
    '$': choice(list(sym_list)),
    '%': choice(list(sym_list)),
    '^':choice(list(sym_list)),
    '&': choice(list(sym_list)),
    '*': choice(list(sym_list)),
    '(': choice(list(sym_list)),
    ')': choice(list(sym_list)),
    '_': choice(list(sym_list)),
    '+': choice(list(sym_list)),
    'q': choice(list(sym_list))
}

def generate_vulnerable_password(*,s=str_list,i=int_list,sm=sym_list,sh=strHex_list) -> str:
    data_vulnerable = ['root','data','qwerty','admin','asdfg','user']
    return '{}{}{}'.format(choice(data_vulnerable),choice(i),choice(sm))


def generate_pin_code(*,s=str_list,i=int_list,sm=sym_list,sh=strHex_list) -> str:
    return '{}{}{}{}'.format(choice(i),choice(i),choice(i),choice(i))


def generate_classic_password(*,s=str_list,i=int_list,sm=sym_list,sh=strHex_list) -> str:
    return choice(s)+choice(s)+choice(sm)+choice(s)+choice(i)+choice(s)+choice(s)+choice(s)+choice(sm)+choice(s)+choice(s)+choice(sm)

def generate_complex_password(*,s=str_list,i=int_list,sm=sym_list,sh=strHex_list) -> str:
    return choice(sh)+choice(sh)+choice(sm)+choice(s)+choice(i)+choice(s)+choice(i)+choice(i)+choice(sm)+choice(s)+choice(s)+choice(sh)+choice(s)+choice(s)+choice(sm)+choice(sh)+choice(i)+choice(sh)+choice(sh)+choice(i)

def generate_highly_obfuscated_password(*,s=str_list,i=int_list,sm=sym_list,sh=strHex_list) -> str:
    new_pwd = choice(sh)+choice(sh)+choice(sm)+choice(s)+choice(i)+choice(s)+choice(i)+choice(i)+choice(sm)+choice(s)+choice(s)+choice(sh)+choice(s)+choice(s)+choice(sm)+choice(sh)+choice(i)+choice(sh)+choice(sh)+choice(i)
    for key,value in replacement_dictionary_hard.items():
        new_pwd=new_pwd.replace(f'{key}',f'{value}')
    return new_pwd.swapcase() + str(uuid4())[::choice(list(range(1,10)))] + choice(sm)
