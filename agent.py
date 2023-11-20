# Simple reflex agent
# Based on the agent in Figure 2.10 of Artificial Intelligence: A Modern Approach (4th Edition) by Stuart Russell and Peter Norvig
import matplotlib.pyplot as plt
import numpy as np

class SimpleReflexAgent:
    def __init__(self, environment):
        self.environment = environment
        self.location = (0, 0)

    # The agent's perception is a tuple of two values (dx, dy), or None if the agent is stuck.
    def sensor(self):
        x, y = self.location
        print(f"Current location: ({x}, {y})")
        if y < len(self.environment[0]) - 1:
            if self.environment[x][y + 1] == 1:
                if x < len(self.environment) - 1:
                    if self.environment[x + 1][y] == 1:
                        return None # If there is an obstacle to the right and below
                    else:
                        return (1, 0) # If there is an obstacle to the right but not below
            else:
                return (0, 1) # If there is no obstacle to the right
        elif x < len(self.environment) - 1:
            if self.environment[x + 1][y] == 1:
                return None
            else:
                return (1, 0)
        else:
            return None # If at the bottom right corner of the environment

    # The agent's action returns a boolean value indicating whether the agent is able to continue moving.
    def actuator(self, perception):
        if perception == None:
            print("Agent is stuck!")
            return False
        else:
            x, y = self.location
            dx, dy = perception
            self.location = (x + dx, y + dy)
            print(f"Moving to: ({x + dx}, {y + dy})\n")
            return True

# Example environment: a 2D square grid representing obstacles (1) and empty spaces (0).

environment = [
    #0  1  2  3  4  5
    [0, 1, 0, 0, 0, 0], # 0
    [0, 0, 1, 1, 0, 1], # 1
    [1, 0, 0, 0, 0, 1], # 2
    [0, 0, 1, 0, 0, 0], # 3
    [0, 0, 0, 0, 0, 0], # 4
    [0, 0, 0, 0, 0, 1]  # 5
]

# Create an instance of the agent
agent = SimpleReflexAgent(environment)

# Demonstrate the agent's actions
print("Initial location: (0, 0)\n")
steps = [(0,0)]
flag = True
while flag:
    perception = agent.sensor()
    flag = agent.actuator(perception)
    if flag:
        steps.append(agent.location)

# Define colors
colors = { 0: 'white', 1: 'red' }

# Function to visualize the environment and path
def visualize_path(environment, path):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(-0.5, len(environment[0]), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(environment), 1), minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
    ax.tick_params(which="minor", size=0)

    for i in range(len(environment)):
        for j in range(len(environment[0])):
            color = colors[environment[i][j]]
            ax.add_patch(plt.Rectangle((j - 0.5, len(environment) - i - 1 - 0.5), 1, 1, fill=True, color=color))

    for step in path:
        ax.plot(step[1], len(environment) - step[0] - 1, marker='o', markersize=8, color='green')

    plt.title("Agent's Path")
    plt.show()

visualize_path(environment, steps)