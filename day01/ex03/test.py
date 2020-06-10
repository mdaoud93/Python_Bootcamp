from matrix import Matrix

def test_matrix_invalid():
    m = Matrix([[0, 1, 2, 3], [4, 5, 6]])
    m = Matrix("Hello")



# test_matrix_invalid()

m = Matrix()
print(m)