import numpy as np
from FilesAndData import FilesAndData


class Vectors:
    """This class performs all operations with vectors"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def scalar_product(self):
        """This function calculates the scalar product."""
        while True:
            try:
                scalar = float(input("Enter the value of scalar.\n> "))
                break
            except ValueError:
                print("Please, enter numerical values!")
        return list(scalar * np.array([self.x, self.y, self.z]))

    def calculate_magnitude(self):
        """This function calculates the magnitude of one given vector."""
        return np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, vector2):
        """This function returns a new vector which is the sum of two original ones."""
        return [self.x + vector2.x, self.y + vector2.y, self.z + vector2.z]

    def __sub__(self, vector2):
        """This function returns a new vector which is the subtraction of two original ones."""
        return [self.x - vector2.x, self.y - vector2.y, self.z - vector2.z]

    def dot_product_as_number(self, vector2):
        """This function calculates the Dot product magnitude using the Dot product property."""
        return self.x * vector2.x + self.y * vector2.y + self.z * vector2.z

    def dot_product_as_vector(self, vector2):
        """This function calculates a vector which is the result of dot product of two initial vectors."""
        return [self.x * vector2.x, self.y * vector2.y, self.z * vector2.z]

    def cross_product_area(self, vector2):
        """This function calculates the Cross product area using the Dot product property."""
        magnitude1 = np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        magnitude2 = np.sqrt(vector2.x ** 2 + vector2.y ** 2 + vector2.z ** 2)
        return magnitude1 * magnitude2 * np.sin(np.radians(self.angle_between_two_vectors(vector2)))

    def cross_product_vector(self, vector2):
        """This function calculates a vector which is the result of cross product of two initial vectors."""
        return [self.y * vector2.z - self.z * vector2.y,
                self.z * vector2.x - self.x * vector2.z,
                self.x * vector2.y - self.y * vector2.x]

    def angle_between_two_vectors(self, vector2):
        """This function calculates the angle between two given vectors."""
        dot_product = lambda v1, v2: sum((a * b) for a, b in zip(v1, v2))
        length = lambda v: np.sqrt(dot_product(v, v))
        vector_1 = [self.x, self.y, self.z]
        vector_2 = [vector2.x, vector2.y, vector2.z]
        cos_angle = dot_product(vector_1, vector_2) / (length(vector_1) * length(vector_2))
        if not (1 >= cos_angle >= -1):
            print("Given value are out of bound [-1, 1].")
            return 0.0
        return np.degrees(np.arccos(cos_angle))

    @classmethod
    def get_coordinates(cls):
        """
        This function allows user to input the coordinates of one
        or two vectors depending on the type of operation.
        :return: List of coordinates.
        """
        while True:
            try:
                print("\nEnter vector's coordinates.")
                x, y, z = float(input("X: ")), float(input("Y: ")), float(input("Z: "))
                break
            except ValueError:
                print("Please, enter numerical values!")
        return [x, y, z]

    @classmethod
    def creating_vector_object(cls):
        """
        This function stores all coordinates values to the class VectorsOperations.
        :return: Vector Object.
        """
        # if one_or_two_vectors == 0:
        coordinates = cls.get_coordinates()
        return cls(coordinates[0], coordinates[1], coordinates[2])

    @classmethod
    def vector_operations(cls, saving_wish, file_object):
        """
        This function performs all operations with vectors.
        :param file_object: To write files to selected file.
        :param saving_wish: If this parameter if False then save function just passes.
        :return: None
        """
        FilesAndData.print_all(1)
        calculation_wish = input("> ")

        if calculation_wish == "1" or calculation_wish == "2":
            vector = cls.creating_vector_object()
            if calculation_wish == "1":
                magnitude = vector.calculate_magnitude()
                print(f"The answer is: {magnitude}")
                file_object.reading_and_writing_data(saving_wish, magnitude=magnitude)
            elif calculation_wish == "2":
                scalar = vector.scalar_product()
                print(f"The answer is: {scalar}")
                file_object.reading_and_writing_data(saving_wish, coordinates=scalar)
        else:
            vector_1: Vectors = cls.creating_vector_object()
            vector_2: Vectors = cls.creating_vector_object()
            if calculation_wish == "3":
                sum = vector_1.__add__(vector_2)
                print(f"The answer is: {sum}")
                FilesAndData.plot_result(sum)
                file_object.reading_and_writing_data(saving_wish, coordinates=sum)
            elif calculation_wish == "4":
                subtraction = vector_1.__sub__(vector_2)
                print(f"The answer is: {subtraction}")
                FilesAndData.plot_result(subtraction)
                file_object.reading_and_writing_data(saving_wish, coordinates=subtraction)
            elif calculation_wish == "5":
                dot = vector_1.dot_product_as_number(vector_2)
                print(f"The answer is: {dot}")
                file_object.reading_and_writing_data(saving_wish, magnitude=dot)
            elif calculation_wish == "6":
                vector_dot_product = vector_1.dot_product_as_vector(vector_2)
                print(f"The answer is: {vector_dot_product}")
                FilesAndData.plot_result(vector_dot_product)
                file_object.reading_and_writing_data(saving_wish, coordinates=vector_dot_product)
            elif calculation_wish == "7":
                cross = vector_1.cross_product_area(vector_2)
                print(f"The answer is: {cross}")
                file_object.reading_and_writing_data(saving_wish, magnitude=cross)
            elif calculation_wish == "8":
                vector_cross_product = vector_1.cross_product_vector(vector_2)
                print(f"The answer is: {vector_cross_product}")
                FilesAndData.plot_result(vector_cross_product)
                file_object.reading_and_writing_data(saving_wish, coordinates=vector_cross_product)
            elif calculation_wish == "9":
                angle_between = vector_1.angle_between_two_vectors(vector_2)
                print(f"The answer is: {angle_between}")
                file_object.reading_and_writing_data(saving_wish, angle=angle_between)
