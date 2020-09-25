import numpy as np
import json as js
import matplotlib.pyplot as plt
import os
import os.path as op
import pandas as pd
from tabulate import tabulate


class FilesAndData:

    def __init__(self, file_name, data):
        """This function checks if file exists in the folder. If file doesn't exist it creates the Json file."""
        self.file_name = file_name
        self.data = data

    def show_or_manipulate_data(self):
        """This function allows user to display, rename, delete data from Json file."""
        self.print_all(8)
        database_wish = input("> ")
        if database_wish == "1":
            self.show_vector()
        elif database_wish == "2":
            self.show_matrix()

    def reading_and_writing_data(self, save_or_not, coordinates=None, magnitude=None, matrix=None):
        """This function writes all data to 'Vector_Data.json' file."""
        if save_or_not == "1":
            if matrix is None:
                while True:
                    name = input("\nEnter the under which you want to save the calculation.\n> ")
                    if name in self.data[0]:
                        print("\nSuch vector already exists!")
                    else:
                        if coordinates:
                            self.data[0][name] = {
                                'X': coordinates[0],
                                'Y': coordinates[1],
                                'Z': coordinates[2],
                                'Magnitude': np.sqrt(coordinates[0] ** 2 + coordinates[1] ** 2 + coordinates[2] ** 2),
                            }
                        elif magnitude:
                            self.data[0][name] = {
                                'X': None,
                                'Y': None,
                                'Z': None,
                                'Magnitude': magnitude,
                            }
                        break
                with open(self.file_name, 'w') as file2:
                    js.dump(self.data, file2, indent=True)
            else:
                while True:
                    print("\nEnter the name under which you want to save the calculation.")
                    name = input("\r> ")
                    if name in self.data[1]:
                        print("\nSuch matrix already exists!")
                    else:
                        self.data[1][name] = matrix.tolist()
                        break
                with open(self.file_name, 'w') as file2:
                    js.dump(self.data, file2, indent=True)

    def show_vector(self):
        """
        This function allows user to observe vector part of the database.
        :return:
        """
        if self.data[0] == {}:
            print("There is no vector data yet!")
            self.show_or_manipulate_data()
        self.print_all(3)
        display_wish = input("> ")
        if display_wish == "1":
            df = pd.DataFrame(self.data[0])
            print(tabulate(df.transpose(), headers='keys', tablefmt='fancy_grid', numalign='right'))
            self.show_vector()
        elif display_wish == "2":
            try:
                name = input("\nEnter vector's name.\n> ")
                if self.data[0][name]['Angle'] is not None:
                    print(f"\nThe angle between two vectors = {self.data[0][name]['Angle']}")
                elif self.data[0][name]['X'] is None:
                    print(f"\nThere are no coordinates available for {name}.")
                    print(f"{name}'s magnitude = {self.data[0][name]['Magnitude']}.")
                else:
                    print(f"\n{name}'s coordinates = "
                          f"[{self.data[0][name]['X']}, {self.data[0][name]['Y']}, {self.data[0][name]['X']}].")
                    self.plot_result(
                        [self.data[0][name]['X'], self.data[0][name]['Y'], self.data[0][name]['X']])
                    print(f"{name}'s magnitude = {self.data[0][name]['Magnitude']}.")
            except KeyError:
                self.print_all(11)
            self.show_vector()
        elif display_wish == "3":
            name = input("\nEnter vector's name which you want to rename.\n> ")
            if name in self.data[0]:
                new_name = input("\nEnter the new name.\n> ")
                if new_name in self.data[0]:
                    print("Vector with this name already exists!")
                else:
                    self.data[0][new_name] = self.data[0].pop(name)
                    with open("Vector_Data.json", 'w') as file2:
                        js.dump(self.data, file2, indent=True)
                    print("\nVector successfully renamed.")
            else:
                print("\nThere is no saved vector with this name!")
            self.show_vector()
        elif display_wish == "4":
            self.print_all(4)
            statistics_wish = input("> ")
            df = pd.DataFrame(self.data[0])
            if statistics_wish == "1":
                print(tabulate(df.transpose().describe(), headers='keys', tablefmt='fancy_grid', numalign='right'))
            elif statistics_wish == "2":
                print(df.transpose().mean())
            elif statistics_wish == "3":
                print(df.transpose().median())
            self.show_vector()
        elif display_wish == "5":
            name = input("\nEnter vector's name which you want to delete.\n> ")
            if name in self.data[0]:
                insure_delete = input('''Enter "1" if you are sure you want to delete the vector.
                                         \rEnter anything else to return\n> ''')
                if insure_delete == "1":
                    del self.data[0][name]
                    with open(self.file_name, 'w') as file2:
                        js.dump(self.data, file2, indent=True)
                    print("\nVector was deleted.")
            else:
                print("\nThere is no saved vector with this name!")
            self.show_vector()
        else:
            self.show_or_manipulate_data()

    def show_matrix(self):
        """
        This function allows user to observe matrix part of database.
        :return: None
        """
        if self.data[1] == {}:
            print("There is no matrix data yet!")
            self.show_or_manipulate_data()
        self.print_all(7)
        display_wish2 = input("> ")
        if display_wish2 == "1":
            for i in self.data[1].items():
                print(f"\n{i[0]}:")
                if type(i[1][0]) is int:
                    print(i[1])
                else:
                    for x in i[1]:
                        print(np.array(x))
            self.show_matrix()
        elif display_wish2 == "2":
            name_matrix = input("\nEnter matrix name.\n> ")
            if name_matrix in self.data[1]:
                print("\nValue is: ")
                for i in self.data[1][name_matrix]:
                    print(np.array(i))
            else:
                self.print_all(10)
            self.show_matrix()
        elif display_wish2 == "3":
            name_matrix = input("\nEnter matrix name which you want to rename.\n> ")
            if name_matrix in self.data[1]:
                while True:
                    new_name = input("\nEnter the new name.\n> ")
                    if new_name in self.data[1]:
                        print("Matrix with this name already exists!")
                        self.show_matrix()
                    else:
                        self.data[1][new_name] = self.data[1].pop(name_matrix)
                        with open(self.file_name, 'w') as file2:
                            js.dump(self.data, file2, indent=True)
                        print("\nMatrix successfully renamed.")
                        break
            else:
                print("\nThere is no saved matrix with this name!")
            self.show_matrix()
        elif display_wish2 == "4":
            name = input("\nEnter matrix's name which you want to delete.\n> ")
            if name in self.data[1]:
                insure_delete = input('''Enter "1" if you are sure you want to delete the matrix.
                                         \rEnter anything else to return\n> ''')
                if insure_delete == "1":
                    del self.data[1][name]
                    with open(self.file_name, 'w') as file2:
                        js.dump(self.data, file2, indent=True)
                    print("\nMatrix was deleted.")
            else:
                print("\nThere is no saved matrix with this name!")
            self.show_matrix()
        else:
            self.show_or_manipulate_data()

    @classmethod
    def list_and_change_file(cls):
        """
        This function at the beginning allows user to choose file to store data.
        :return: File object.
        """
        while True:
            current_directory = os.getcwd()
            only_files = [f for f in os.listdir(current_directory) if op.isfile(op.join(current_directory, f))]
            list_of_files = []
            for i in only_files:
                if ".json" in i:
                    list_of_files.append(i)
            if len(list_of_files) == 0:
                print("\nNo json file. If you want to create one enter the name of the new file.")
            else:
                print("\nThese are all files you can store data in.")
                for i in list_of_files:
                    print(i)
            cls.print_all(9)
            file_name = input("> ") + ".json"
            if not op.exists(file_name):
                cls.print_all(5)
                create_file_wish = input("> ")
                if create_file_wish == "1":
                    with open(file_name, 'w+') as _file:
                        _file.write("[{}, {}]")
                    print(f'''\nFile {file_name} was created!''')
                    with open(file_name, 'r') as _file:
                        data = js.load(_file)
                else:
                    pass
            else:
                with open(file_name, 'r') as _file:
                    data = js.load(_file)
                break
        return cls(file_name, data)

    @staticmethod
    def plot_result(operation):
        """
        This function plots the vector either when calculations are done or user wants
        to display the vector and information about it from Json file.
        :param operation: Receives vector coordinates.
        :return: None
        """
        x_plot = [0, operation[0]]
        y_plot = [0, operation[1]]
        z_plot = [0, operation[2]]
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(x_plot, y_plot, z_plot, color='r')
        ax.quiver3D(0, 0, 0, operation[0], operation[1], operation[2],
                    color='r', arrow_length_ratio=0.1)
        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        ax.set_zlabel("Z axis")
        plt.show()

    @staticmethod
    def print_all(which_to_print):
        """
        This function prints everything when needed depending on part of the code.
        :param which_to_print: To decide what to print in different parts of code.
        :return: None
        """
        if which_to_print == 0:
            print('''\nIf you you want to do calculations with vectors enter "1".
                     \rIf you you want to do calculations with matrices enter "2".
                     \rIf you want to display information from database enter "3".
                     \rIf you want to return and choose another file enter "4".
                     \rIf you want to quit enter anything else.''')
        elif which_to_print == 1:
            print('''\nEnter "1" if you want to calculate the magnitude of the vector.
                     \rEnter "2" if you want to multiply vector by a scalar.
                     \rEnter "3" if you want to calculate the sum of two vectors.
                     \rEnter "4" if you want to calculate the subtraction of two vectors.
                     \rEnter "5" if you want to calculate the dot product of two vectors as a number.
                     \rEnter "6" if you want to calculate the dot product of two vectors as vector.
                     \rEnter "7" if you want to calculate the cross product of two vectors as number.
                     \rEnter "8" if you want to calculate the cross product of two vectors as vector.
                     \nIf you want to return to the main menu enter anything else.''')
        elif which_to_print == 2:
            print('''\nIf you want to return to the main menu enter "1".
                     \rIf if you want to quit enter anything else.''')
        elif which_to_print == 3:
            print('''\nEnter "1" if you want to display all data.
                     \rEnter "2" if you want to display particular vector.
                     \rEnter "3" if you want to rename some vector.
                     \rEnter "4" if you want to show statistics of the database. 
                     \rEnter "5" if you want to delete some vector from the database.
                     \rEnter anything else to return.''')
        elif which_to_print == 4:
            print('''\nEnter "1" to display general statistics of the database.
                     \rEnter "2" to display mean of column in database.
                     \rEnter "3" to display median of column in database.
                     \rEnter anything else to return.''')
        elif which_to_print == 5:
            print('''\nThere is no file with such name.
                     \nEnter "1" if you want to create a Json file with this name.
                     \rIf you want to return enter anything else.''')
        elif which_to_print == 6:
            print('''\nEnter "1" to add two matrices.
                     \rEnter "2" to subtract two matrices.
                     \rEnter "3" to multiply two matrices.
                     \rEnter "4" for calculating product of two matrices.
                     \rEnter "5" to divide two matrices.
                     \rEnter "6" to take the square root of a matrix.
                     \rEnter "7" to do column wise summation.
                     \rEnter "8" to do row wise summation.
                     \rEnter "9" to transpose matrix.
                     \nIf you want to return to the main menu enter anything else.''')
        elif which_to_print == 7:
            print('''\nEnter "1" to display all data.
                     \rEnter "2" to display particular matrix.
                     \rEnter "3" to rename matrix.
                     \rEnter "4" to remove matrix from database.
                     \rEnter anything else to return''')
        elif which_to_print == 8:
            print('''\nTo access vector database enter "1".
                     \rTo access matrix database enter "2".
                     \rTo return enter anything else.''')
        elif which_to_print == 9:
            print('''\nEnter the name of json file which you want to use (without extension).
                     \rOr to create a new file enter the name of new file.''')
        elif which_to_print == 10:
            print('''There is no saved matrix with this name!
                     \rPlease do some calculations and save data to use this function.''')
        elif which_to_print == 11:
            print('''There is no saved vector with this name!
                     \rPlease do some calculations and save data to use this function.''')
