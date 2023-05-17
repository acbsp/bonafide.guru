import argparse
import json
import re

from .exceptions import NoTracebackException
from .logs import clr, logs

__all__ = [
    'Cli',
    'Type',
]


class NoAction(argparse.Action):
    def __init__(self, **kwargs):
        kwargs.setdefault('default', argparse.SUPPRESS)
        kwargs.setdefault('nargs', 0)
        super().__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        pass


class ChoicesAction(argparse._StoreAction):  # pylint: disable=protected-access
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = ['default']

    def add_choice(self, choice, help=''):  # pylint: disable=redefined-builtin
        self.choices.append(choice)
        self.container.add_argument(choice, help=help, action='none')  # pylint: disable=no-member


class Cli(argparse.ArgumentParser):
    def __init__(self, **kwargs):
        self._args = None
        self._commands_argument = None
        self._commands_functions = {}

        # If use super().__init help (-h) is not displayed
        argparse.ArgumentParser.__init__(self, **kwargs)
        self.register('action', 'none', NoAction)
        self.register('action', 'store_choice', ChoicesAction)

    def add_command(self, cmd=None, func=None, help=''):  # pylint: disable=redefined-builtin
        if not func:
            raise TypeError('missing required argument \'func\'')

        if not cmd:
            if func.__name__.startswith('do_'):
                cmd = func.__name__.replace('do_', '')
            else:
                raise ValueError('function should be started with \'do_\'')

        if self._commands_argument is None:
            group = self.add_argument_group(title='commands')
            self._commands_argument = group.add_argument(dest='commands', metavar='COMMANDS', nargs='*',
                                                         action='store_choice', default='default')

        self._commands_functions[cmd] = func
        self._commands_argument.add_choice(cmd, help)

    def parse_args(self, args=None, namespace=None):
        try:
            import argcomplete  # pylint: disable=import-outside-toplevel
            argcomplete.autocomplete(self, default_completer=None)
        except ModuleNotFoundError:
            pass

        self._args = super().parse_args(args, namespace)
        return self._args

    def handle_commands(self, default_cmds=('config', 'build', 'install')):
        if self._args.commands == 'default':
            self._args.commands = default_cmds

        try:
            for cmd in self._args.commands:
                print_cmd = f'{clr.CYN}{cmd}{clr.RST}'

                logs.log(f'Executing command \'{print_cmd}\'')
                self._commands_functions[cmd](self._args)
                logs.log(f'Command \'{print_cmd}\' finished OK')

        except (KeyboardInterrupt, SystemExit):
            logs.error(f'Interrupted command \'{print_cmd}\'')
            raise NoTracebackException
        except NoTracebackException:
            logs.error(f'Command \'{print_cmd}\' failed')
            raise
        except Exception as error:
            logs.error(error)
            logs.error(f'Command \'{print_cmd}\' failed')
            raise


class Type:
    @staticmethod
    def str(s):
        '''Return string'''
        if not s:
            return None
        return s

    @staticmethod
    def int(s):
        '''Return string with int value'''
        if not s:
            return None
        return str(int(s.strip()))

    @staticmethod
    def list_int(s):
        '''Return list of ints values(str)'''
        if not s:
            return None
        return re.findall(r'\d+', s)

    @staticmethod
    def json(s):
        '''Parse JSON'''
        if not s:
            return None
        return json.loads(s)

    @staticmethod
    def url(s):
        '''Validate URL'''
        url_pattern = '^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b' \
                      '(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$'
        if not s:
            return None
        if not re.match(url_pattern, s):
            raise ValueError
        return s
