import numpy as np
from FilesAndData import FilesAndData


class Matrix:
    """This class performs all operations with matrices"""

    def __init__(self, matrix1, matrix2=None):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def add(self):
        """Matrix addition"""
        return np.add(self.matrix1, self.matrix2)

    def subtract(self):
        """Matrix subtraction"""
        return np.subtract(self.matrix1, self.matrix2)

    def multiply(self):
        """Matrix multiplication"""
        return np.multiply(self.matrix1, self.matrix2)

    def dot(self):
        """Matrix product"""
        return np.dot(self.matrix1, self.matrix2)

    def divide(self):
        """Matrix division"""
        return np.divide(self.matrix1, self.matrix2)

    def square_root(self):
        """Square root of matrix"""
        return np.sqrt(self.matrix1)

    def column_sum(self):
        """Column wise summation of matrix elements"""
        return np.sum(self.matrix1, axis=0)

    def row_sum(self):
        """Row wise summation of matrix elements"""
        return np.sum(self.matrix1, axis=1)

    def transpose(self):
        """Transposes one matrix."""
        return self.matrix1.T

    @classmethod
    def get_matrix(cls, one_or_two_matrices):
        """
        This function allows use to input matrix.
        :param one_or_two_matrices: Get one or two matrices depending on operation.
        :return: List of matrices.
        """
        while True:
            try:
                rows = int(input("Enter the number of rows: "))
                columns = int(input("Enter the number of columns: "))
                print("Enter the entries in a single line (separated by space)")
                entries = list(map(int, input("> ").split()))
                matrix1 = np.array(entries).reshape(rows, columns)
                break
            except ValueError:
                print("Please enter correct values!")
        if one_or_two_matrices:
            while True:
                try:
                    rows = int(input("Enter second matrix number of rows: "))
                    columns = int(input("Enter second matrix number of columns: "))
                    print("Enter the entries in a single line (separated by space)")
                    entries = list(map(int, input("> ").split()))
                    matrix2 = np.array(entries).reshape(rows, columns)
                    break
                except ValueError:
                    print("Please enter correct values!")
            return [matrix1, matrix2]
        else:
            return [matrix1]

    @classmethod
    def creating_matrix_object(cls, one_or_two_matrices):
        """
        This function creates matrix object to perform operations on given matrices.
        :param one_or_two_matrices: To create object with one or two matrices.
        :return: Matrix object.
        """
        if one_or_two_matrices:
            matrices = cls.get_matrix(True)
            return cls(matrices[0], matrices[1])
        else:
            matrices = cls.get_matrix(False)
            return cls(matrices[0])

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
            if calculation_wish == "1":
                sum = cls.creating_matrix_object(True).add()
                print("The answer is: ")
                for i in sum:
                    print(i)
                file_object.reading_and_writing_data(saving_wish, matrix=sum)
            elif calculation_wish == "2":
                subtraction = cls.creating_matrix_object(True).subtract()
                print("The answer is: ")
                for i in subtraction:
                    print(i)
                file_object.reading_and_writing_data(saving_wish, matrix=subtraction)
            elif calculation_wish == "3":
                multiply = cls.creating_matrix_object(True).multiply()
                print("The answer is: ")
                for i in multiply:
                    print(i)
                file_object.reading_and_writing_data(saving_wish, matrix=multiply)
            elif calculation_wish == "4":
                product = cls.creating_matrix_object(True).dot()
                print("The answer is: ")
                for i in product:
                    print(i)
                file_object.reading_and_writing_data(saving_wish, matrix=product)
            elif calculation_wish == "5":
                division = cls.creating_matrix_object(True).divide()
                print("The answer is: ")
                for i in division:
                    print(i)
                file_object.reading_and_writing_data(saving_wish, matrix=division)
            elif calculation_wish == "6":
                root = cls.creating_matrix_object(False).square_root()
                print("The answer is: ")
                for i in root:
                    print(i)
                file_object.reading_and_writing_data(saving_wish, matrix=root)
            elif calculation_wish == "7":
                column = cls.creating_matrix_object(False).column_sum()
                print("The answer is: ")
                print(column.tolist())
                file_object.reading_and_writing_data(saving_wish, matrix=column)
            elif calculation_wish == "8":
                row = cls.creating_matrix_object(False).row_sum()
                print("The answer is: ")
                print(row.tolist())
                file_object.reading_and_writing_data(saving_wish, matrix=row)
            elif calculation_wish == "9":
                transpose = cls.creating_matrix_object(False).transpose()
                print("The answer is: ")
                print(transpose.tolist())
                file_object.reading_and_writing_data(saving_wish, matrix=transpose)
        except ValueError:
            print("Cannot perform such type of operation with these values")
            cls.matrix_operations(saving_wish, file_object)
