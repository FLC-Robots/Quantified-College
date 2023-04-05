import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Assuming 'df' is the DataFrame created from the provided data (as in the previous responses)
df = pd.read_csv('/Users/colincasey/Documents/GitHub/Quantified-College/Data/Raw/data.csv')
# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Set plot labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Significant Wave Height (m)')
ax.set_title('Animated Time-series plot: Significant Wave Height')

# Function to update the plot
def update(num):
    ax.clear()
    ax.set_xlabel('Time')
    ax.set_ylabel('Significant Wave Height (m)')
    ax.set_title('Animated Time-series plot: Significant Wave Height')
    ax.plot(df.index[:num], df['Significant Wave Height (m)'][:num])

# Create the animation with a 1-second interval between frames and a repeating loop
ani = FuncAnimation(fig, update, frames=len(df), interval=1000, repeat=True)

# Show the plot
plt.show()
