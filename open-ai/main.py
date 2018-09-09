# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 01:19:07 2018

@author: shuchowdhury
"""

from Agent import Agent
from Monitor import interact
import gym
import numpy as np

env = gym.make('Taxi-v2')
agent = Agent()
avg_rewards, best_avg_reward = interact(env, agent, num_episodes=30000)