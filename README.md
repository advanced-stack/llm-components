# LLM Components

## Overview

`llm-components` is a Python library designed to feed large language models with data from different sources.

The library formats content in a structured markdown format.

## Features

- Code base formatting:
    - Traverse a directory tree while respecting `.gitignore` rules.
    - Format the directory structure and file contents into a readable markdown format.
    - Clone a git repository and format its contents.

- Convert web pages to markdown format

## Installation
To install the `llm-components` library, you can use pip:
```sh
pip install llm-components
```

## Usage

### Command-Line Interface

You can use the command-line interface to map a code base to markdown. The CLI takes the root directory of the code base or a git repository URL as an argument.

```sh
llm-components format-codebase <root_dir_or_repo>
```

You can also convert a web page to markdown using the CLI:

```sh
llm-components web-to-markdown <url>
```

### Example

```sh
# For a local directory
llm-components format-codebase /path/to/your/code/base

# For a git repository
llm-components format-codebase https://github.com/your/repo.git

# For a web page
llm-components web-to-markdown https://advanced-stack.com
```

This will output the directory structure and file contents in a structured markdown format.

### Programmatic Usage

You can also use the library programmatically by importing the necessary functions.

```python
import tempfile
from pathlib import Path
from llm_components.loaders.code_base import map_codebase_to_text
from llm_components.loaders.git_utils import clone_repository
from llm_components.loaders.web_to_markdown import retrieve_and_convert

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

# For a web page
url = "https://example.com"
markdown_content = retrieve_and_convert(url)
print(markdown_content)
```


## License

This project is licensed under the MIT License.
