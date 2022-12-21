"""
Contains the package's core method to render markdown files
i.e. `markdown()`, along with its helper methods.
"""

import re
from pathlib import Path
from typing import List, Tuple, Union

import streamlit as st

IMAGE_PATH_REGEX = r"""\(([^()]*?)\s*(?:'[^']*'|\"[^\"]*\")*\)"""
MARKDOWN_IMAGE_REGEX = r"""(!\[[^\]]*\]\([^\]]*\))"""


def markdown(filepath: Union[Path, str]):
    """
    Renders a markdown file in Streamlit.
    Args:
        filepath: path to a markdown file
    """

    with open(filepath, "r", encoding="UTF-8") as file:
        markdown_string = file.read()

    for part in split_in_parts(markdown_string):
        part_type, part_content = extract_part(part)
        display_part(part_type, part_content)


def split_in_parts(markdown_string: str) -> List[str]:
    """
    Splits a markdown string into parts, where each part
    is either simple text or the markdown for an image.
    Args:
        markdown_string: string containing markdown

    Returns:
        list of parts
    """
    return list(filter(None, re.split(MARKDOWN_IMAGE_REGEX, markdown_string)))


def extract_part(part: str) -> Tuple[str, str]:
    """
    Extracts the type and content of a part.
    Args:
        part: part of a markdown string

    Returns:
        tuple of part type ("text" or "image")
        and part content (whole string for text, image path for image)
    """
    if re.match(MARKDOWN_IMAGE_REGEX, part):
        return "image", extract_image_path(part)
    return "text", part


def extract_image_path(markdown_image_string: str):
    """
    Extracts the path of an image from a markdown image string.
    Args:
        markdown_image_string: must be a string of the form `![alt text](image.png "title")`

    Returns:
        path of the image
    """
    match = re.search(IMAGE_PATH_REGEX, markdown_image_string)

    if match:
        return match.groups()[0]

    raise ValueError(f"Could not extract image path from {markdown_image_string}")


def display_part(part_type: str, part_content: str):
    """
    Displays a part in Streamlit.
    Args:
        part_type: either "text" or "image"
        part_content: markdown string for text, path to an image for image

    """
    if part_type == "image":
        st.image(part_content)
    elif part_type == "text":
        st.markdown(part_content)
    else:
        raise ValueError(f"Unknown part type: {part_type}")
