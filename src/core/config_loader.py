import yaml
from src.core.utils import get_config_path, get_env

def load_env_config():
    env = get_env("ENV", "local")
    file_path = get_config_path("environments.yaml")

    with open(file_path) as f:
        data = yaml.safe_load(f)

    return data.get(env, {})