import sys
import string

def text_analyzer(arg_text=None, *argv):
    '''\033[32mThis function counts the number of upper characters, lower characters, punctuation and spaces in a given text.\033[0m'''
    default_txt = "This is an example text. It will have some punctuation marks."
    if (len(argv) > 0):
        print("ERROR")
        return
    if (arg_text is None):
        text = input("What is the text to analyse?\n")
    else:
        text_size = len(arg_text)
        if (text_size == 0):
            print("\033[93mNo text has been give, the default will be the following:\033[0m\n\"" + default_txt + "\"\n")
            text = default_txt
        else:
            text = arg_text
    char_num = int(0)
    upper = int(0)
    lower = int(0)
    spaces = int(0)
    punct = int(0)
    for letter in text:
        char_num = char_num + 1
        if (letter == ' '):
            spaces = spaces + 1
        if (letter >= "A" and letter <= "Z"):
            upper = upper + 1
        elif (letter >= 'a' and letter <= 'z'):
            lower = lower + 1
        elif (letter in [".", ",", "?", "!", "\'", "\"", ":", ";", "-", "(", ")", "[", "]"]):
            punct = punct + 1
    print("The text contains \033[34m", char_num, "\033[0m characters")
    print()
    print("- \033[34m", upper, "\033[0m upper letters")
    print()
    print("- \033[34m", lower, "\033[0m lower letters")
    print()
    print("- \033[34m", punct, "\033[0m punctuation marks")
    print()
    print("- \033[34m", spaces, "\033[0m spaces")


# text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")
# text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
# text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")


# text_analyzer(sys.argv[1])