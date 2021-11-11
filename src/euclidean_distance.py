import time

import numpy as np


def euclidean_distance(u, v):
    l_1 = len(u)
    l_2 = len(v)
    result = np.zeros((l_1, l_2))

    start = time.time()
    for idx_1 in range(l_1):
        for idx_2 in range(l_2):
            result[idx_1, idx_2] = np.linalg.norm(u[idx_1] - v[idx_2])

    end = time.time()
    print("one loop : ", end - start)
    return result


def main():
    u = np.array([[1, 4, -3], [9, 5, 12], [5, -1, 3]])
    v = np.array([[1, 2, 3], [8, -5, 7]])
    print("u * v: \n", euclidean_distance(u, v))


if __name__ == "__main__":
    main()
