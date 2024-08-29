# LLM Components

## Overview

`llm-components` is a Python library designed to feed large language models with data from different sources. The library formats content in a structured markdown format.

The first data source implemented is a code base (a folder containing a gitignore file).

## Features

- Traverse a directory tree while respecting `.gitignore` rules.
- Format the directory structure and file contents into a readable markdown format.
- Command-line interface for easy usage.
- Clone a git repository and format its contents.

## Installation
To install the `llm-components` library, you can use pip:
```sh
pip install llm-components
```

## Usage

### Command-Line Interface

You can use the command-line interface to map a code base to markdown. The CLI takes the root directory of the code base or a git repository URL as an argument.

```sh
format-codebase <root_dir_or_repo>
```

### Example

```sh
# For a local directory
format-codebase /path/to/your/code/base

# For a git repository
format-codebase https://github.com/your/repo.git
```

This will output the directory structure and file contents in a structured markdown format.

### Programmatic Usage

You can also use the library programmatically by importing the necessary functions.

```python
import tempfile
from pathlib import Path
from llm_components.loaders.code_base import map_codebase_to_text
from llm_components.loaders.git_utils import clone_repository

# For a local directory
root_dir = Path("/path/to/your/code/base")
result = map_codebase_to_text(root_dir)
print(result)

# For a git repository
repo_url = "https://github.com/your/repo.git"
with tempfile.TemporaryDirectory() as temp_dir:
    clone_dir = Path(temp_dir) / "repo"
    clone_repository(repo_url, clone_dir)
    result = map_codebase_to_text(clone_dir)
    print(result)
```

## License

This project is licensed under the MIT License.
