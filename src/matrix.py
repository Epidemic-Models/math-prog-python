from __future__ import annotations


class Matrix:
    def __init__(self, data: list) -> None:
        self.check_input_data(data=data)
        self.__data = data
        self.__n_rows = None
        self.__n_cols = None

    @property
    def n_rows(self) -> int:
        self.__n_rows = len(self.__data)
        return self.__n_rows

    @property
    def n_cols(self) -> int:
        self.__n_cols = len(self.__data[0])
        return self.__n_cols

    @property
    def data(self) -> list:
        return self.__data

    def __str__(self) -> str:
        result = ""
        for row in self.__data:
            result += str(row)
            result += "\n"
        return result

    def __matmul__(self, other: Matrix) -> Matrix:
        if isinstance(other, Matrix):
            if self.n_cols == other.n_rows:
                result = []
                for idx_1 in range(0, self.n_rows):
                    temp_row = []
                    for idx_2 in range(0, other.n_cols):
                        elem = 0
                        for idx_3 in range(0, self.n_cols):
                            elem += self.__data[idx_1][idx_3] * other.data[idx_3][idx_2]
                        temp_row.append(elem)
                    result.append(temp_row)
                return Matrix(data=result)
            else:
                raise Exception("The matrices are not compatible.")
        else:
            raise Exception("The given multiplier is not a matrix.")

    def __add__(self, other: Matrix) -> Matrix:
        if isinstance(other, Matrix):
            if self.n_rows == other.n_rows and self.n_cols == other.n_cols:
                result = []
                for idx_1 in range(0, self.n_rows):
                    temp_row = []
                    for idx_2 in range(0, self.n_cols):
                        elem = self.__data[idx_1][idx_2] + other.data[idx_1][idx_2]
                        temp_row.append(elem)
                    result.append(temp_row)
                return Matrix(data=result)
            else:
                raise Exception("The matrices are not compatible")
        else:
            raise Exception("The other object is not a matrix ")

    def __eq__(self, other: Matrix) -> bool:
        pass

    @staticmethod
    def check_input_data(data: list) -> None:
        # Check whether the input is a list
        if isinstance(data, list):
            n_cols = None
            for row in data:
                # Check whether all elements of the list are list
                if isinstance(row, list):
                    # First row
                    if n_cols is None:
                        # Check whether the first row is empty
                        if len(row) > 0:
                            n_cols = len(row)
                        else:
                            raise Exception("First row of the input data is empty.")
                    # All rows from the second row
                    else:
                        # Check whether all rows have the same size
                        if n_cols == len(row):
                            n_cols = len(row)
                        else:
                            raise Exception("The input data has rows with different length.")

                    for elem in row:
                        # Check whether all elements in the row is a number
                        if isinstance(elem, int) or isinstance(elem, float):
                            pass
                        else:
                            raise Exception("The input data has a non-number element.")
                else:
                    raise Exception("The input consist of an element which is not a list.")
        else:
            raise Exception("The input data is not a list.")


def main() -> None:
    a = Matrix(data=[[1, 2], [3, 4]])
    b = Matrix(data=[[0, 1, 0], [-1, 1, -1]])
    c = Matrix(data=[[1, 2], [3, 4]])
    print(a)
    print(a @ b)
    print(a + c)


if __name__ == "__main__":
    main()
