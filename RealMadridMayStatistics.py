import numpy as np
import matplotlib.pyplot as plt


# Data for goals scored and conceded
goals_scored = [0,2,1,1,0,0,2,2]
goals_conceded = [2,1,1,0,4,1,1,1]

# Dates for each match in May
dates = [2,6,9,13,17,21,24,27]

# Plotting the data
plt.plot(dates, goals_scored, marker='o', label='Goals Scored')
plt.plot(dates, goals_conceded, marker='o', label='Goals Conceded')

# Customizing the plot
plt.xlabel('Match Dates')
plt.ylabel('Number of Goals')
plt.title('Real Madrid Goals Scored and Conceded in May')
plt.legend()

# Displaying the plot
plt.show()
