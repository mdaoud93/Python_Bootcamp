import sys
import string

def text_analyzer(arg_text):
    default_txt = "This is an example text."
    if (arg_text is None):
        print("ERROR")
    char_num = int(0)
    upper = int(0)
    lower = int(0)
    spaces = int(0)
    punct = int(0)
    text_size = len(arg_text)
    if (text_size == 0):
        text = default_txt
    else:
        text = arg_text
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
    print("The text contains ", char_num, " characters")
    print()
    print("- ", upper, " upper letters")
    print()
    print("- ", lower, " lower letters")
    print()
    print("- ", punct, " punctuation marks")
    print()
    print("- ", spaces, " spaces")


# text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")
# text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
# text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")


text_analyzer(sys.argv[1])