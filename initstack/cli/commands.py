import argparse
import os
import sys
import shutil

from initstack.core.templates import get_template, list_templates
from initstack.core.filesystem import create_structure
from initstack.core.environment import detect_environment
from initstack.core.gitutils import init_git_repo, add_license
from initstack.utils.output import info, success, error


# -------------------------
# COMMAND: initstack new
# -------------------------
def cmd_new(args):
    project_type = args.type.lower()
    project_name = args.name

    base_path = os.path.join(os.getcwd(), project_name)

    if os.path.exists(base_path):
        error(f"Directory '{project_name}' already exists")
        sys.exit(1)

    info(f"Initializing {project_type} project: {project_name}")

    # Create project structure
    structure = get_template(project_type)
    create_structure(base_path, structure)

    # Optional git init
    if shutil.which("git"):
        use_git = input("Initialize git repository? (y/n): ").strip().lower() == "y"
        if use_git:
            init_git_repo(base_path)
            success("Git repository initialized")

            license_name = input("License (MIT / none): ").strip().upper()
            if license_name == "MIT":
                author = input("Author name: ").strip()
                add_license(base_path, "MIT", author)
                success("MIT license added")
    else:
        info("Git not available — skipping git initialization")

    success("Project initialized successfully")


# -------------------------
# COMMAND: initstack list
# -------------------------
def cmd_list(_):
    info("Available templates:")
    for name in list_templates():
        print(f"  - {name}")


# -------------------------
# COMMAND: initstack doctor
# -------------------------
def cmd_doctor(_):
    print("Initstack Doctor\n")

    # Python
    print(f"Python version : {sys.version.split()[0]}")

    # Environment
    env = detect_environment()
    print(f"Environment    : {env}")

    # Git
    print(f"Git available  : {'YES' if shutil.which('git') else 'NO'}")

    # Write permissions
    writable = os.access(os.getcwd(), os.W_OK)
    print(f"Write access   : {'YES' if writable else 'NO'}")

    # PATH sanity (best-effort)
    path_entries = os.environ.get("PATH", "").split(os.pathsep)
    path_ok = any(
        os.path.isfile(os.path.join(p, "initstack")) or
        os.path.isfile(os.path.join(p, "initstack.exe"))
        for p in path_entries
    )
    print(f"PATH OK        : {'YES' if path_ok else 'UNKNOWN'}")


# -------------------------
# ARGPARSE BUILDER
# -------------------------
def build_parser():
    parser = argparse.ArgumentParser(
        prog="initstack",
        description="Universal, environment-aware project initializer"
    )

    subparsers = parser.add_subparsers(dest="command")

    # new
    new_cmd = subparsers.add_parser(
        "new", help="Create a new project"
    )
    new_cmd.add_argument("type", help="Project type (python, web, cli, custom)")
    new_cmd.add_argument("name", help="Project name")
    new_cmd.set_defaults(func=cmd_new)

    # list
    list_cmd = subparsers.add_parser(
        "list", help="List available templates"
    )
    list_cmd.set_defaults(func=cmd_list)

    # doctor
    doctor_cmd = subparsers.add_parser(
        "doctor", help="Check environment health"
    )
    doctor_cmd.set_defaults(func=cmd_doctor)

    return parser
