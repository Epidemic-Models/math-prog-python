import pytest

from src.matrix import Matrix


def test_invalid_matrix():
    with pytest.raises(Exception):
        a = Matrix(data=[1, 2, 3])

def test__matrix_multiplication():
    pass
