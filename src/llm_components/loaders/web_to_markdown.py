import requests
from bs4 import BeautifulSoup, Comment
import markdownify
from .utils import clean_scraped_content  # Import the cleaning function


def handle_nested_tags(soup, parent_tag, child_tag):
    """
    Handle nested tags by moving the child tag outside the parent tag.

    Args:
        soup (BeautifulSoup): The parsed HTML content.
        parent_tag (str): The parent tag to search for.
        child_tag (str): The child tag to move outside the parent tag.
    """
    for parent in soup.find_all(parent_tag):
        if parent.find(child_tag):
            child = parent.find(child_tag)
            # Move the child tag outside the parent tag
            parent.insert_before(child)
            # Optionally, you can keep the parent tag content or remove it
            parent.unwrap()


def get_html_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.content


def get_html_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def convert_html_to_markdown(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove CSS and JS
    for element in soup(["style", "script"]):
        element.decompose()

    # Remove HTML comments
    for comment in soup.find_all(
        string=lambda text: isinstance(text, Comment)
    ):
        comment.extract()

    # Handle nested tags
    handle_nested_tags(soup, "a", "h1")
    handle_nested_tags(soup, "a", "h2")
    handle_nested_tags(soup, "a", "h3")
    handle_nested_tags(soup, "a", "h4")
    handle_nested_tags(soup, "a", "h5")

    # Convert to markdown
    markdown_text = markdownify.markdownify(str(soup), heading_style="ATX")

    # Clean the markdown text
    cleaned_markdown_text = clean_scraped_content(markdown_text)

    return cleaned_markdown_text


def retrieve_and_convert(url):
    html_content = get_html_from_url(url)
    return convert_html_to_markdown(html_content)


def convert_file_to_markdown(file_path):
    html_content = get_html_from_file(file_path)
    return convert_html_to_markdown(html_content)
