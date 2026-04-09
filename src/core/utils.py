from pathlib import Path
import time
import os
from datetime import datetime
import yaml

def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_env(key, default=None):
    return os.getenv(key, default)

def retry(func, retries=3, delay=2):
    for _ in range(retries):
        try:
            return func()
        except Exception:
            time.sleep(delay)
    raise

def get_project_root():
    return Path(__file__).resolve().parents[2]


def get_config_path(filename):
    return get_project_root() / "config" / filename

def load_yaml(filename):
    file_path = get_config_path(filename)

    with open(file_path) as f:
        return yaml.safe_load(f)
    

def load_capabilities(platform, profile="default"):
    caps_path = get_project_root() / "config" / "capabilities" / f"{platform}.yaml"

    if not caps_path.exists():
        raise FileNotFoundError(f"{platform}.yaml not found")

    data = load_yaml(caps_path)

    if profile not in data:
        raise ValueError(f"Profile '{profile}' not found in {platform}.yaml")

    return data[profile]