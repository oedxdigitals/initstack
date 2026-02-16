# initstack/core/filesystem.py
import os

def create_structure(base_path, structure):
    for path, content in structure.items():
        full = os.path.join(base_path, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(content)
