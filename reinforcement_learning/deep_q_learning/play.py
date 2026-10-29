#!/usr/bin/env python3
"""Displays a game of Atari's Breakout played by the trained DQN agent"""
import gym
import numpy as np
from PIL import Image
from keras.models import load_model
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.core import Processor
from rl.memory import SequentialMemory
from rl.policy import GreedyQPolicy

ENV_NAME = 'BreakoutDeterministic-v4'
INPUT_SHAPE = (84, 84)
WINDOW_LENGTH = 4


class AtariProcessor(Processor):
    """Preprocesses Atari frames and rewards for the agent"""

    def process_observation(self, observation):
        """Resizes a frame to 84x84 and converts it to grayscale"""
        img = Image.fromarray(observation)
        img = img.resize(INPUT_SHAPE).convert('L')
        return np.array(img).astype('uint8')

    def process_state_batch(self, batch):
        """Scales a batch of states to the range [0, 1]"""
        return batch.astype('float32') / 255.

    def process_reward(self, reward):
        """Clips the reward to the range [-1, 1]"""
        return np.clip(reward, -1., 1.)


if __name__ == '__main__':
    env = gym.make(ENV_NAME)
    np.random.seed(123)
    env.seed(123)
    nb_actions = env.action_space.n

    model = load_model('policy.h5', compile=False)
    memory = SequentialMemory(limit=1000, window_length=WINDOW_LENGTH)
    dqn = DQNAgent(model=model, nb_actions=nb_actions,
                   policy=GreedyQPolicy(), memory=memory,
                   processor=AtariProcessor(), nb_steps_warmup=0)
    dqn.compile(Adam(lr=.00025), metrics=['mae'])

    dqn.test(env, nb_episodes=5, visualize=True)
