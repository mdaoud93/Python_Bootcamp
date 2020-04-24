

t = (0, 4, 132.42222, 10000, 12345.67)

day = t[0]
ex = t[1]
fl = t[2]
pwr1 = t[3]
pwr2 = t[4]

print("day_" + f'{day:02}' + ", ", end='')
print("ex_" + f'{ex:02}' + ": ", end='')
print(str(round(fl, 2))+ ", ", end='')
print("{:.2e}".format(pwr1) + ", ", end='')
print("{:.2e}".format(pwr2))
