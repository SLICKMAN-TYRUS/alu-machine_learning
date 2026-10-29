#!/usr/bin/env python3
"""Load the FrozenLake environment"""
import gym


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """Loads the pre-made FrozenLakeEnv environment from OpenAI's gym

    desc: None or a list of lists containing a custom map description
    map_name: None or a string containing the pre-made map to load
    is_slippery: boolean, determines if the ice is slippery

    If both desc and map_name are None, the environment loads a randomly
    generated 8x8 map.

    Returns: the environment
    """
    return gym.make('FrozenLake-v0', desc=desc, map_name=map_name,
                    is_slippery=is_slippery)
