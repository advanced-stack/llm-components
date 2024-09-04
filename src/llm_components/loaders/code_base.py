import pathspec
from pathlib import Path


def traverse_directory(root_dir, gitignore_file):
    """
    Traverses a directory tree and generates a list of tuples compatible with format_output.

    Args:
        root_dir (Path): The root directory to start the traversal.
        gitignore_file (Path): The path to the .gitignore file.

    Returns:
        list of tuples: A list of tuples where each tuple contains a Path object and an integer representing the depth of the item in the directory tree.
    """
    with gitignore_file.open() as f:
        spec = pathspec.GitIgnoreSpec.from_lines(f)

    def traverse(path, depth):
        relative_path = path.relative_to(root_dir)
        if spec.match_file(str(relative_path)) or path.name == ".git":
            return []
        if path.is_dir():
            children = [traverse(child, depth + 1) for child in path.iterdir()]
            children = [
                item for sublist in children for item in sublist
            ]  # Flatten the list
            if (
                not children
            ):  # If directory is empty or only contains ignored files
                return []
            return [(path, depth)] + children
        else:
            return [(path, depth)]

    return traverse(root_dir, 0)


def format_dir_name(item):
    """
    Add a trailing slash if the item is a directory.

    Args:
        item (Path): The Path object to format.

    Returns:
        str: The formatted directory name with a trailing slash if it is a directory.
    """
    return f"{item.name}/" if item.is_dir() else item.name


def format_output(traversed_data, root_dir, gitignore_file):
    """
    Formats the output of a directory traversal into a structured text format.

    Args:
        traversed_data (list of tuples): A list of tuples where each tuple contains a Path object and an integer representing the depth of the item in the directory tree.
        root_dir (Path): The root directory from which the relative paths will be calculated.
        gitignore_file (Path): The path to the .gitignore file.

    Returns:
        str: A formatted string representing the directory structure and file contents.

    The function processes each item in the traversed_data. If the item is a directory, it appends the directory name and its contents to the result. If the item is a file, it appends the file name, its size, and its contents to the result.
    """
    with gitignore_file.open() as f:
        spec = pathspec.GitIgnoreSpec.from_lines(f)

    def get_file_size(file_path):
        return file_path.stat().st_size

    def read_file(file_path):
        try:
            return file_path.read_text()
        except Exception:
            return "[Non-text file content not displayed]"

    result = []
    for item, depth in traversed_data:
        relative_path = item.relative_to(root_dir)
        if item.is_dir():
            result.append(f"{'#' * depth} {item.name}\n")
            result.append(f"./{relative_path}:\n```\n")

            dir_contents = [
                child.name
                for child in item.iterdir()
                if not spec.match_file(
                    format_dir_name(child.relative_to(root_dir))
                )
            ]

            result.append("\n".join(dir_contents))
            result.append("\n```\n\n")
        else:
            file_size = get_file_size(item)
            result.append(f"{'#' * depth} {item.name} ({file_size})\n")
            result.append(f"./{relative_path}:\n```\n")
            result.append(read_file(item))
            result.append("\n```\n\n")
    return "".join(result)


def map_codebase_to_text(root_dir):
    gitignore_file = root_dir / ".gitignore"
    traversed_data = traverse_directory(root_dir, gitignore_file)
    return format_output(traversed_data, root_dir, gitignore_file)
