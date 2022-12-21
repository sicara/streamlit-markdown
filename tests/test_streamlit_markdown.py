"""
Test the methods in stmd.streamlit_markdown
"""

import pytest

from stmd.streamlit_markdown import (
    _extract_image_path,
    _extract_part,
    _split_in_parts,
    markdown,
)


@pytest.mark.parametrize(
    "markdown_string, expected_parts",
    [
        (
            "This is a text with an image ![image](image.png)",
            ["This is a text with an image ", "![image](image.png)"],
        ),
        (
            "This is a text with an image ![image](image.png) "
            "and another one ![image](image.png)",
            [
                "This is a text with an image ",
                "![image](image.png)",
                " and another one ",
                "![image](image.png)",
            ],
        ),
        (
            "This is a text with an image ![image](image.png) "
            "and another one ![image](image.png) and a text",
            [
                "This is a text with an image ",
                "![image](image.png)",
                " and another one ",
                "![image](image.png)",
                " and a text",
            ],
        ),
    ],
)
def test_split_in_parts(markdown_string, expected_parts):
    assert _split_in_parts(markdown_string) == expected_parts


@pytest.mark.parametrize("source", ["examples/simple.md", "examples/images.md"])
def test_markdown_runs_without_error_for_all_examples(source):
    markdown(source)


@pytest.mark.parametrize(
    "input_part, expected_part_type, expected_part_content",
    [
        ("![image](image.png)", "image", "image.png"),
        ("![](image2.png 'title')", "image", "image2.png"),
        (
            "![](https://google.com/dummy?image.png)",
            "image",
            "https://google.com/dummy?image.png",
        ),
        ("This is a text", "text", "This is a text"),
        ("", "text", ""),
        ("My text ![", "text", "My text !["),
        ("My text ![]", "text", "My text ![]"),
        (
            "A simple link [link](https://www.google.com)",
            "text",
            "A simple link [link](https://www.google.com)",
        ),
    ],
)
def test_extract_part(input_part, expected_part_type, expected_part_content):
    assert _extract_part(input_part) == (expected_part_type, expected_part_content)


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("![](image.png)", "image.png"),
        ("![alt text](image.png)", "image.png"),
        ("![alt text](image.png 'title')", "image.png"),
        ('![alt text](image.png "title")', "image.png"),
        (
            "![alt text]("
            "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg "
            "'title')",
            "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg",
        ),
    ],
)
def test_extract_image_path(input_string, expected_output):
    assert _extract_image_path(input_string) == expected_output
