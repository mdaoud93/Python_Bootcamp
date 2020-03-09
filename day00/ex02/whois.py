import sys

len = len(sys.argv)
if (len == 1):
    sys.exit(0)
if (len != 2):
    print("ERROR")
    sys.exit(0)
arg = sys.argv[1]
try:
    val = int(arg)
except ValueError:
    print("ERROR")
    sys.exit(0)
if (val == 0):
    print("i'm Zero.")
elif (val % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
