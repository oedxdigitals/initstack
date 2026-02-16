import argparse
import os
import sys
import shutil

from initstack.core.templates import get_template, list_templates
from initstack.core.filesystem import create_structure
from initstack.core.environment import detect_environment
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

    structure = get_template(project_type)
    create_structure(base_path, structure)

    success("Project initialized")


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
    git_status = "YES" if shutil.which("git") else "NO"
    print(f"Git available  : {git_status}")

    # Write permissions
    writable = os.access(os.getcwd(), os.W_OK)
    print(f"Write access   : {'YES' if writable else 'NO'}")

    # PATH sanity
    path_ok = any(
        os.access(os.path.join(p, "initstack"), os.X_OK)
        for p in os.environ.get("PATH", "").split(os.pathsep)
    )
    print(f"PATH OK       : {'YES' if path_ok else 'UNKNOWN'}")


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
