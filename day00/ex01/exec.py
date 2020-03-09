import sys
import string

len = int(len(sys.argv))
if (len == 1):
    sys.exit(0)
firstarg = 1
for i in range(len - 1, 0, -1):
    s = sys.argv[i]
    s = s.swapcase()
    s = s[::-1]
    if (firstarg == 1): firstarg = 0
    else: print(' ', end='')
    print(s, end='')
print()
