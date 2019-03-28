import functools
import dmenu

import papis.utils
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


def pick(options, header_filter=None, match_filter=None, **kwargs):

    fmt = papis.config.get('header-format', section='dmenu-gui')
    header_filter = (
        header_filter if header_filter is not None
        else lambda x: papis.utils.format_doc(fmt, x)
    )

    if len(options) == 1:
        index = 0
    elif len(options) == 0:
        return ''
    else:
        headers = [header_filter(o) for o in options]
        header = _dmenu_pick(headers)
        if not header:
            return None
        index = headers.index(header)

    return options[index]


def input(prompt=''):
    return _dmenu_pick([], prompt=prompt)
