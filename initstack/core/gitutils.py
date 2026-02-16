import subprocess
import os
import shutil
from datetime import datetime

def init_git_repo(path):
    subprocess.run(["git", "init"], cwd=path)

def add_license(path, license_name, author):
    src = os.path.join(
        os.path.dirname(__file__), "..", "licenses", f"{license_name}.txt"
    )
    dst = os.path.join(path, "LICENSE")

    with open(src, "r") as f:
        content = f.read()

    content = content.replace("{{year}}", str(datetime.now().year))
    content = content.replace("{{author}}", author)

    with open(dst, "w") as f:
        f.write(content)
