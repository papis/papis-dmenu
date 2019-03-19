import dmenu
import papis.utils
import papis.pick
import functools
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


class Picker(papis.pick.Picker):

    def __init__(
            self, options, header_filter=None, match_filter=None, **kwargs
            ):

        self.fmt = papis.config.get('header-format', section='dmenu-gui')
        print('asdf')
        print(self.fmt)
        papis.pick.Picker.__init__(
            self,
            options
        )
        self.header_filter = lambda x: papis.utils.format_doc(self.fmt, x)

    def __call__(self):

        if len(self.options) == 1:
            index = 0
        else:
            print(self.header_filter(self.options[0]))
            headers = [self.header_filter(o) for o in self.options]
            print(headers)
            header = _dmenu_pick(headers)
            if not header:
                return None
            index = headers.index(header)
        return self.options[index]


def input(prompt=''):
    return _dmenu_pick([], prompt=prompt)
