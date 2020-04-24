import sys
import string


if (len(sys.argv) != 3):
    print("ERROR")
    sys.exit(0)
if (sys.argv[1].isnumeric()):
    print("ERROR")
    exit(0)
if (not sys.argv[2].isnumeric()):
    print("ERROR")
    exit(0)
text = sys.argv[1]
length = int(sys.argv[2])
punct = [".", ",", "?", "!", "\'", "\"", ":", ";", "-", "(", ")", "[", "]"]
final_list = []
word_list = text.split()
for word in word_list:
    if (len(word) > length and word not in punct):
        final_list.append(word)
print(final_list)