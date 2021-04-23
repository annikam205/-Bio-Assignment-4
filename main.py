# Assignment 4, Annika Messer
# Link to GitHub https://github.com/annikam205/-Bio-Assignment-4

import pandas as pd

# Reading in from input.csv file
input_data = pd.read_csv('input.csv', sep=';', engine='python', skiprows=2, header=None)
input_data.columns = ['X', 'Y']
input_data = input_data.replace(',', '.', regex=True)

# Converting data from x and y columns to numeric values
x_axis = pd.to_numeric(input_data['X'], errors='raise', downcast=None)
y_axis = pd.to_numeric(input_data['Y'], errors='raise', downcast=None)

print(input_data)
print(x_axis)
print(y_axis)
