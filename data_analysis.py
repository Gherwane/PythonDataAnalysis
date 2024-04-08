'''
Created on Apr 18, 2022

@author: gherwane
'''
import pandas as pd
import matplotlib.pyplot as plt
print(" ********** Welcome to the Python Data Analysis App ********** ")
def population_data():
    """The population data analysis"""
    print("You have entered Population Data")
    reader = pd.read_csv("PopChange.csv")
    while True:
        print("Select the Column you want to analyze:")
        print("a. Pop Apr 1")
        print("b. Pop Jul 1")
        print("c. Change Pop")
        print("d. Exit Column")
        population_choice = str(input("")).lower().strip()
        if population_choice == "a":
            print("You selected Pop Apr 1")
            print("The statistics of this column are:")
            print("Count =             " , reader["Pop Apr 1"].count())
            print("Mean =               " , reader["Pop Apr 1"].mean())
            print("Standard Deviation = " , reader["Pop Apr 1"].std())
            print("Min =                " , reader["Pop Apr 1"].min())
            print("Max =                " , reader["Pop Apr 1"].max())
            print("The Histogram of this column is now displayed.")
            plt.hist(reader["Pop Apr 1"])
            plt.grid()
            plt.title("Pop Apr 1")
            plt.show()
        elif population_choice == "b":
            print("You selected Pop Jul 1")
            print("The statistics of this column are:")
            print("Count =              " , reader["Pop Jul 1"].count())
            print("Mean =               " , reader["Pop Jul 1"].mean())
            print("Standard Deviation = " , reader["Pop Jul 1"].std())
            print("Min =                " , reader["Pop Jul 1"].min())
            print("Max =                " , reader["Pop Jul 1"].max())
            print("The Histogram of this column is now displayed.")
            plt.hist(reader["Pop Jul 1"])
            plt.grid()
            plt.title("Pop Jul 1")
            plt.show()
        elif population_choice == "c":
            print("You selected Change Pop")
            print("The statistics of this column are:")
            print("Count =              " , reader["Change Pop"].count())
            print("Mean =               " , reader["Change Pop"].mean())
            print("Standard Deviation = " , reader["Change Pop"].std())
            print("Min =                " , reader["Change Pop"].min())
            print("Max =                " , reader["Change Pop"].max())
            print("The Histogram of this column is now displayed.")
            plt.hist(reader["Change Pop"])
            plt.grid()
            plt.title("Change Pop")
            plt.show()
        elif population_choice == "d":
            print("You selected to exit the column menu")
            break
        else:
            print("Invalid entry...try again")
def housing_data():
    """ Housing data analysis"""
    print("You have entered Housing Data")
    reader = pd.read_csv("Housing.csv")
    while True:
        print("Select the Column you want to analyze:")
        print("a. Age")
        print("b. Bedrooms")
        print("c. Built")
        print("d. Rooms")
        print("e. Utility")
        print("f. Exit")
        housing_choice = str(input("")).lower().strip()
        if housing_choice == "a":
            print("You selected Age")
            print("The statistics of this column are:")
            print("Count =              " , reader["AGE"].count())
            print("Mean =              " , reader["AGE"].mean())
            print("Standard Deviation = " , reader["AGE"].std())
            print("Min =                " , reader["AGE"].min())
            print("Max =                " , reader["AGE"].max())
            print("The Histogram of this column is now displayed.")
            plt.hist(reader["AGE"])
            plt.grid()
            plt.title("Age")
            plt.show()
        elif housing_choice == "b":
            print("You selected Bedrooms")
            print("The statistics of this column are:")
            print("Count =              " , reader["BEDRMS"].count())
            print("Mean =              " , reader["BEDRMS"].mean())
            print("Standard Deviation = " , reader["BEDRMS"].std())
            print("Min =               " , reader["BEDRMS"].min())
            print("Max =               " , reader["BEDRMS"].max())
            print("The Histogram of this column is now displayed.")
            plt.hist(reader["BEDRMS"])
            plt.grid()
            plt.title("Bedrooms")
            plt.show()
        elif housing_choice == "c":
            print("You selected Built")
            print("The statistics of this column are:")
            print("Count =              " , reader["BUILT"].count())
            print("Mean =               " , reader["BUILT"].mean())
            print("Standard Deviation = " , reader["BUILT"].std())
            print("Min =                " , reader["BUILT"].min())
            print("Max =                " , reader["BUILT"].max())
            print("The Histogram of this column is now displayed.")
            plt.hist(reader["BUILT"])
            plt.grid()
            plt.title("Built")
            plt.show()
        elif housing_choice == "d":
            print("You selected Rooms")
            print("The statistics of this column are:")
            print("Count =              " , reader["ROOMS"].count())
            print("Mean =               " , reader["ROOMS"].mean())
            print("Standard Deviation = " , reader["ROOMS"].std())
            print("Min =                " , reader["ROOMS"].min())
            print("Max =                " , reader["ROOMS"].max())
            plt.hist(reader["ROOMS"])
            plt.grid()
            plt.title("Rooms graph")
            plt.show()
        elif housing_choice == "e":
            print("You selected Utility")
            print("The statistics of this column are:")
            print("Count =              " , reader["UTILITY"].count())
            print("Mean =               " , reader["UTILITY"].mean())
            print("Standard Deviation = " , reader["UTILITY"].std())
            print("Min =                " , reader["UTILITY"].min())
            print("Max =                " , reader["UTILITY"].max())
            plt.hist(reader["UTILITY"])
            plt.grid()
            plt.title("Utility")
            plt.show()
        elif housing_choice == "f":
            print("f. You selected to exit the column menu")
            break
        else:
            print("Invalid entry...try again")
while True:#prompt
    print("Select the file you want to analyze: ")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program")
    while True:
        try:
            choice = int(input())
            break
        except ValueError:
            print("Invalid entry...try again")
    if choice == 1:
        print("")
        population_data()
    elif choice == 2:
        print("")
        housing_data()
    elif choice == 3:
        print("********** Thanks for using the Data Analysis App **********")
        break
    else:
        print("Invalid entry...try again")
