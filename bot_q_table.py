import gym
import gym
import keyboard
import matplotlib.pyplot as plt
import time
import random
import numpy as np
from typing import List
random.seed(0)
np.random.seed(0)
noe = 4000
discount_factor = 0.8
learning_rate = 0.9

report = "100 episodes Average %.2f, Best 100-ep average: %.2f (Episode %d)"

def print_report(rewards:List, episodes:int):
   print(report % (np.mean(rewards[-100:]), max([np.mean(rewards[i:i+100]) for i in range(len(rewards)-100)])))


# # Define the environment
# # env = gym.make('ALE/SpaceInvaders-v5', render_mode='human', full_action_space=False, repeat_action_probability=0.1, obs_type='rgb')
# # env.reset()

# # Define the action mappings (these may vary, consult the environment's action space)
# action_left = 3   # Typically for "left"
# action_right = 2  # Typically for "right"
# action_fire = 1   # Typically for "fire"
# action_noop = 0   # No action

# while True:
#     action = action_noop  # Default action is "no-op" (no action)

#     # Check keyboard input and update action accordingly
#     if keyboard.is_pressed('left'):
#         action = action_left
#     elif keyboard.is_pressed('right'):
#         action = action_right
#     elif keyboard.is_pressed('space'):
#         action = action_fire

#     # Take a step in the environment with the selected action
#     obs, reward, terminated, truncated, info = env.step(action)

#     # Check for end of episode
#     if terminated or truncated:
#         env.reset()  # Reset the environment if episode ends

#     time.sleep(0.05)  # Add a small delay to control the speed of gameplay

# env.close()
# env = gym.make('FrozenLake-v1', render_mode = 'human', full_action_space=True, repeat_action_probability=0.1, obs_type='rgb')  # Use the latest version of Space Invaders
#     env.seed(0)
# env = gym.make('ALE/Breakout-v5', render_mode = 'human', full_action_space=False, repeat_action_probability=0.1, obs_type='rgb')

def main():
    env = gym.make('FrozenLake-v1', render_mode = 'human', desc=None, map_name="4x4", is_slippery=True)  # Use the latest version of Space Invaders
    # env.seed(0)

    rewards = []
    # env.reset()
    Q = np.zeros((env.observation_space.n, env.action_space.n))
    for episode in range(1,noe+1):

        state = env.reset()
        episode_reward = 0

        while True:
            noise = np.random.random((1,env.action_space.n))/(episode**2)
            action = np.argmax(Q[state,:]+noise)  # Randomly select an action
            state2, reward, terminated,_ ,_= env.step(action)  # Update based on the latest Gym version
            Qtarget = reward+discount_factor*np.max(Q[state2,1])
            Q[state,action] = (1-learning_rate)*Q[state,action]+learning_rate*Qtarget
            episode_reward += reward
            state = state2
            if terminated:
                print("Total Reward:", episode_reward)
                rewards.append(episode_reward)
                break

    print_report(rewards,-1)


    # while True:
    #     #env.render()  # Render the environment (optional)
    #     # a = 0
    #     action = env.action_space.sample()  # Randomly select an action
    #     _, reward, terminated,_ ,_= env.step(action)  # Update based on the latest Gym version
    #     episode_reward += reward

    #     if terminated:
    #         print("Total Reward:", episode_reward)
    #         break

    #env.close()

if __name__ == "__main__":
    main()
