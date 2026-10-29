#!/usr/bin/env python3
"""Trains a DQN agent to play Atari's Breakout with keras-rl"""
import gym
import numpy as np
from PIL import Image
from keras.layers import Conv2D, Dense, Flatten, Permute
from keras.models import Sequential
from keras.optimizers import Adam
from rl.agents.dqn import DQNAgent
from rl.callbacks import ModelIntervalCheckpoint
from rl.core import Processor
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy, LinearAnnealedPolicy

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


def build_model(nb_actions):
    """Builds the policy network

    nb_actions: number of actions available in the environment

    Returns: the keras model
    """
    model = Sequential()
    model.add(Permute((2, 3, 1), input_shape=(WINDOW_LENGTH,) + INPUT_SHAPE))
    model.add(Conv2D(32, (8, 8), strides=(4, 4), activation='relu'))
    model.add(Conv2D(64, (4, 4), strides=(2, 2), activation='relu'))
    model.add(Conv2D(64, (3, 3), strides=(1, 1), activation='relu'))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(nb_actions, activation='linear'))
    return model


if __name__ == '__main__':
    env = gym.make(ENV_NAME)
    np.random.seed(123)
    env.seed(123)
    nb_actions = env.action_space.n

    model = build_model(nb_actions)
    memory = SequentialMemory(limit=200000, window_length=WINDOW_LENGTH)
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps',
                                  value_max=1., value_min=.1, value_test=.05,
                                  nb_steps=1000000)
    dqn = DQNAgent(model=model, nb_actions=nb_actions, policy=policy,
                   memory=memory, processor=AtariProcessor(),
                   nb_steps_warmup=50000, gamma=.99,
                   target_model_update=10000, train_interval=4,
                   delta_clip=1.)
    dqn.compile(Adam(lr=.00025), metrics=['mae'])

    checkpoint = ModelIntervalCheckpoint('dqn_weights_{step}.h5f',
                                         interval=250000)
    dqn.fit(env, nb_steps=2000000, callbacks=[checkpoint],
            log_interval=10000, visualize=False, verbose=2)

    dqn.model.save('policy.h5')
