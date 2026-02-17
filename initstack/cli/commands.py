import sys
import os
import platform

from initstack.core.templates import list_templates, get_template
from initstack.core.project import create_project


# -------------------------
# Command handlers
# -------------------------

def cmd_list(args):
    print("ℹ Available templates:")
    for name in list_templates():
        print(f"  - {name}")


def cmd_new(args):
    template = get_template(args.template)
    create_project(template, args.name)


def cmd_doctor(args):
    print("\n🩺 Initstack Doctor Report\n")

    # Python
    print(f"✔ Python executable: {sys.executable}")
    print(f"✔ Python version: {platform.python_version()}")

    # OS
    print(f"✔ Platform: {platform.system().lower()}")

    # Home directory
    home = os.path.expanduser("~")
    print(f"✔ Home directory: {home}")

    # Plugin directory
    plugin_dir = os.path.expanduser("~/.initstack/plugins")
    print(f"\n🔌 Plugin directory: {plugin_dir}")

    if not os.path.isdir(plugin_dir):
        print("⚠ Plugin directory does not exist")
        return

    plugins = os.listdir(plugin_dir)
    if not plugins:
        print("⚠ No plugins installed")
    else:
        print("✔ Installed plugins:")
        for p in plugins:
            print(f"  - {p}")

    print("\n✅ Doctor check complete\n")


def cmd_self_update(args):
    print("ℹ Self-update is not yet implemented")
    print("ℹ Use: pip install --upgrade initstack")


# -------------------------
# Subcommand registration
# -------------------------

def build_parser(subparsers):
    # list
    p_list = subparsers.add_parser(
        "list",
        help="List available templates"
    )
    p_list.set_defaults(func=cmd_list)

    # new
    p_new = subparsers.add_parser(
        "new",
        help="Create a new project"
    )
    p_new.add_argument("template", help="Template name")
    p_new.add_argument("name", help="Project directory name")
    p_new.set_defaults(func=cmd_new)

    # doctor
    p_doctor = subparsers.add_parser(
        "doctor",
        help="Check environment health"
    )
    p_doctor.set_defaults(func=cmd_doctor)

    # self-update
    p_update = subparsers.add_parser(
        "self-update",
        help="Update initstack to the latest version"
    )
    p_update.set_defaults(func=cmd_self_update)
