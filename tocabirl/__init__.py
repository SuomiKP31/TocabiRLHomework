from .policies import FixedStdActorCriticPolicy
from stable_baselines3 import PPO

PPO.policy_aliases["FixedStddevMlpPolicy"] = FixedStdActorCriticPolicy