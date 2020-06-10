# import numpy as np

# np.random.seed(0)

# x1 = np.random.randint(10, size=6)  # One-dimensional array
# x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
# x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

# print(x3)
# print(x3.ndim)
# print(x3.size)
# print(x3.shape)

# print(type(x3))

from NumPyCreator import NumpyCreator

npc = NumpyCreator()

x = npc.from_list([[1,2,3],[6,3,4]])
print(x)

x = npc.from_list([[1,2,3],[6,3,4]], float)
print(x)

x = npc.from_tuple(("a", "b", "c"))
print(x)

x = npc.from_iterable(range(5))
print(x)

shape=(3,5)
x = npc.from_shape(shape, 7)
print(x)

x = npc.random(shape, dtype=float)
print(x)

x = npc.identity(4)
print(x)