import sys


languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

if len(languages) == 0:
    print("\033[93mEmpty dictionnary\033[0m")
for k in languages.keys():
    print("\033[34m" + str(k) + "\033[0m was created by \033[32m" + str(languages[k]) + "\033[0m")