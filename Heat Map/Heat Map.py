# Heat map optimised for PyCharm in full-screen mode
import numpy as np
import matplotlib.pyplot as plt
# This subroutine encapsulates the 'plot' method, as the most suitable for raster rendering
def DrawBox(x, y, size, r, g, b):
    for i in range(0, int(size)):
        if r < 0:
            r = int(0)
        if r > 255:
            r = int(255)
        if g < 0:
            g = int(0)
        if g > 255:
            g = int(255)
        if b < 0:
            b = int(0)
        if b > 255:
            b = int(255)
        plt.plot([x, x + size], [y + i, y + i], '#{:02x}{:02x}{:02x}'.format(r, g, b))
# Initialise NumPy arrays containing the average monthly temperatures for 3 cities
City1 = np.array([0, 2, 6, 11, 16, 20, 22, 22, 17, 12, 7, 2], dtype=int)
City2 = np.array([24, 25, 27, 29, 30, 29, 29, 29, 29, 27, 26, 24], dtype=int)
City3 = np.array([21, 22, 19, 16, 14, 12, 10, 12, 14, 15, 17, 19], dtype=int)
# Initialise a two-dimensional NumPy array containing the average monthly temperatures
Cities = np.array([City1, City2, City3], dtype=int)
# Extract the minimum and the maximum values
Min = np.min(Cities)
Max = np.max(Cities)
# Setup the plotting area
    #Also, added figure ratio in order to keep it compact
plt.figure(figsize=(8, 4))
plt.axis([0, 960, 0, 380])
plt.xticks([])
plt.yticks([])
# Initialise box size and offsets
BoxSize = int(50)
OffsetX = int(15)
OffsetY = int(15)
    # Input method to collects input value
Threashold = int(0)
Threashold = int(input('Enter threshold value: '))
# Visualise the heat map
for i in range(0, Cities.shape[0]):
    for j in range(0, Cities.shape[1]):
        ColourCode = int(((Cities[i, j]-Min)/(Max-Min))*256)
        if Cities[i, j] > Threashold:
            DrawBox(210+BoxSize*j, 210 - BoxSize*i, BoxSize, ColourCode, 0, 0)
        else:
            DrawBox(210 + BoxSize * j, 210 - BoxSize * i, BoxSize,  0, 0,ColourCode)
        plt.text(OffsetX+207+BoxSize*j, OffsetY+210-BoxSize*i, str(Cities[i, j]), color='white')
# Visualise the colour scale
    #Max Scale(red)
for i in range(0, 100):
    plt.plot([825, 850], [i + 190, i + 190], '#{:02x}{:02x}{:02x}'.format(int((i / 100) * 256), 0, 0))
plt.text(860, 270, str(Max))
    #Min Scale(blue)
for i in range(0, 80):
    plt.plot([825, 850], [i + 110, i + 110], '#{:02x}{:02x}{:02x}'.format(0, 0, int(((80 - i) / 256) * 795)))
plt.text(860, 110, str(Min))
# Print the names of the months with the respectively attributes
plt.text(215, 270, 'Jan', weight='bold', rotation=25, size=10)
plt.text(265, 270, 'Feb', weight='bold', rotation=25, size=10)
plt.text(315, 270, 'Mar', weight='bold', rotation=25, size=10)
plt.text(365, 270, 'Apr', weight='bold', rotation=25, size=10)
plt.text(415, 270, 'May', weight='bold', rotation=25, size=10)
plt.text(470, 270, 'Jun', weight='bold', rotation=25, size=10)
plt.text(525, 270, 'Jul', weight='bold', rotation=25, size=10)
plt.text(565, 270, 'Aug', weight='bold', rotation=25, size=10)
plt.text(615, 270, 'Sep', weight='bold', rotation=25, size=10)
plt.text(665, 270, 'Oct', weight='bold', rotation=25, size=10)
plt.text(715, 270, 'Nov', weight='bold', rotation=25, size=10)
plt.text(765, 270, 'Dec', weight='bold', rotation=25, size=10)
# Print the names of the Cities with the respectively attributes
plt.text(20, 230, 'Plovdiv', weight='bold', size=10)
plt.text(20, 180, 'Villahermosa', weight='bold', size=10)
plt.text(20, 130, 'Melbourne', weight='bold', size=10)
# Print the Heat Map Description
plt.text(
    480, 20,
    s='Heat Map for cities of\n Plovdiv(BG), Villahermosa(MEX), Melbourne(AU) ',
    color='#696969',
    weight='bold',
    verticalalignment='bottom',
    horizontalalignment='center',
    rotation=0,
    family='sans-serif',
    size=10)

plt.show()
