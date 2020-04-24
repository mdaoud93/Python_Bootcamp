import sys
import string

def run_check(args):
    for i in range(1, len(args)):
        for letter in args[i]:
            if (not letter.isalnum() and not letter.isspace()):
                print("ERROR")
                sys.exit(0)

MORSE_CODE_DICT = {
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----'
}

first_space = True
first_slash = True
first_arg = True
run_check(sys.argv)
for i in range(1, len(sys.argv)):
    arg = sys.argv[i].split()
    for word in arg:
        if (first_arg):
            first_arg = False
        else:
            print(" /", end='')
        for letter in word.upper():
            if (first_space):
                first_space = False
            else:
                print(" ", end='')
            print(MORSE_CODE_DICT[letter], end='')
print()
