#!/usr/bin/env python3
"""Play an episode with a trained agent"""
import numpy as np


def play(env, Q, max_steps=100):
    """Has the trained agent play an episode

    env: the FrozenLakeEnv instance
    Q: numpy.ndarray containing the Q-table
    max_steps: maximum number of steps in the episode

    Each state of the board is displayed via the console and the agent
    always exploits the Q-table.

    Returns: the total rewards for the episode
    """
    state = env.reset()
    env.render()
    total = 0
    for _ in range(max_steps):
        action = np.argmax(Q[state])
        state, reward, done, _ = env.step(action)
        total += reward
        env.render()
        if done:
            break
    return total
