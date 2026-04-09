from core.utils import load_yaml, get_env

def load_env_config():
    env = get_env("ENV", "local")
    file_path = load_yaml("environments.yaml")
    return file_path.get(env, {})