import argparse
from llm_components.loaders.code_base import map_codebase_to_text
from llm_components.loaders.git_utils import clone_repository
from llm_components.loaders.web_to_markdown import retrieve_and_convert
from llm_components.version import __version__
from pathlib import Path
import tempfile


def format_codebase(args):
    if not args.root_dir_or_repo:
        print(
            "Root directory of the codebase or git repository URL is required"
        )
        return

    if args.root_dir_or_repo.startswith(
        "http://"
    ) or args.root_dir_or_repo.startswith("https://"):
        with tempfile.TemporaryDirectory() as temp_dir:
            clone_dir = Path(temp_dir) / "repo"
            clone_repository(args.root_dir_or_repo, clone_dir)
            result = map_codebase_to_text(clone_dir)
    else:
        root_dir = Path(args.root_dir_or_repo)
        result = map_codebase_to_text(root_dir)

    print(result)


def web_to_markdown(args):
    if not args.url:
        print("URL of the web page to convert is required")
        return

    result = retrieve_and_convert(args.url)
    print(result)


def main():
    parser = argparse.ArgumentParser(
        description="Map codebase to text or convert web page to markdown"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for the codebase command
    codebase_parser = subparsers.add_parser(
        "format-codebase", help="Map codebase to text"
    )
    codebase_parser.add_argument(
        "root_dir_or_repo",
        type=str,
        nargs="?",
        help="Root directory of the codebase or git repository URL",
    )
    codebase_parser.set_defaults(func=format_codebase)

    # Subparser for the web-to-markdown command
    web_parser = subparsers.add_parser(
        "web-to-markdown", help="Convert web page to markdown"
    )
    web_parser.add_argument(
        "url", type=str, help="URL of the web page to convert"
    )
    web_parser.set_defaults(func=web_to_markdown)

    parser.add_argument(
        "--version",
        action="store_true",
        help="Display the current version of the package",
    )

    args = parser.parse_args()

    if args.version:
        print(f"llm-components version {__version__}")
        return

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
