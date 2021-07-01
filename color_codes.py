class ColorCode:
    """
    Certain sequences of bytes, most starting with an ASCII escape character and a bracket character,
    are embedded into text.
    The terminal interprets these sequences as commands, rather than text to display verbatim.

    Escape Character: print() accepts octal: \033 or hex: \x1B
    https://en.wikipedia.org/wiki/Escape_character

    ESC [ -> Control Sequence Introducer
    https://en.wikipedia.org/wiki/ANSI_escape_code#CSIsection
    For Control Sequence Introducer, or CSI, commands, the ESC [ is followed by any number (including none)
    of "parameter bytes" in the range 0x30–0x3F (ASCII 0–9:;<=>?), then by any number of "intermediate bytes"
    in the range 0x20–0x2F (ASCII space and !"#$%&'()*+,-./),
    then finally by a single "final byte" in the range 0x40–0x7E (ASCII @A–Z[\]^_`a–z{|}~).

    ANSI Color Codes
    https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit

    CSI n m -> Select Graphic Rendition
    https://en.wikipedia.org/wiki/ANSI_escape_code#SGR
    The final m sets the appearance of the following characters.

    :cvar
    """

    # Foreground colors - Dark
    FG_BLACK = '\x1B[30m'
    FG_RED = '\x1B[31m'
    FG_GREEN = '\x1B[32m'
    FG_YELLOW = '\x1B[33m'
    FG_BLUE = '\x1B[34m'
    FG_MAGENTA = '\x1B[35m'
    FG_CYAN = '\x1B[36m'
    FG_WHITE = '\x1B[37m'
    # Foreground colors - Light
    FG_BRIGHT_BLACK = '\x1B[90m'
    FG_BRIGHT_RED = '\x1B[91m'
    FG_BRIGHT_GREEN = '\x1B[92m'
    FG_BRIGHT_YELLOW = '\x1B[93m'
    FG_BRIGHT_BLUE = '\x1B[94m'
    FG_BRIGHT_MAGENTA = '\x1B[95m'
    FG_BRIGHT_CYAN = '\x1B[96m'
    FG_BRIGHT_WHITE = '\x1B[97m'

    # Background colors - Dark
    BG_BLACK = '\x1B[40m'
    BG_RED = '\x1B[41m'
    BG_GREEN = '\x1B[42m'
    BG_YELLOW = '\x1B[43m'
    BG_BLUE = '\x1B[44m'
    BG_MAGENTA = '\x1B[45m'
    BG_CYAN = '\x1B[46m'
    BG_WHITE = '\x1B[47m'
    # Background colors - Light
    BG_BRIGHT_BLACK = '\x1B[100m'
    BG_BRIGHT_RED = '\x1B[101m'
    BG_BRIGHT_GREEN = '\x1B[102m'
    BG_BRIGHT_YELLOW = '\x1B[103m'
    BG_BRIGHT_BLUE = '\x1B[104m'
    BG_BRIGHT_MAGENTA = '\x1B[105m'
    BG_BRIGHT_CYAN = '\x1B[106m'
    BG_BRIGHT_WHITE = '\x1B[107m'

    # Select Graphic Rendition
    RESET = '\x1B[0m'  # or '\033[m' (missing numbers are treated as a zero)
    BOLD = '\033[1m'
    FAINT = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK_SLOW = '\033[5m'
    BLINK_FAST = '\033[6m'
    REVERSE = '\033[7m'  # Swap foreground and background colors
    HIDE = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    NORMAL = '\033[22m'
    NOT_ITALIC = '\033[23m'
    NOT_UNDERLINE = '\033[24m'
    NOT_BLINKING = '\033[25m'
    NOT_REVERSE = '\033[27m'
    REVEAL = '\033[28m'
    NOT_STRIKETHROUGH = '\033[29m'
