import sys
import papis.cli
import papis.config

import papis_dmenu
import papis_dmenu.dmenu
import papis_dmenu.config

import click
import logging

logger = logging.getLogger('dmenu:main')


@click.group(
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
    logger.debug('Setting picktool to dmenu')
    papis.config.set('picktool', 'dmenu')
    logger.debug('Setting editor to dmenu-gui-editor')
    papis.config.set('editor', papis.config.get('editor', section='dmenu-gui'))
    logger.error('TODO: https://github.com/papis/papis-dmenu')
