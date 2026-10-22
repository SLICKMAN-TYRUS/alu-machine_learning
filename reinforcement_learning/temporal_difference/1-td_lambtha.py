#!/usr/bin/env python3
"""TD(lambda) algorithm"""
import numpy as np


def td_lambtha(env, V, policy, lambtha, episodes=5000, max_steps=100,
               alpha=0.1, gamma=0.99):
    """Performs the TD(lambda) algorithm

    env: the openAI environment instance
    V: numpy.ndarray of shape (s,) containing the value estimate
    policy: function that takes in a state and returns the next action
    lambtha: the eligibility trace factor
    episodes: total number of episodes to train over
    max_steps: maximum number of steps per episode
    alpha: the learning rate
    gamma: the discount rate

    Returns: V, the updated value estimate
    """
    for _ in range(episodes):
        state = env.reset()
        trace = np.zeros_like(V)
        for _ in range(max_steps):
            action = policy(state)
            new_state, reward, done, _ = env.step(action)
            trace *= lambtha * gamma
            trace[state] += 1
            delta = reward + gamma * V[new_state] - V[state]
            V += alpha * delta * trace
            if done:
                break
            state = new_state
    return V
