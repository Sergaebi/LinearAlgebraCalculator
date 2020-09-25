import numpy as np
from FilesAndData import FilesAndData


class Matrix:
    """This class performs all operations with matrices"""

    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, matrix2):
        """Matrix addition"""
        return np.add(self.matrix, matrix2)

    def subtract(self, matrix2):
        """Matrix subtraction"""
        return np.subtract(self.matrix, matrix2)

    def multiply(self, matrix2):
        """Matrix multiplication"""
        return np.multiply(self.matrix, matrix2)

    def dot(self, matrix2):
        """Matrix product"""
        return np.dot(self.matrix, matrix2)

    def divide(self, matrix2):
        """Matrix division"""
        return np.divide(self.matrix, matrix2)

    def square_root(self):
        """Square root of matrix"""
        return np.sqrt(self.matrix)

    def column_sum(self):
        """Column wise summation of matrix elements"""
        return np.sum(self.matrix, axis=0)

    def row_sum(self):
        """Row wise summation of matrix elements"""
        return np.sum(self.matrix, axis=1)

    def transpose(self):
        """Transposes one matrix."""
        return self.matrix.T

    @classmethod
    def get_matrix(cls):
        """
        This function allows use to input matrix.
        :return: List of matrices.
        """
        while True:
            try:
                rows = int(input("Enter the number of rows: "))
                columns = int(input("Enter the number of columns: "))
                print("Enter the entries in a single line (separated by space)")
                entries = list(map(int, input("> ").split()))
                matrix = np.array(entries).reshape(rows, columns)
                break
            except ValueError:
                print("Please enter correct values!")
        return matrix

    @classmethod
    def creating_matrix_object(cls):
        """
        This function creates matrix object to perform operations on given matrices.
        :return: Matrix object.
        """
        matrices = cls.get_matrix()
        return cls(matrices)

    @classmethod
    def matrix_operations(cls, saving_wish, file_object):
        """
        This function performs all operations matrices.
        :param file_object: For writing files to selected file.
        :param saving_wish: If this parameter if False then save function just passes.
        :return: None
        """
        FilesAndData.print_all(6)
        calculation_wish = input("> ")
        try:
            if calculation_wish == "1" or calculation_wish == "2" or calculation_wish == "3" \
                    or calculation_wish == "4" or calculation_wish == "5":
                matrix_1 = cls.creating_matrix_object()
                matrix_2 = cls.creating_matrix_object()
                if calculation_wish == "1":
                    sum = matrix_1.add(matrix_2)
                    print("The answer is: ")
                    for i in sum:
                        print(i)
                    file_object.reading_and_writing_data(saving_wish, matrix=sum)
                elif calculation_wish == "2":
                    subtraction = matrix_1.subtract(matrix_2)
                    print("The answer is: ")
                    for i in subtraction:
                        print(i)
                    file_object.reading_and_writing_data(saving_wish, matrix=subtraction)
                elif calculation_wish == "3":
                    multiply = matrix_1.multiply(matrix_2)
                    print("The answer is: ")
                    for i in multiply:
                        print(i)
                    file_object.reading_and_writing_data(saving_wish, matrix=multiply)
                elif calculation_wish == "4":
                    product = matrix_1.dot(matrix_2)
                    print("The answer is: ")
                    for i in product:
                        print(i)
                    file_object.reading_and_writing_data(saving_wish, matrix=product)
                elif calculation_wish == "5":
                    division = matrix_1.divide(matrix_2)
                    print("The answer is: ")
                    for i in division:
                        print(i)
                    file_object.reading_and_writing_data(saving_wish, matrix=division)
            else:
                matrix = cls.creating_matrix_object()
                if calculation_wish == "6":
                    root = matrix.square_root()
                    print("The answer is: ")
                    for i in root:
                        print(i)
                    file_object.reading_and_writing_data(saving_wish, matrix=root)
                elif calculation_wish == "7":
                    column = matrix.column_sum()
                    print("The answer is: ")
                    print(column.tolist())
                    file_object.reading_and_writing_data(saving_wish, matrix=column)
                elif calculation_wish == "8":
                    row = matrix.row_sum()
                    print("The answer is: ")
                    print(row.tolist())
                    file_object.reading_and_writing_data(saving_wish, matrix=row)
                elif calculation_wish == "9":
                    transpose = matrix.transpose()
                    print("The answer is: ")
                    print(transpose.tolist())
                    file_object.reading_and_writing_data(saving_wish, matrix=transpose)
        except ValueError:
            print("Cannot perform such type of operation with these values")
            cls.matrix_operations(saving_wish, file_object)
