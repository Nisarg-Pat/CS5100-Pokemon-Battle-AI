from AI import Agents, QLearning


class AgentEnum:
    ManualAgent = Agents.ManualAgent
    RandomAgent = Agents.RandomAgent
    RandomAgentAttackOnly = Agents.RandomAgentAttackOnly
    RandomAgentSuperEffective = Agents.RandomAgentAttackOnlySuperEffective
    MinimaxAgent = Agents.MinimaxAgent
    Expectimax = Agents.Expectimax
    QLearningAgent = QLearning.ApproximateQAgent
