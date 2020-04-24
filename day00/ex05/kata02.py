

t = (3,30,2019,9,25)

hour = t[0]
min = t[1]
year = t[2]
day = t[3]
mon = t[4]

if (len(str(day))) < 2:
    print("0", end='')
print(str(day) + "/", end='')
if (len(str(mon))) < 2:
    print("0", end='')
print(str(mon) + "/", end='')
print(str(year), end='')
print(" ", end='')
if (len(str(hour))) < 2:
    print("0", end='')
print(str(hour) + ":", end='')
if (len(str(min))) < 2:
    print("0", end='')
print(str(min))
