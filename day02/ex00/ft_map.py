

def ft_map(fun, in_list):
    out_list = []
    for elem in in_list:
        out_list.append(fun(elem))
    return iter(out_list)

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

temperatures = (36.5, 37, 37.5, 38, 39)


# temperatures_in_Fahrenheit = list(ft_map(fahrenheit, temperatures))
# temperatures_in_Celsius = list(ft_map(celsius, temperatures_in_Fahrenheit))
# print(temperatures_in_Fahrenheit)
# print(temperatures_in_Celsius)

# a = [1, 2, 3, 4]
# b = [17, 12, 11, 10]
# c = [-1, -4, 5, 9]
# list(ft_map(lambda x, y : x+y, a, b))
# [18, 14, 14, 14]
# list(ft_map(lambda x, y, z : x+y+z, a, b, c))
# [17, 10, 19, 23]
# list(ft_map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))
# [37.5, 33.0, 24.5, 21.0]
