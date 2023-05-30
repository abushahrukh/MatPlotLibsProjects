import matplotlib.pyplot as plt
import numpy as np

# Data for goals scored and opponents
home_goals = [2, 1, 1, 0]
away_goals = [0, 0, 0, 2,]
opponents = ['Rayo Vallencio', 'Getafe', 'Manchester City', 'Sevilla']

# Creating an array for the x-axis positions
x = np.arange(len(opponents))

# Width of each bar
bar_width = 0.35

# Plotting the grouped bars
plt.bar(x, home_goals, width=bar_width, label='Home', color='cyan')
plt.bar(x + bar_width, away_goals, width=bar_width, label='Away', color='lime')

# Customizing the plot
plt.xlabel('Opponents')
plt.ylabel('Number of Goals')
plt.title('Real Madrid Goals Scored against Different Opponents')
plt.xticks(x + bar_width/2, opponents, rotation=45)
plt.legend()

# Labeling the bars with opponent names and goals scored
for i, v in enumerate(home_goals):
    plt.text(i, v, str(v), ha='center', va='bottom')
for i, v in enumerate(away_goals):
    plt.text(i + bar_width, v, str(v), ha='center', va='bottom')

# Displaying the plot
plt.tight_layout()
plt.show()
