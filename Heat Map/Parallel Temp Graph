import numpy as np
import matplotlib.pyplot as plt
# Set the value of dimensions (give them a number)
Dimension = int(12)
# Set value for samples
NumberOfSamples = int(3)
Scale = int(1000)
# Resize the figure to be clear and readable
plt.figure(figsize=(14, 4))
# All the 3 cities with their average monthly temperature
Plovdiv = np.array([0, 2, 6, 11, 16, 20, 22, 22, 17, 12, 7, 2], dtype=int)
Villahermosa = np.array([24, 25, 27, 29, 30, 29, 29, 29, 29, 27, 26, 24], dtype=int)
Melbourne = np.array([21, 22, 19, 16, 14, 12, 10, 12, 14, 15, 17, 19], dtype=int)
# Initialise a two-dimensional Numpy array containing the average monthly temperatures
Cities = np.array([Plovdiv, Villahermosa, Melbourne], dtype=int)
# Spine names
Name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# Draw the spines, their number and the color used
for i in range(0, Dimension):
    plt.vlines(i, 0, Scale, '#808080')
# Generate the parallel coordinates with different colour for each city
for i in range(0, 3):
    plt.plot(Name, Cities[0], '#E9841E')
for i in range(0, 3):
    plt.plot(Name, Cities[1], '#0BB611')
for i in range(0, 3):
    plt.plot(Name, Cities[2], '#1AA7EE')
# Label each city with the related color
plt.text(
    11.7, 1,
    s='Plovdiv',
    color='#E9841E',
    weight='bold',
    family='sans-serif',
    size=10)
plt.text(
    11.7, 23,
    s='Villahermosa',
    color='#0BB611',
    weight='bold',
    family='sans-serif',
    size=10)
plt.text(
    11.7, 12,
    s='Melbourne',
    color='#1AA7EE',
    weight='bold',
    family='sans-serif',
    size=10)
# Label a Header to style the graph
plt.text(
    6, 33,
    s='Monthly Average Temperature from Cities of - Plovdiv, Villahermosa and Melbourne in Parallel Coordinates',
    color='#696969',
    weight='bold',
    verticalalignment='bottom',
    horizontalalignment='center',
    family='sans-serif',
    size=10)
# Give a details about some values on the graph
plt.text(
    -1, 6,
    s='Average Temperature in °C',
    color='#000000',
    weight='normal',
    verticalalignment='bottom',
    horizontalalignment='center',
    rotation=90,
    family='sans-serif',
    size=9)
plt.show()
