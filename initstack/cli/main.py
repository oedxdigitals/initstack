import argparse
import platform

from initstack.cli.commands import build_parser


def main():
    print(f"ℹ Initstack running on: {platform.system().lower()}")

    parser = argparse.ArgumentParser(
        prog="initstack",
        description="Universal, environment-aware project initializer"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)
    build_parser(subparsers)

    args = parser.parse_args()
    args.func(args)
