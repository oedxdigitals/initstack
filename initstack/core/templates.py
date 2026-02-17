import json
import os
from pathlib import Path
from jsonschema import validate, ValidationError

# Built-in templates directory
BUILTIN_DIR = Path(__file__).parent / "builtin"

# User plugin directory
PLUGIN_DIR = Path(os.path.expanduser("~/.initstack/plugins"))

# Load JSON schema
from initstack.core.schema import template_schema


def _load_template_from_dir(template_dir: Path):
    """
    Load and validate a template from a directory.
    Expects template.json inside the directory.
    """
    template_file = template_dir / "template.json"

    if not template_file.exists():
        return None

    try:
        with open(template_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"⚠ Failed to parse {template_file}: {e}")
        return None

    # Schema validation
    try:
        validate(instance=data, schema=template_schema)
    except ValidationError as e:
        print(f"⚠ Invalid template.json in {template_dir.name}: {e.message}")
        return None

    # Name consistency
    name = data.get("name")
    if not name:
        print(f"⚠ Template in {template_dir} missing 'name'")
        return None

    return name, data


def load_builtin_templates():
    templates = {}

    if not BUILTIN_DIR.exists():
        return templates

    for item in BUILTIN_DIR.iterdir():
        if not item.is_dir():
            continue

        result = _load_template_from_dir(item)
        if result:
            name, data = result
            templates[name] = data

    return templates


def load_plugins():
    templates = {}

    if not PLUGIN_DIR.exists():
        return templates

    for item in PLUGIN_DIR.iterdir():
        if not item.is_dir():
            continue

        result = _load_template_from_dir(item)
        if result:
            name, data = result
            templates[name] = data

    return templates


def list_templates():
    """
    Return sorted list of all available template names.
    """
    templates = {}
    templates.update(load_builtin_templates())
    templates.update(load_plugins())

    return sorted(templates.keys())


def get_template(name: str):
    """
    Return template structure by name.
    Raises ValueError if not found.
    """
    templates = {}
    templates.update(load_builtin_templates())
    templates.update(load_plugins())

    if name not in templates:
        raise ValueError(f"Unknown template: {name}")

    return templates[name]
