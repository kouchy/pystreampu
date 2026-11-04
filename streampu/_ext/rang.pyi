from __future__ import annotations

import typing

__all__: list[str] = [
    "bg",
    "bgB",
    "control",
    "disable_colors",
    "enable_colors",
    "fg",
    "fgB",
    "setControlMode",
    "setWinTermMode",
    "style",
    "winTerm",
]

class bg:
    """
    Members:

    black

    red

    green

    yellow

    blue

    magenta

    cyan

    gray

    reset
    """

    __members__: typing.ClassVar[
        dict[str, bg]
    ]  # value = {'black': <bg.black: 40>, 'red': <bg.red: 41>, 'green': <bg.green: 42>, 'yellow': <bg.yellow: 43>, 'blue': <bg.blue: 44>, 'magenta': <bg.magenta: 45>, 'cyan': <bg.cyan: 46>, 'gray': <bg.gray: 47>, 'reset': <bg.reset: 49>}
    black: typing.ClassVar[bg]  # value = <bg.black: 40>
    blue: typing.ClassVar[bg]  # value = <bg.blue: 44>
    cyan: typing.ClassVar[bg]  # value = <bg.cyan: 46>
    gray: typing.ClassVar[bg]  # value = <bg.gray: 47>
    green: typing.ClassVar[bg]  # value = <bg.green: 42>
    magenta: typing.ClassVar[bg]  # value = <bg.magenta: 45>
    red: typing.ClassVar[bg]  # value = <bg.red: 41>
    reset: typing.ClassVar[bg]  # value = <bg.reset: 49>
    yellow: typing.ClassVar[bg]  # value = <bg.yellow: 43>
    @staticmethod
    def __add__(slf, message): ...
    @staticmethod
    def __radd__(slf, message): ...
    def __eq__(self, other: typing.Any) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: typing.Any) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    @typing.overload
    def __str__(self) -> str: ...
    @typing.overload
    def __str__(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class bgB:
    """
    Members:

    black

    red

    green

    yellow

    blue

    magenta

    cyan

    gray
    """

    __members__: typing.ClassVar[
        dict[str, bgB]
    ]  # value = {'black': <bgB.black: 100>, 'red': <bgB.red: 101>, 'green': <bgB.green: 102>, 'yellow': <bgB.yellow: 103>, 'blue': <bgB.blue: 104>, 'magenta': <bgB.magenta: 105>, 'cyan': <bgB.cyan: 106>, 'gray': <bgB.gray: 107>}
    black: typing.ClassVar[bgB]  # value = <bgB.black: 100>
    blue: typing.ClassVar[bgB]  # value = <bgB.blue: 104>
    cyan: typing.ClassVar[bgB]  # value = <bgB.cyan: 106>
    gray: typing.ClassVar[bgB]  # value = <bgB.gray: 107>
    green: typing.ClassVar[bgB]  # value = <bgB.green: 102>
    magenta: typing.ClassVar[bgB]  # value = <bgB.magenta: 105>
    red: typing.ClassVar[bgB]  # value = <bgB.red: 101>
    yellow: typing.ClassVar[bgB]  # value = <bgB.yellow: 103>
    @staticmethod
    def __add__(slf, message): ...
    @staticmethod
    def __radd__(slf, message): ...
    def __eq__(self, other: typing.Any) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: typing.Any) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    @typing.overload
    def __str__(self) -> str: ...
    @typing.overload
    def __str__(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class control:
    """
    Members:

    Off

    Auto

    Force
    """

    Auto: typing.ClassVar[control]  # value = <control.Auto: 1>
    Force: typing.ClassVar[control]  # value = <control.Force: 2>
    Off: typing.ClassVar[control]  # value = <control.Off: 0>
    __members__: typing.ClassVar[
        dict[str, control]
    ]  # value = {'Off': <control.Off: 0>, 'Auto': <control.Auto: 1>, 'Force': <control.Force: 2>}
    def __eq__(self, other: typing.Any) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: typing.Any) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    def __str__(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class fg:
    """
    Members:

    black

    red

    green

    yellow

    blue

    magenta

    cyan

    gray

    reset
    """

    __members__: typing.ClassVar[
        dict[str, fg]
    ]  # value = {'black': <fg.black: 30>, 'red': <fg.red: 31>, 'green': <fg.green: 32>, 'yellow': <fg.yellow: 33>, 'blue': <fg.blue: 34>, 'magenta': <fg.magenta: 35>, 'cyan': <fg.cyan: 36>, 'gray': <fg.gray: 37>, 'reset': <fg.reset: 39>}
    black: typing.ClassVar[fg]  # value = <fg.black: 30>
    blue: typing.ClassVar[fg]  # value = <fg.blue: 34>
    cyan: typing.ClassVar[fg]  # value = <fg.cyan: 36>
    gray: typing.ClassVar[fg]  # value = <fg.gray: 37>
    green: typing.ClassVar[fg]  # value = <fg.green: 32>
    magenta: typing.ClassVar[fg]  # value = <fg.magenta: 35>
    red: typing.ClassVar[fg]  # value = <fg.red: 31>
    reset: typing.ClassVar[fg]  # value = <fg.reset: 39>
    yellow: typing.ClassVar[fg]  # value = <fg.yellow: 33>
    @staticmethod
    def __add__(slf, message): ...
    @staticmethod
    def __radd__(slf, message): ...
    def __eq__(self, other: typing.Any) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: typing.Any) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    @typing.overload
    def __str__(self) -> str: ...
    @typing.overload
    def __str__(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class fgB:
    """
    Members:

    black

    red

    green

    yellow

    blue

    magenta

    cyan

    gray
    """

    __members__: typing.ClassVar[
        dict[str, fgB]
    ]  # value = {'black': <fgB.black: 90>, 'red': <fgB.red: 91>, 'green': <fgB.green: 92>, 'yellow': <fgB.yellow: 93>, 'blue': <fgB.blue: 94>, 'magenta': <fgB.magenta: 95>, 'cyan': <fgB.cyan: 96>, 'gray': <fgB.gray: 97>}
    black: typing.ClassVar[fgB]  # value = <fgB.black: 90>
    blue: typing.ClassVar[fgB]  # value = <fgB.blue: 94>
    cyan: typing.ClassVar[fgB]  # value = <fgB.cyan: 96>
    gray: typing.ClassVar[fgB]  # value = <fgB.gray: 97>
    green: typing.ClassVar[fgB]  # value = <fgB.green: 92>
    magenta: typing.ClassVar[fgB]  # value = <fgB.magenta: 95>
    red: typing.ClassVar[fgB]  # value = <fgB.red: 91>
    yellow: typing.ClassVar[fgB]  # value = <fgB.yellow: 93>
    @staticmethod
    def __add__(slf, message): ...
    @staticmethod
    def __radd__(slf, message): ...
    def __eq__(self, other: typing.Any) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: typing.Any) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    @typing.overload
    def __str__(self) -> str: ...
    @typing.overload
    def __str__(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class style:
    """
    Members:

    reset

    bold

    dim

    italic

    underline

    blink

    rblink

    reversed

    conceal

    crossed
    """

    __members__: typing.ClassVar[
        dict[str, style]
    ]  # value = {'reset': <style.reset: 0>, 'bold': <style.bold: 1>, 'dim': <style.dim: 2>, 'italic': <style.italic: 3>, 'underline': <style.underline: 4>, 'blink': <style.blink: 5>, 'rblink': <style.rblink: 6>, 'reversed': <style.reversed: 7>, 'conceal': <style.conceal: 8>, 'crossed': <style.crossed: 9>}
    blink: typing.ClassVar[style]  # value = <style.blink: 5>
    bold: typing.ClassVar[style]  # value = <style.bold: 1>
    conceal: typing.ClassVar[style]  # value = <style.conceal: 8>
    crossed: typing.ClassVar[style]  # value = <style.crossed: 9>
    dim: typing.ClassVar[style]  # value = <style.dim: 2>
    italic: typing.ClassVar[style]  # value = <style.italic: 3>
    rblink: typing.ClassVar[style]  # value = <style.rblink: 6>
    reset: typing.ClassVar[style]  # value = <style.reset: 0>
    reversed: typing.ClassVar[style]  # value = <style.reversed: 7>
    underline: typing.ClassVar[style]  # value = <style.underline: 4>
    @staticmethod
    def __add__(slf, message): ...
    @staticmethod
    def __radd__(slf, message): ...
    def __eq__(self, other: typing.Any) -> bool: ...
    def __ge__(self, other: typing.Any) -> bool: ...
    def __getstate__(self) -> int: ...
    def __gt__(self, other: typing.Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    def __int__(self) -> int: ...
    def __le__(self, other: typing.Any) -> bool: ...
    def __lt__(self, other: typing.Any) -> bool: ...
    def __ne__(self, other: typing.Any) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    @typing.overload
    def __str__(self) -> str: ...
    @typing.overload
    def __str__(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class winTerm:
    """
    Members:

    Auto

    Ansi

    Native
    """

    Ansi: typing.ClassVar[winTerm]  # value = <winTerm.Ansi: 1>
    Auto: typing.ClassVar[winTerm]  # value = <winTerm.Auto: 0>
    Native: typing.ClassVar[winTerm]  # value = <winTerm.Native: 2>
    __members__: typing.ClassVar[
        dict[str, winTerm]
    ]  # value = {'Auto': <winTerm.Auto: 0>, 'Ansi': <winTerm.Ansi: 1>, 'Native': <winTerm.Native: 2>}
    def __eq__(self, other: typing.Any) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: typing.Any) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None: ...
    def __str__(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def disable_colors() -> None: ...
def enable_colors() -> None: ...
def setControlMode(arg0: control) -> None: ...
def setWinTermMode(arg0: winTerm) -> None: ...
