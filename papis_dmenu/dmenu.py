import functools
import dmenu

import papis.pick
import papis.format
import papis.config
import papis_dmenu.config


papis_dmenu.config.register_default_settings()


_dmenu_pick = functools.partial(
    dmenu.show,
    prompt='',
    case_insensitive=papis.config.getboolean(
        'case_insensitive', section="dmenu-gui"
    ),
    lines=papis.config.getint('lines', section='dmenu-gui'),
    bottom=papis.config.getboolean('bottom', section='dmenu-gui'),
    font=papis.config.get('font', section='dmenu-gui'),
    background=papis.config.get('background', section='dmenu-gui'),
    foreground=papis.config.get('foreground', section='dmenu-gui'),
    background_selected=papis.config.get(
        'background_selected', section='dmenu-gui'
    ),
    foreground_selected=papis.config.get(
        'foreground_selected', section='dmenu-gui'
    )
)


def pick(options):

    papis_dmenu.config.register_default_settings()
    fmt = papis.config.get('header-format', section='dmenu-gui')

    if len(options) == 1:
        index = 0
    elif len(options) == 0:
        return ''
    else:

        def header_filter(x):
            return papis.format.format(fmt, x)

        headers = [header_filter(o) for o in options]
        header = _dmenu_pick(headers)
        if not header:
            return None
        index = headers.index(header)

    return options[index]


class Picker(papis.pick.Picker):

    def __call__(self,
                 items,
                 header_filter,
                 match_filter,
                 default_index: int = 0):
        return [pick(items)]


def input(prompt=''):
    return _dmenu_pick([], prompt=prompt)
