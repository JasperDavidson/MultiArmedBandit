import random
import numpy as np
import matplotlib.pyplot as plt

def multiArmedBandit(arms, epsilon, time_steps):
    arms = arms
    time_steps = time_steps
    epsilon = epsilon
    total_reward = 0
    mean_list = [5, 2, -5, -3, 4, 6, 1, 7, -1, 3]
    estimated_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    times_seen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(time_steps):
        explore_or_exploit = random.uniform(arms * epsilon, arms) - 1
        
        if explore_or_exploit <= arms * epsilon:
            action = random.randint(1, arms)  - 1
        else:
            action = estimated_values.index(max(estimated_values))

        reward = np.random.normal(loc=mean_list[action], scale=1, size=1)
        total_reward += reward
        times_seen[action] += 1
        estimated_values[action] = estimated_values[action] + (1 / times_seen[action]) * (reward - estimated_values[action])

        plt.plot(i, total_reward / i, color='green', linestyle='solid', linewidth=3, marker='.')

    plt.xlabel("Timesteps")
    plt.ylabel("Average Reward")
    plt.show()
