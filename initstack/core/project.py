import os
from pathlib import Path


def create_project(template: dict, project_name: str):
    """
    Create a project directory structure from a template definition.
    """
    root = Path(project_name)

    if root.exists():
        raise FileExistsError(f"Directory '{project_name}' already exists")

    print(f"📁 Creating project: {project_name}")
    root.mkdir(parents=True)

    structure = template.get("structure", {})

    _create_structure(root, structure)

    print("✅ Project created successfully")


def _create_structure(base: Path, structure: dict):
    for name, content in structure.items():
        path = base / name

        if isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            _create_structure(path, content)

        elif isinstance(content, str):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        else:
            raise ValueError(f"Invalid structure item: {name}")
