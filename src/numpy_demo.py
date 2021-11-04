import time

import numpy as np


def main():
    #numpy_fundamentals()
    #numpy_basics()
    numpy_broadcasting()


def numpy_fundamentals():
    a = np.array([1, 2, 3])
    print(a)
    b = np.array([0, -1, 1])
    print(b)
    print(a + b)
    print(a * b)
    print(a @ b)
    c = np.array([[1, 2], [3, 4], [5, 6]])
    print("Matrix c: \n ", c)
    print(a @ c)
    print("Shape of matrix c: ", c.shape)


def numpy_basics():
    start = time.time()
    matrix = [[1 for _ in range(1000)] for _ in range(1000)]
    end = time.time()
    print("List comprehension: ", end - start)

    start = time.time()
    matrix_np = np.ones((1000, 1000))
    end = time.time()
    print("np.ones: ", end - start)
    
    def two_loops(matrix):
        result = []
        for row in matrix:
            result_row = []
            for elem in row:
                result_row.append(2 * elem)
            result.append(result_row)

    start = time.time()
    two_loops(matrix)
    end = time.time()
    print("Two loop: ", end - start)

    def one_loop(matrix):
        result = []
        for row in matrix:
            result.append(2 * row)

    start = time.time()
    one_loop(matrix_np)
    end = time.time()
    print("One loop: ", end - start)

    start = time.time()
    matrix_double = 2 * matrix_np
    end = time.time()
    print("No loops: ", end - start)


def numpy_broadcasting():
    num_u = 1000
    num_v = 100

    mtx_u = np.random.random((num_u, 32 * 32))
    mtx_v = np.random.random((num_v, 32 * 32))

    result_two_loops = np.zeros((num_u, num_v))

    start = time.time()
    for i in range(num_u):
        for j in range(num_v):
            result_two_loops[i, j] = np.sqrt(np.sum((mtx_u[i] - mtx_v[j]) ** 2))
    end = time.time()
    print("Two loops: ", end - start)


if __name__ == "__main__":
    main()
