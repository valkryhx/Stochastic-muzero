from gym_examples.grid_world import GridWorldEnv
from gymnasium.envs.registration import register

register(
     id="GridWorld-v0",
     entry_point="gym_examples:GridWorldEnv",
     max_episode_steps=300,
)


