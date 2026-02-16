# initstack/utils/config.py
import os
import yaml

CONFIG_FILE = "initstack.yaml"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}

    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f) or {}
