from initstack.core.plugins import load_plugins


# Built-in templates
BUILTIN_TEMPLATES = {
    "python": {
        "src": {},
        "tests": {},
        "README.md": "",
        "pyproject.toml": ""
    },
    "cli": {
        "cli": {},
        "README.md": "",
        "pyproject.toml": ""
    },
    "web": {
        "public": {},
        "src": {},
        "README.md": ""
    }
}


def get_template(name: str):
    name = name.lower()

    # Built-in templates
    if name in BUILTIN_TEMPLATES:
        return BUILTIN_TEMPLATES[name]

    # Plugin templates
    plugins = load_plugins()
    if name in plugins:
        return plugins[name]

    raise ValueError(f"Unknown template: {name}")


def list_templates():
    templates = set(BUILTIN_TEMPLATES.keys())

    plugins = load_plugins()
    templates.update(plugins.keys())

    return sorted(templates)
