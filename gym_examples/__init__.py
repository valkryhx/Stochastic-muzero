from gymnasium.envs.registration import register

register(
     id="MyGridWorld-v0",
     entry_point="gym_examples:GridWorldEnv",
     max_episode_steps=300,
)

from gym_examples.envs.grid_world import GridWorldEnv
