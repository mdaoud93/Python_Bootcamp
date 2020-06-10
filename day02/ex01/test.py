

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

s = Student("Marwa", 27)

doom_printer(s)