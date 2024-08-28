import subprocess


def clone_repository(repo_url, clone_dir):
    """
    Clones a git repository to a specified directory.

    Args:
     repo_url (str): The URL of the git repository.
     clone_dir (Path): The directory where the repository will be cloned.

    Returns:
     Path: The path to the cloned repository.
    """
    subprocess.run(
        ["git", "clone", repo_url, str(clone_dir)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return clone_dir
