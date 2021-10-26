
import EatingContestEnv as ece

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


def build_model(states, actions):
    model = Sequential()
    model.add(Dense(24, activation='relu', input_shape=states))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model


def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                  nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
    return dqn


env = ece.EatingContest()
states = env.observation_space.shape
actions = env.action_space.n

model = build_model(states, actions)
model.summary()

agent = build_agent(model, actions)
agent.compile(Adam(lr=1e-3), metrics=['mae'])
agent.fit(env, nb_steps=50000, visualize=False, verbose=1)

scores = agent.test(env, nb_episodes=10, visualize=False)
print(np.mean(scores.history['episode_reward']))
