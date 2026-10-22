#!/usr/bin/env python3
"""Monte Carlo algorithm"""
import numpy as np


def monte_carlo(env, V, policy, episodes=5000, max_steps=100, alpha=0.1,
                gamma=0.99):
    """Performs the Monte Carlo algorithm

    env: the openAI environment instance
    V: numpy.ndarray of shape (s,) containing the value estimate
    policy: function that takes in a state and returns the next action
    episodes: total number of episodes to train over
    max_steps: maximum number of steps per episode
    alpha: the learning rate
    gamma: the discount rate

    Returns: V, the updated value estimate
    """
    for i in range(episodes):
        state = env.reset()
        episode = []
        for _ in range(max_steps):
            action = policy(state)
            new_state, reward, done, _ = env.step(action)
            episode.append([state, action, reward, new_state])
            if done:
                break
            state = new_state
        episode = np.array(episode, dtype=int)
        G = 0
        for step in episode[::-1]:
            state, _, reward, _ = step
            G = reward + gamma * G
            if state not in episode[:i, 0]:
                V[state] = V[state] + alpha * (G - V[state])
    return V
