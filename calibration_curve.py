import numpy as np
import matplotlib.pyplot as plt

# Define the x, y data
channel = np.array([]) #write values here
energy = np.array([])  #write values here

# Calculate the slope and intercept of the regression line
slope, intercept = np.polyfit(channel, energy, 1)

# Create a scatter plot of the data
plt.scatter(channel, energy)

# Add the regression line to the plot
plt.plot(channel, slope * channel + intercept, color='red')

# Add labels to the plot
plt.xlabel('Channel Number')
plt.ylabel('Energy Level')
plt.title('Energy Calibration Plot')

# Show the plot
plt.show()

