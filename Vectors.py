import numpy as np
from FilesAndData import FilesAndData


class Vectors:
    """This class performs all operations with vectors"""

    def __init__(self, x1, y1, z1, x2=None, y2=None, z2=None, angle=None):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.angle = angle

    def scalar_product(self):
        """This function calculates the scalar product."""
        while True:
            try:
                scalar = float(input("Enter the value of scalar.\n> "))
                break
            except ValueError:
                print("Please, enter numerical values!")
        return list(scalar * np.array([self.x1, self.y1, self.z1]))

    def calculate_magnitude(self):
        """This function calculates the magnitude of one given vector."""
        return np.sqrt(self.x1 ** 2 + self.y1 ** 2 + self.z1 ** 2)

    def __add__(self):
        """This function returns a new vector which is the sum of two original ones."""
        return [self.x1 + self.x2, self.y1 + self.y2, self.z1 + self.z2]

    def __sub__(self):
        """This function returns a new vector which is the subtraction of two original ones."""
        return [self.x1 - self.x2, self.y1 - self.y2, self.z1 - self.z2]

    def dot_product_as_number(self):
        """This function calculates the Dot product magnitude using the Dot product property."""
        magnitude1 = np.sqrt(self.x1 ** 2 + self.y1 ** 2 + self.z1 ** 2)
        magnitude2 = np.sqrt(self.x2 ** 2 + self.y2 ** 2 + self.z2 ** 2)
        return magnitude1 * magnitude2 * np.cos(self.angle)

    def dot_product_as_vector(self):
        """This function calculates a vector which is the result of dot product of two initial vectors."""
        return [self.x1 * self.x2, self.y1 * self.y2, self.z1 * self.z2]

    def cross_product_area(self):
        """This function calculates the Cross product area using the Dot product property."""
        magnitude1 = np.sqrt(self.x1 ** 2 + self.y1 ** 2 + self.z1 ** 2)
        magnitude2 = np.sqrt(self.x2 ** 2 + self.y2 ** 2 + self.z2 ** 2)
        return magnitude1 * magnitude2 * np.sin(self.angle)

    def cross_product_vector(self):
        """This function calculates a vector which is the result of cross product of two initial vectors."""
        return [self.y1 * self.z2 - self.z1 * self.y2,
                self.z1 * self.x2 - self.x1 * self.z2,
                self.x1 * self.y2 - self.y1 * self.x2]

    def angle_between_two_vectors(self):
        """This function calculates the angle between two given vectors."""
        dot_product = lambda v1, v2: sum((a * b) for a, b in zip(v1, v2))
        length = lambda v: np.sqrt(dot_product(v, v))
        vector1 = [self.x1, self.y1, self.z1]
        vector2 = [self.x2, self.y2, self.z2]
        cos_angle = dot_product(vector1, vector2) / (length(vector1) * length(vector2))
        if not (1 >= cos_angle >= -1):
            print("Given value are out of bound [-1, 1].")
            return 0.0
        return np.degrees(np.arccos(cos_angle))

    @classmethod
    def get_coordinates_and_angle(cls, one_or_two_vectors):
        """
        This function allows user to input the coordinates of one
        or two vectors depending on the type of operation.
        :param one_or_two_vectors: Input one or two vectors depending on operation.
        :return: List of coordinates.
        """
        while True:
            try:
                print("\nEnter vector's coordinates.")
                x1, y1, z1 = float(input("X: ")), float(input("Y: ")), float(input("Z: "))
                break
            except ValueError:
                print("Please, enter numerical values!")
        if one_or_two_vectors:
            while True:
                try:
                    print("Enter second vector's coordinates.")
                    x2, y2, z2 = float(input("X: ")), float(input("Y: ")), float(input("Z: "))
                    break
                except ValueError:
                    print("Please, enter numerical values!")
            return [x1, y1, z1, x2, y2, z2]
        else:
            return [x1, y1, z1]

    @classmethod
    def creating_vector_object(cls, one_or_two_vectors):
        """
        This function stores all coordinates values to the class VectorsOperations.
        :param one_or_two_vectors: To create object with one or two vectors.
        :return: Vector Object.
        """
        if one_or_two_vectors == 0:
            coordinates = cls.get_coordinates_and_angle(False)
            return cls(coordinates[0], coordinates[1], coordinates[2])
        elif one_or_two_vectors == 1:
            coordinates = cls.get_coordinates_and_angle(True)
            return cls(coordinates[0], coordinates[1], coordinates[2],
                       coordinates[3], coordinates[4], coordinates[5])
        elif one_or_two_vectors == 2:
            coordinates = cls.get_coordinates_and_angle(True)
            while True:
                try:
                    angle_in_degrees = float(input("Enter the angle between two vectors in degrees.\n> "))
                    angle = np.radians(angle_in_degrees)
                    break
                except ValueError:
                    print("\nPlease, enter numerical values!")
            return cls(coordinates[0], coordinates[1], coordinates[2],
                       coordinates[3], coordinates[4], coordinates[5], angle)

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
        if calculation_wish == "1":
            magnitude = cls.creating_vector_object(0).calculate_magnitude()
            print(f"The answer is: {magnitude}")
            file_object.reading_and_writing_data(saving_wish, magnitude=magnitude)
        elif calculation_wish == "2":
            scalar = cls.creating_vector_object(0).scalar_product()
            print(f"The answer is: {scalar}")
            file_object.reading_and_writing_data(saving_wish, coordinates=scalar)
        elif calculation_wish == "3":
            sum = cls.creating_vector_object(1).__add__()
            print(f"The answer is: {sum}")
            FilesAndData.plot_result(sum)
            file_object.reading_and_writing_data(saving_wish, coordinates=sum)
        elif calculation_wish == "4":
            subtraction = cls.creating_vector_object(1).__sub__()
            print(f"The answer is: {subtraction}")
            FilesAndData.plot_result(subtraction)
            file_object.reading_and_writing_data(saving_wish, coordinates=subtraction)
        elif calculation_wish == "5":
            dot = cls.creating_vector_object(2).dot_product_as_number()
            print(f"The answer is: {dot}")
            file_object.reading_and_writing_data(saving_wish, magnitude=dot)
        elif calculation_wish == "6":
            vector_dot_product = cls.creating_vector_object(1).dot_product_as_vector()
            print(f"The answer is: {vector_dot_product}")
            FilesAndData.plot_result(vector_dot_product)
            file_object.reading_and_writing_data(saving_wish, coordinates=vector_dot_product)
        elif calculation_wish == "7":
            cross = cls.creating_vector_object(2).cross_product_area()
            print(f"The answer is: {cross}")
            file_object.reading_and_writing_data(saving_wish, magnitude=cross)
        elif calculation_wish == "8":
            vector_cross_product = cls.creating_vector_object(1).cross_product_vector()
            print(f"The answer is: {vector_cross_product}")
            FilesAndData.plot_result(vector_cross_product)
            file_object.reading_and_writing_data(saving_wish, coordinates=vector_cross_product)
        elif calculation_wish == "9":
            angle_between = cls.creating_vector_object(1).angle_between_two_vectors()
            print(f"The answer is: {angle_between}")
            file_object.reading_and_writing_data(saving_wish, angle=angle_between)
