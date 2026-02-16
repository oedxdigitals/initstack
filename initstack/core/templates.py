# initstack/core/templates.py
from initstack.core.plugins import load_plugins

def python_template():
    return {
        "src/__init__.py": "",
        "src/main.py": (
            "def main():\n"
            "    print('Hello from Initstack')\n\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        ),
        "tests/__init__.py": "",
        "README.md": "# Python Project\n",
        ".gitignore": "__pycache__/\n.env\n"
    }

def web_template():
    return {
        "index.html": "<!DOCTYPE html><html></html>",
        "css/style.css": "",
        "js/app.js": "",
        "README.md": "# Web Project\n"
    }

def cli_template():
    return {
        "app.py": "def main():\n    print('CLI app')\n",
        "README.md": "# CLI Project\n"
    }

TEMPLATES = {
    "python": python_template,
    "web": web_template,
    "cli": cli_template,
    "custom": lambda: {"README.md": "# Custom Project\n"},
}

def get_template(name):
plugins = load_plugins()
if name in plugins:
    base, meta = plugins[name]
    files = {}
    for dst, src in meta["files"].items():
        with open(base / src) as f:
            files[dst] = f.read()
    return files

def list_templates():
    return TEMPLATES.keys()
