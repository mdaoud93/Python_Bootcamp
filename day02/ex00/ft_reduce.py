from functools import reduce 

def ft_reduce(fun, inlist):
    if (len(inlist) == 0):
        raise TypeError("reduce() of empty sequence with no initial value")
    if (len(inlist) == 1):
        return (inlist[0])
    out = f(inlist[0], inlist[1])
    for elem in inlist[2:]:
        out = fun(out, elem)
    return out


f = lambda a,b: a if (a > b) else b

x = ft_reduce(f, [47])
print(x)
x = ft_reduce(f, [47, 112])
print(x)
x = ft_reduce(f, [47,11,42,102,13])
print(x)