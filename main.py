# Assignment 4, Annika Messer
# Link to GitHub https://github.com/annikam205/-Bio-Assignment-4

import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# Reading in from input.csv file
input_data = pd.read_csv('input.csv', sep=';', engine='python', skiprows=2, header=None)
input_data.columns = ['X', 'Y']
input_data = input_data.replace(',', '.', regex=True)

# Converting data from x and y columns to numeric values
x_axis = pd.to_numeric(input_data['X'], errors='raise', downcast=None)
y_axis = pd.to_numeric(input_data['Y'], errors='raise', downcast=None)

# Creating a scatter plot
figure_1 = px.scatter(x=x_axis, y=y_axis)
figure_1.update_layout(title={
        'text': "Scatter plot of input.csv data",
        'y': 1.0,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
figure_1.show()

X = input_data.values
figure_2 = ff.create_dendrogram(X, orientation='right')
figure_2.update_layout(width=1200, height=700)
figure_2.update_layout(title={
        'text': "Dendrogram",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
figure_2.show()
