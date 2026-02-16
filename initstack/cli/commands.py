# initstack/cli/commands.py
import argparse
import os
from initstack.core.templates import get_template, list_templates
from initstack.core.filesystem import create_structure
from initstack.utils.output import info, success, error
from initstack.utils.config import load_config

def cmd_new(args):
    config = load_config()
    project_type = args.type or config.get("default_type", "custom")

    base_path = os.path.join(os.getcwd(), args.name)

    if os.path.exists(base_path):
        error("Directory already exists")
        return

    info(f"Creating {project_type} project: {args.name}")
    structure = get_template(project_type)
    create_structure(base_path, structure)
    success("Project initialized")

def cmd_list(_):
    for t in list_templates():
        print(f"- {t}")

def build_parser():
    parser = argparse.ArgumentParser(
        prog="initstack",
        description="Universal project initializer"
    )

    sub = parser.add_subparsers()

    new = sub.add_parser("new", help="Create a new project")
    new.add_argument("type", help="Project type")
    new.add_argument("name", help="Project name")
    new.set_defaults(func=cmd_new)

    lst = sub.add_parser("list", help="List available templates")
    lst.set_defaults(func=cmd_list)

    return parser
