import random
def search(keyword, filename):
    print('generator started')
    f = open(filename, 'r')
    # Looping through the file line by line
    for line in f:
        if keyword in line:
            # If keyword found, return it
            yield line
    f.close()

def gen(text, sep = " ", option=None):
    word_list = text.split(sep)
    if (option is None):
        pass
    elif (option == "shuffle"):
        random.shuffle(word_list)
    elif (option == "ordered"):
        word_list.sort(key=str.casefold)
    elif (option == "unique"):
        dict = {}
        for word in word_list:
            if (not word in dict):
                dict[word] = 1
            else:
                dict[word] = dict[word] + 1
            word_list = [k for k,v in dict.items() if v == 1]
    else:
        raise ValueError("Error, option must be one of the following: 'shuffle', 'unique' or 'ordered'")
    for word in word_list:
        yield(word)

text = "Le Lorem Ipsum est simplement du faux texte."
# text = "1 2 3 4 5 6 7 3 4 5"
for word in gen(text, " "):
    print(word)