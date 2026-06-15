"""Test of rang functionality."""

import pytest

import streampu as spu


@pytest.mark.parametrize(
    ("func", "message", "expected"),
    [
        (spu.rang.error_tag, "This is an error.", "\033[1m\033[31m(EE) \033[0mThis is an error."),
        (
            spu.rang.info_tag,
            "This is an information message.",
            "\x1b[1m\x1b[34m(II) \x1b[0mThis is an information message.",
        ),
        (spu.rang.warning_tag, "This is a warning.", "\033[1m\033[33m(WW) \033[0mThis is a warning."),
        (
            spu.rang.positive_tag,
            "This is a positive message.",
            "\x1b[1m\x1b[32m(II) \x1b[0mThis is a positive message.",
        ),
    ],
)
def test_rang_tags_with_colors(func, message, expected):
    spu.rang.disable_colors()
    out = spu.rang.warning_tag("This is a warning.")
    assert out == "(WW) This is a warning."

    spu.rang.enable_colors()
    assert func(message) == expected


@pytest.mark.parametrize(
    ("prefix", "text", "expected"),
    [
        (spu.rang.style.italic, "This is an italic message.", "\033[3mThis is an italic message.\033[0m"),
        (spu.rang.style.bold, "This is a bold message.", "\033[1mThis is a bold message.\033[0m"),
        (
            spu.rang.style.italic + spu.rang.style.bold,
            "This is an italic and bold message.",
            "\033[3m\033[1mThis is an italic and bold message.\033[0m",
        ),
        (
            spu.rang.style.underline,
            "This is an underline message.",
            "\033[4mThis is an underline message.\033[0m",
        ),
        (
            spu.rang.style.underline + spu.rang.style.bold,
            "This is an underline and bold message.",
            "\033[4m\033[1mThis is an underline and bold message.\033[0m",
        ),
        (
            spu.rang.style.underline + spu.rang.style.bold + spu.rang.style.italic,
            "This is an underline, bold, and italic message.",
            "\033[4m\033[1m\033[3mThis is an underline, bold, and italic message.\033[0m",
        ),
        (
            spu.rang.bg.red,
            "This is a message with red background.",
            "\033[41mThis is a message with red background.\033[0m",
        ),
        (
            spu.rang.fg.blue,
            "This is a message with blue foreground.",
            "\033[34mThis is a message with blue foreground.\033[0m",
        ),
    ],
)
def test_rang_style_and_single_color(prefix, text, expected):
    assert prefix + text + spu.rang.style.reset == expected


def test_rang_combined_fg_bg():
    message = (
        spu.rang.fg.black
        + spu.rang.bgB.red
        + "This is a message with black foreground and red background."
        + spu.rang.style.reset
    )
    assert message == "\033[30m\033[101mThis is a message with black foreground and red background.\033[0m"
