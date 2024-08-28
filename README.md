# LLM Components

## Overview

`llm-components` is a Python library designed to feed large language models with data from different sources. The library formats content in a structured markdown format.

The first data source implemented is a code base (a folder containing a gitignore file).

## Features

- Traverse a directory tree while respecting `.gitignore` rules.
- Format the directory structure and file contents into a readable markdown format.
- Command-line interface for easy usage.

## Installation
To install the `llm-components` library, you can use pip:
```sh
pip install llm-components
```

## Usage

### Command-Line Interface
You can use the command-line interface to map a code base to markdown. The CLI takes the root directory of the code base as an argument.

```sh
format-codebase <root_dir>
```

### Example
```sh
format-codebase /path/to/your/code/base
```

This will output the directory structure and file contents in a structured markdown format.

### Programmatic Usage
You can also use the library programmatically by importing the necessary functions.

```python
from pathlib import Path
from llm_components.loaders import map_codebase_to_text

root_dir = Path("/path/to/your/code/base")
result = map_codebase_to_text(root_dir)
print(result)
```

## License
This project is licensed under the MIT License.
