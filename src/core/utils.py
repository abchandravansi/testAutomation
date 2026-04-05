from pathlib import Path
import time
import os
from datetime import datetime

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