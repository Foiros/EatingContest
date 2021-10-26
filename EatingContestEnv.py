import pyglet
import gym
from gym import Env
from gym.spaces import Discrete
import random
import numpy as np
import Food


class EatingContest(Env):
    def __init__(self):
        # Eat either number one, two, three or four

        self.action_space = Discrete(4)
        # Temperature array from a another environment. What is our observation_space?
        # self.observation_space = Box(low=np.array([0]), high=np.array([100]))
        # Set all the different food
        self.foods = None
        self.foods = [Food.Food("Pork", 500, 5, False),
                      Food.Food("Chicken", -100, 2, True),
                      Food.Food("Fish", 250, 3, False),
                      Food.Food("Berry", -200, 3, True),
                      Food.Food("Cake", -500, 5, True),
                      Food.Food("Soup", 100, 1, False),
                      Food.Food("Cat Food", 50, 1, False),
                      Food.Food("Dog Food", -1000, 10, True)]

        # Create array for the food available each round
        self.currentFoods = []
        # Set starting score
        self.score = 0
        # Set contest timer
        self.contest_timer = 60

    def step(self, action: int):
        # First we randomize available food for this round
        for x in range(4):
            randomNumber = random.randrange(8)
            self.currentFoods.append(self.foods[randomNumber])

        # Next we look at the chosen action
        # Depending on the action number we consume a food
        # Consumed food applies its effects
        # If food is bad, it causes reward to be negative. Otherwise it will reward the AI
        if action == 0:
            self.score += self.currentFoods[0].getScoreValue()
            self.contest_timer -= self.currentFoods[0].get_time_lost()
            if self.currentFoods[0].getScoreValue() <= 0:
                reward = -1
            else:
                reward = 1
        elif action == 1:
            self.score += self.currentFoods[0].getScoreValue()
            self.contest_timer -= self.currentFoods[0].get_time_lost()
            if self.currentFoods[0].getScoreValue() <= 0:
                reward = -1
            else:
                reward = 1
        elif action == 2:
            self.score += self.currentFoods[0].getScoreValue()
            self.contest_timer -= self.currentFoods[0].get_time_lost()
            if self.currentFoods[0].getScoreValue() <= 0:
                reward = -1
            else:
                reward = 1
        elif action == 3:
            self.score += self.currentFoods[0].getScoreValue()
            self.contest_timer -= self.currentFoods[0].get_time_lost()
            if self.currentFoods[0].getScoreValue() <= 0:
                reward = -1
            else:
                reward = 1

        # If contest_timer is lower or equal to 0, the contest ends
        if self.contest_timer <= 0:
            done = True
        else:
            done = False

        # Before we end step sequence, we need to clear the contest of currentFoods
        # This mainly so that we don't increase the size of this array and cause errors
        self.currentFoods.clear()

        # Return step information, aka gained score, reward for doing right thing, if the episode is done
        return self.score, reward, done

    def render(self):
        # Implement visualization
        pass

    def reset(self):
        # When the episode is done, we reset score and contest_timer to their default values
        self.score = 0
        self.contest_timer = 60
