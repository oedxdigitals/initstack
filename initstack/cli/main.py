# initstack/cli/main.py
from initstack.cli.commands import build_parser
from initstack.core.environment import detect_environment
from initstack.utils.output import info

def main():
    env = detect_environment()
    info(f"Initstack running on: {env}")

    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
