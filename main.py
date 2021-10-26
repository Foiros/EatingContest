
import EatingContestEnv as ece

env = ece.EatingContest()

# states = env.observation_space.shape
# actions = env.action_space.n

episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    totalScore = 0
    totalReward = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        score, reward, done = env.step(action)
        totalScore += score
        totalReward += reward

    print('Episode:{}, Score:{}, Reward:{}'.format(episode, totalScore, totalReward))




