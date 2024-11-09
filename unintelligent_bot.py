import gym
import gym
import keyboard
import matplotlib.pyplot as plt
import time
import random

def main():
    env = gym.make('MountainCar-v0', render_mode = 'human', full_action_space=True, repeat_action_probability=0.1, obs_type='rgb')  # Use the latest version of Space Invaders
    env.reset()
    episode_reward = 0

    while True:
        #env.render()  # Render the environment (optional)
        # a = 0
        action = env.action_space.sample()  # Randomly select an action
        _, reward, terminated,_ ,_= env.step(action)  # Update based on the latest Gym version
        episode_reward += reward

        if terminated:
            print("Total Reward:", episode_reward)
            break

    env.close()

if __name__ == "__main__":
    main()