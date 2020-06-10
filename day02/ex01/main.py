


def what_are_the_vars(*args, **kwargs):
    """Making a list of attributes of an object"""
    obj = ObjectC()
    for key, value in kwargs.items():
        if (key[0:4] == "var_"):
            return None
        setattr(obj, key, value)
    i = 0
    for att in args:
        att_name = "var_" + str(i)
        i += 1
        setattr(obj, att_name, att)
    return obj

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end\n")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)

    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)

    obj = what_are_the_vars()
    doom_printer(obj)

    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)

    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)


# var_0: 7
# end

# var_0: ft_lol
# var_1: Hi
# end

# end

# a: 10
# hello: world
# var_0: 12
# var_1: Yes
# var_2: [0, 0, 0]
# end

# ERROR
# end