

def ft_filter(fun, inlist):
    outlist = []
    for elem in inlist:
        if (fun(elem)):
            outlist.append(elem)
    return iter(outlist)



fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(ft_filter(lambda x: x % 2, fibonacci))
print(odd_numbers)
even_numbers = list(ft_filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

# # or alternatively:
# ... 
# even_numbers = list(filter(lambda x: x % 2 -1, fibonacci))
# print(even_numbers)
# [0, 2, 8, 34]
