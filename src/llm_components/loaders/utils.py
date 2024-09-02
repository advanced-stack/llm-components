import re


def clean_scraped_content(content):
    # Remove excessive blank lines
    content = re.sub(r"\n\n\s*\n", "\n", content)

    return content
