import os
import yaml


def load_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def get_environment_config():
    env = os.getenv("ENV", "local")   # default = local

    all_envs = load_yaml("config/environments.yaml")

    if env not in all_envs:
        raise ValueError(f"Environment '{env}' not found in environments.yaml")

    return all_envs[env]