from pathlib import Path
import json

PLUGIN_DIRS = [
    Path.cwd() / ".initstack/templates",
    Path.home() / ".initstack/templates"
]

def load_plugins():
    plugins = {}

    for base in PLUGIN_DIRS:
        if not base.exists():
            continue

        for tpl in base.iterdir():
            cfg = tpl / "template.json"
            if cfg.exists():
                with open(cfg) as f:
                    data = json.load(f)
                plugins[data["name"]] = (tpl, data)

    return plugins
