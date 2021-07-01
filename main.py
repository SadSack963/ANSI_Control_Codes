from color_codes import ColorCode as cc

print(f'{cc.BOLD}Bold{cc.NORMAL} - not bold')
print(f'{cc.FAINT}Faint{cc.NORMAL} - not faint')  # not implemented in Pycharm
print(f'{cc.ITALIC}Italic{cc.NOT_ITALIC} - not italic')  # uses script font in Windows Terminal
print(f'{cc.UNDERLINE}Underlined{cc.NOT_UNDERLINE} - not underlined')
print(f'{cc.BLINK_SLOW}Slow Blink{cc.NOT_BLINKING} - not blinking')  # not implemented in Pycharm
print(f'{cc.BLINK_FAST}Fast Blink{cc.NOT_BLINKING} - not blinking')  # not implemented in Pycharm, same as slow blink in Windows Terminal
print(f'{cc.REVERSE}Reversed video{cc.NOT_REVERSE} - not reversed video')
print(f'{cc.HIDE}Hidden{cc.REVEAL} - not hidden')  # not implemented in Pycharm
print(f'{cc.STRIKETHROUGH}Strikethrough{cc.NOT_STRIKETHROUGH} - not strikethrough')
print(f'{cc.DOUBLE_UNDERLINE}Double Underline{cc.NOT_UNDERLINE} - not underlined')
