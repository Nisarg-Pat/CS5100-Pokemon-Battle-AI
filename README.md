# Pokemon Battle AI
## Abstract

In this project, I implemented a console based Pokémon Battle simulator along with and various strategies to select 
best possible action for each turn and compared the performances. I implemented Greedy Agent, 
Minimax Agent, Expectimax Agent, and Approximate Q-Learning Agent. Out of these agents, 
the results showed that Expectimax performed well against opponent with Random Agent. 
Minimax performed well against opponent with Greedy Agent and Q-learning Agent performed 
well against both.

## Approach

The project required to implement a simulator for Poké-mon Battle from scratch. 
The first step was to collect the data about every Pokémon including their types, 
stats and moves they can learn. Data of moves and type matchups were also required. 
All the data required by the project was available at Kaggle.

I implemented an MVC console simulator that randomly selects a predefined number of 
Pokémon for each player with 4 random moves which they can learn. I implemented a Manual 
Agent that uses console for user input to select actions on each turn.

The damage is calculated in a similar way as it is calcu-lated in actual Pokémon games. 
The faster Pokémon gets to attack first and if a Pokémon is fainted, a new Pokémon should 
be switched.

Following a working simulator, I implemented the following strategies to select an action
1) **Epsilon Greedy**
This strategy follows a greedy strategy with a small chance of selecting a random action.
2) **Minimax**
The Minimax Agent used minimax algorithm with a depth of 2 to compute the best action.
3) **Expectimax**
The Expectimax Agent used expectimax algorithm with similar parameters as by minimax agent.
4) **Approximate Q-Learning**
A total of 18 different features were selected. State-only rewards were used: 0 if game not over, 
    100 for player winning states and -100 for losing or drawing states. 
    Number of learning games were set as 1000 but can be changed.

## How to Run

1) To run the game, open the src folder in command prompt:
   > cd src
2) Run the game
   > python game.py

## How to Use

Console Mode:

1) You and the opponent will be given a set of 3 random fully evolved Pokemon.
2) You can follow the command line prompts to battle with the computer.
3) You can change the agent by opening the game.py file and changing the agentTypes to any of the following 
ManualAgent, RandomAgent, RandomAgentAttackOnly, RandomAgentAttackOnlySuperEffective, MinimaxAgent, Expectimax or QLearning.ApproximateQAgent.

## Citations

1. Norvig, Peter, and Stuart Russell. Artificial Intelligence: A Modern Approach, Global Edition. 4th ed., Pearson, 2021.
2. Sutton, Richard, and Andrew Barto. Reinforcement Learning: An Introduction. Second edition, Cambridge, MA, MIT Press, 2018.
3. “Complete Competitive Pokémon Dataset.” Kaggle, 24 June 2018, www.kaggle.com/datasets/n2cholas/competitive-pokemon-dataset.
4. Kush Khosla, Lucas Li, Calvin Qi. Artificial Intelligence for Pokémon ´ Showdown. Stanford, CA: n.d. Web. 6 Dec. 2018.