import argparse
from llm_components.loaders.code_base import map_codebase_to_text
from llm_components.loaders.git_utils import clone_repository
from pathlib import Path
import tempfile


def main():
    parser = argparse.ArgumentParser(description="Map codebase to text")
    parser.add_argument(
        "root_dir_or_repo",
        type=str,
        help="Root directory of the codebase or git repository URL",
    )
    args = parser.parse_args()

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


if __name__ == "__main__":
    main()
