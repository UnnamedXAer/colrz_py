type ColorNumber = int
type ColorEscape = str

fg_black: ColorEscape = "\033[30m"
fg_red: ColorEscape = "\033[31m"
fg_green: ColorEscape = "\033[32m"
fg_yellow: ColorEscape = "\033[33m"
fg_blue: ColorEscape = "\033[34m"
fg_magenta: ColorEscape = "\033[35m"
fg_cyan: ColorEscape = "\033[36m"
fg_white: ColorEscape = "\033[37m"

fg_reset: ColorEscape = "\033[39m"

bg_black: ColorEscape = "\033[40m"
bg_red: ColorEscape = "\033[41m"
bg_green: ColorEscape = "\033[42m"
bg_yellow: ColorEscape = "\033[43m"
bg_blue: ColorEscape = "\033[44m"
bg_magenta: ColorEscape = "\033[45m"
bg_cyan: ColorEscape = "\033[46m"
bg_white: ColorEscape = "\033[47m"

bg_reset: ColorEscape = "\033[49m"


# Foreground colors
_fg_black: ColorNumber = 30
_fg_red: ColorNumber = 31
_fg_green: ColorNumber = 32
_fg_yellow: ColorNumber = 33
_fg_blue: ColorNumber = 34
_fg_magenta: ColorNumber = 35
_fg_cyan: ColorNumber = 36
_fg_white: ColorNumber = 37

_fg_reset: ColorNumber = 39

# Background colors
_bg_black: ColorNumber = 40
_bg_red: ColorNumber = 41
_bg_green: ColorNumber = 42
_bg_yellow: ColorNumber = 43
_bg_blue: ColorNumber = 44
_bg_magenta: ColorNumber = 45
_bg_cyan: ColorNumber = 46
_bg_white: ColorNumber = 47

_bg_reset: ColorNumber = 49


def _set_color(c: ColorNumber, s: object) -> str:
    return f"\033[{c}m{s}\033[{_fg_reset}m"


def _set_color_bg(c: ColorNumber, s: object) -> str:
    return f"\033[{c}m{s}\033[{_bg_reset}m"


def black(s: object) -> str:
    return _set_color(_fg_black, s)


def red(s: object) -> str:
    return _set_color(_fg_red, s)


def green(s: object) -> str:
    return _set_color(_fg_green, s)


def yellow(s: object) -> str:
    return _set_color(_fg_yellow, s)


def blue(s: object) -> str:
    return _set_color(_fg_blue, s)


def magenta(s: object) -> str:
    return _set_color(_fg_magenta, s)


def cyan(s: object) -> str:
    return _set_color(_fg_cyan, s)


def white(s: object) -> str:
    return _set_color(_fg_white, s)


def black_bg(s: object) -> str:
    return _set_color_bg(_bg_black, s)


def red_bg(s: object) -> str:
    return _set_color_bg(_bg_red, s)


def green_bg(s: object) -> str:
    return _set_color_bg(_bg_green, s)


def yellow_bg(s: object) -> str:
    return _set_color_bg(_bg_yellow, s)


def blue_bg(s: object) -> str:
    return _set_color_bg(_bg_blue, s)


def magenta_bg(s: object) -> str:
    return _set_color_bg(_bg_magenta, s)


def cyan_bg(s: object) -> str:
    return _set_color_bg(_bg_cyan, s)


def white_bg(s: object) -> str:
    return _set_color_bg(_bg_white, s)
