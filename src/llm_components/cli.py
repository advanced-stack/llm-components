import argparse
from llm_components.loaders.code_base import map_codebase_to_text
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Map codebase to text")
    parser.add_argument(
        "root_dir", type=Path, help="Root directory of the codebase"
    )
    args = parser.parse_args()

    result = map_codebase_to_text(args.root_dir)
    print(result)


if __name__ == "__main__":
    main()
