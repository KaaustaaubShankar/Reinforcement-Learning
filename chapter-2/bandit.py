import numpy as np
import matplotlib.pyplot as plt

k = 10
steps = 2000
runs = 5
epsilon = 0.1
alpha = 0.1
q_star_walk_std = 0.01

def run_bandit(sample_average=False):
    avg_rewards, optimal_action_counts = np.zeros(steps), np.zeros(steps) #rewards for each step, and how often we get optimal actions
    for run in range(runs):
        q_star, q_est = np.zeros(k), np.zeros(k) #true rewards, estimated rewards
        action_counts = np.zeros(k) #how many times we call the action
        rewards = []
        optimal_actions_per_run = []

        for step in range(steps):
            q_star += np.random.normal(0, q_star_walk_std, k) #generating the mean reward for each k action
            optimal_action = np.argmax(q_star) 

            if np.random.rand() < epsilon:
                action = np.random.choice(k) #pick a random option for exploration
            else:
                action = np.argmax(q_est) # pick the optimal action based off of estimated

            reward = np.random.normal(q_star[action], 1) #getting the reward
            action_counts[action] += 1 #used for sample average

            if sample_average:
                step_size = 1 / action_counts[action] # 1-n
            else:
                step_size = alpha

            q_est[action] += step_size * (reward - q_est[action]) #q_{n+1} = Q_n + alpha or 1/n * (R_n - Q_n)

            rewards.append(reward)
            optimal_actions_per_run.append(action == optimal_action)

        avg_rewards += rewards
        optimal_action_counts += optimal_actions_per_run

    return avg_rewards / runs, optimal_action_counts / runs * 100

avg_rewards_sa, opt_actions_sa = run_bandit(sample_average=True)
avg_rewards_cs, opt_actions_cs = run_bandit(sample_average=False)


plt.figure(figsize=(12, 5))

# Average reward
plt.subplot(1, 2, 1)
plt.plot(avg_rewards_sa, label='Sample Average')
plt.plot(avg_rewards_cs, label='Constant Step Size')
plt.xlabel('Steps')
plt.ylabel('Average Reward')
plt.legend()

# Optimal action %
plt.subplot(1, 2, 2)
plt.plot(opt_actions_sa, label='Sample Average')
plt.plot(opt_actions_cs, label='Constant Step Size')
plt.xlabel('Steps')
plt.ylabel('% Optimal Action')
plt.legend()

plt.suptitle('Sample Average vs Constant Step Size in Nonstationary Bandit')
plt.tight_layout()
plt.show()
