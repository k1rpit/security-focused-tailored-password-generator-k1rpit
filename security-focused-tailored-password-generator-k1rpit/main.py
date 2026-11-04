from sys import argv,exit
from tool_gen_pwd.generator import *



sys_arv = argv[1:]

def main() -> None:
    if sys_arv:
        if sys_arv[0] == '-v' or sys_arv[0] == '--vulnerable':
            print('=='*31)
            print(generate_vulnerable_password())
            print('=='*31)
        elif sys_arv[0] == '-c' or sys_arv[0] == '--classic':
            print('=='*31)
            print(generate_classic_password())
            print('=='*31)
        elif sys_arv[0] == '-pn' or sys_arv[0] == '--pincode':
            print('=='*31)
            print(generate_pin_code())
            print('=='*31)
        elif sys_arv[0] == '-cm' or sys_arv[0] == '--complex':
            print('=='*31)
            print(generate_complex_password())
            print('=='*31)
        elif sys_arv[0] == '-ho' or sys_arv[0] == '--highly-obfuscated':
            print('=='*31)
            print(generate_highly_obfuscated_password())
            print('=='*31)
        elif sys_arv[0] == '-h' or sys_arv[0] == '--help':
             print('''
                  Advanced Custom Password Generation Engine by k1rpit

Available arguments:
    -lo or --lite-obfus        Invert case, append random 4-digit number and punctuation sign;
    -no or --normal-obfus      Transform word core via mirror-map with double random tail;
    -ho or --hard-obfus        Extreme mutation via dynamic initialization map and random UUID slice;
    -h  or --help              Show this help message and exit;

Syntax:
    python3 main.py <argv> 
                  ''')
             exit(1)
        else:
            print('''
                  Advanced Custom Password Generation Engine by k1rpit

Available arguments:
    -lo or --lite-obfus        Invert case, append random 4-digit number and punctuation sign;
    -no or --normal-obfus      Transform word core via mirror-map with double random tail;
    -ho or --hard-obfus        Extreme mutation via dynamic initialization map and random UUID slice;
    -h  or --help              Show this help message and exit;

Syntax:
    python3 main.py <argv> 
                  ''')
            exit('invalid argv')


if __name__ == '__main__':
    main()