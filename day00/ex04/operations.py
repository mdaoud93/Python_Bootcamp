import sys

def usage_print():
    print("\033[93mUsage\033[0m: python operations.py <number1> <number2>")
    print("\033[93mExample:\033[0m\n\t python operation.py 42 10")

arg_count = len(sys.argv)
if (arg_count != 3):
    usage_print()
    exit(0)
if ((type(sys.argv[1]) == str) or (type(sys.argv[2]) == str)):
    print("\033[31mInputError\033[0m: only numbers.")
    usage_print()
    exit(0)
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
except ValueError:
    print("\033[31mInputError\033[0m: only numbers.")
    usage_print()
    exit(0)
print("\033[34mSum:\033[0m\t\t" + str(num1 + num2))
print("\033[34mDifference:\033[0m\t" + str(num1 - num2))
print("\033[34mProduct:\033[0m\t" + str(num1 * num2))
if (num2 == 0):
    print("\033[34mQuotient:\033[0m\t\033[31mERROR\033[0m (div by zero)")
    print("\033[34mRemainder:\033[0m\t\033[31mERROR\033[0m (div by zero)")
else:
    print("\033[34mSum:\033[0m\t\t" + str(float(num1) / num2))
    print("\033[34mDifference:\033[0m\t" + str(num1 % num2))