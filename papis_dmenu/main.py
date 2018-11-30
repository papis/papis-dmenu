import dmenu
import sys
import papis.cli
import papis.config
from papis.commands.default import run as papis_main

import papis_dmenu
import papis_dmenu.config

import logging
logger = logging.getLogger("dmenu")
import click


@click.group(
    cls=papis.cli.MultiCommand,
    invoke_without_command=True
)
@click.help_option('--help', '-h')
@click.version_option(version=papis_dmenu.__version__)
@click.option('-q', '--query', help='Input query')
@click.option('-i', default=False, is_flag=True, help='Interactive mode')
@click.option('-p', '--prompt', default='', help='Interactive prompt')
def main(query, i, prompt):
    """A dmenu based GUI for papis"""
    papis_dmenu.config.register_default_settings()
    papis.config.set_external_picker(papis_dmenu.pick)
    papis.config.set('editor', papis.config.get('editor', section='dmenu-gui'))
    if i:
        query = papis_dmenu.input(prompt=prompt)
    if query is not None:
        sys.argv.append(query)
    indices_to_erase = []
    for i, argv in enumerate(sys.argv):
        if i in indices_to_erase:
            continue
        # Put here the prompt options with argument
        if argv in ['-q', '--query', '-p', '--prompt']:
            indices_to_erase += [i, i+1]
        # Put here the prompt options without argument
        elif argv in ['-i', 'dmenu']:
            indices_to_erase += [i]
    last_sum = 0
    for i in sorted(indices_to_erase):
        sys.argv.pop(i - last_sum)
        last_sum = i
    papis_main()
