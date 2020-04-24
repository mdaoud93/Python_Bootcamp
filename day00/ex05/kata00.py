import sys

t = (19,42,21)

tup_len = len(t)
if (tup_len == 0):
    print("\033[93mEmpty tuple\033[0m")
    sys.exit(0)
if (tup_len == 1):
    print("\033[93mThe " + str(tup_len) + " number is: ", end='')
else:
    print("\033[93mThe " + str(tup_len) + " numbers are: ", end='')
first = True
for n in t:
    if (first):
        first = False
    else:
        print(", ", end='')
    print(n, end='')
print("\033[0m")
