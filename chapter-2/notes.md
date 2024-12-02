# Chapter 2
**k-armed**: you have k number of levers and the action has an expected mean rewards

By introducing $\epsilon$, we are able to allow for exploration which after many steps allows for increased gains in average rewards and percent of optimal action. The value for epsilon needs to be scaled in regards to the reward's variance.

**Nonstationarity**: the values for each action is changing. An example is the reward for giving a person a coupon. the customer will get used to it so the reward drop over time.
### 2.1
The probability that the greedy action will be selected is **0.75** because:

- **50% of the time** $(ϵ=0.5)$ we will pick a random action. Since there are two actions, the greedy action will be chosen with a probability of $0.5$ during this random selection.
- The remaining **50% of the time** $(1−ϵ=0.5)$, we will deterministically pick the greedy action.

Thus, the total probability of selecting the greedy action is:

$P(greedy action)=0.5⋅1+0.5⋅0.5=0.75$


**Final Answer:** The probability that the greedy action is selected is **0.75**.

### 2.2
Exploration definitely occurred in steps 4 and 5 and it may have occured on steps 1-4

### 2.3
$0.99*1 + 0.01*0.1 = 0.991$ because 99% of the time we will pick the best option and 1% of the time, we explore and the chance that we get the best option is 0.1

For $\epsilon = 0.1$, we have $0.9*1+0.1*0.1 = 0.91$

### 2.4
