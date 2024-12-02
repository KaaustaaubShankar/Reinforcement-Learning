# Chapter 1
**Temporal Difference Learning**: we keep track of a state's value in a dictionary and we modify the state's value by calculating the difference in value between a state and its previous state. This difference is then uåsed to back propagate these changes to the previous states. Each state is identified by a hashed value that represents the grid so there are less than 19683 states to memorize.

Examples of Estimations
| State Hash | Value Estimation |
|------------|------------------|
| 9841.0     | 0.506354         |
| 16402.0    | 0.500000         |
| 14215.0    | 0.509874         |
| 14944.0    | 0.499500         |
| 14701.0    | 0.523002         |

where 9841 is 111111111 in base 3 or an empty board 


## Exercises
### 1.1
In this case, the algorithm would not be model free because we are teaching how to play against itself. I believe we would have a better understanding of states that it would play but much of the state space or feature space would not be explored

### 1.2
We can make the play symmetric by hashing the states differently. This may be advantageous as it will make training shorter and reduce the number of "states" needed to be explored.

### 1.3
Worse because it did not explore at all. It would just get really good at playing one way. It would only follow one path outlined in **states** 

### 1.4
With exploratory, the understanding will be a generalized understanding of states and their values but without exploratory, the understanding will be more biased but still general since we will be backpropogating the changes in error based off of the differences. I think the second will be more likely since learning while exploring may push the estimations from the global minima (dont know if this is the correct term)

### 1.5
We can make the reward function favor wins by reducing the reward for draws after it ended. This may help drive win rates up but it also may not work out because most tic-tac-toe games end in a draw so the model may end up losing more games because it doesn't know how to draw.



