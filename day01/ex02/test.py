from vector import Vector

def test_valid_init():
    print("\33[1;32mValid cases\33[1;0m")
    # No errors
    v = Vector([0.0, 1.0, 2.0, 3.0])
    print(v.size)
    print(v.values)
    del v

    v = Vector(3)
    print(v.size)
    print(v.values)
    del v

    v = Vector(range(2, 10, 2))
    print(v.size)
    print(v.values)
    del v

    v = Vector([2, 3.0, 4])
    print(v.size)
    print(v.values)
    del v

def test_valid_init_empty():
    # Empty vectors, no errors
    print("\n\33[1;32mValid cases, empty vectors\33[1;0m")

    v = Vector([])
    print(v.size)
    print(v.values)
    del v

    v = Vector(0)
    print(v.size)
    print(v.values)
    del v

    v = Vector(range(1, 1))
    print(v.size)
    print(v.values)
    del v

    v = Vector(range(9, 3))
    print(v.size)
    print(v.values)
    del v

def test_invalid_init():
    # Errors
    print("\n\33[1;32mInvalid initiation\33[1;0m")

    v = Vector([2, 3.0, "hi"])
    del v

    v = Vector((3, 6))
    del v


# test_valid_init()
# test_valid_init_empty()
# test_invalid_init()

def test_add_valid():
    v1 = Vector([1.0, 2.0, 3.0, 4.0])
    v2 = Vector([5.0, 6.0, 7.0, 8.0])
    v = v1 + v2
    print(v)
    del v

    v = v1 + 1
    print(v)
    del v

    v = 1 + v1
    print(v)
    del v

def test_add_invalid():
    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([5.0, 6.0, 7.0, 8.0])
    v = v1 + v2
    print(v)
    del v

    v = v1 + "hi"
    print(v)
    del v

    v = "hi" + v1
    print(v)
    del v

def test_sub_valid():
    v1 = Vector([1.0, 2.0, 3.0, 4.0])
    v2 = Vector([5.0, 6.0, 7.0, 8.0])
    v = v2 - v1
    print(v)
    del v

    v = v1 - 1
    print(v)
    del v

    v = 1 - v1
    print(v)
    del v

def test_mul_valid():
    v1 = Vector([1.0, 2.0, 3.0, 4.0])
    v2 = Vector([5.0, 6.0, 7.0, 8.0])
    v = v2 * v1
    print(v)
    del v

    v = v1 * 2
    print(v)
    del v

    v = 2 * v1
    print(v)
    del v

def test_print():
    v1 = Vector([1.0, 2.0, 3.0, 4.0])
    v2 = Vector([5.0, 6.0, 7.0, 8.0])

    print (v1 + v2)

test_print()