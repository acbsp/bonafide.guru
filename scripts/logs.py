import os
import sys
from pathlib import Path

__all__ = [
    'clr',
    'logs'
]


class Colors:
    def __init__(self):
        def color_code(num: int) -> str:
            return f'\033[{str(num)}m'

        def no_color(num: int) -> str:
            return ''

        color = no_color if 'NO_COLOR' in os.environ else color_code

        # pylint: disable=invalid-name
        self.BLD = color(1)
        self.UDL = color(4)
        self.RST = color(0)

        self.BLK = color(30)
        self.RED = color(31)
        self.GRN = color(32)
        self.YEL = color(33)
        self.BLU = color(34)
        self.MGN = color(35)
        self.CYN = color(36)
        self.WHT = color(37)


class Logger:
    def __init__(self):
        self.prog = f'{clr.BLU}{Path(sys.argv[0]).name}{clr.RST}'
        self.out_func = {'log': self.log, 'info': self.info, 'warning': self.warning, 'error': self.error}

    def log(self, *args, **kwargs):
        print(f'[{self.prog}]', *args, **kwargs, flush=True)

    def info(self, *args):
        self.log(f'{clr.GRN}INFO{clr.RST}:', *args)

    def warning(self, *args):
        self.log(f'{clr.YEL}WARNING{clr.RST}:', *args)

    def error(self, *args):
        self.log(f'{clr.RED}ERROR{clr.RST}:', *args, file=sys.stderr)

    def section(self, *args, _out='log'):
        total_len = 100
        string = ' '.join(args)

        if string:
            part_len = (total_len - len(string)) // 2
            string = f'{"-"*part_len} {string} {"-"*part_len}'[:total_len]  # Strip string to 'total_len'
        else:
            string = f'{"-" * total_len}'

        self.out_func[_out](string)


clr = Colors()
logs = Logger()

if __name__ == '__main__':
    def print_color(color):
        color_code = getattr(clr, color)
        print(f'{color_code}{color}{clr.RST}')

    print_color('BLK')
    print_color('RED')
    print_color('GRN')
    print_color('YEL')
    print_color('BLU')
    print_color('MGN')
    print_color('CYN')
    print_color('WHT')

    print_color('BLD')
    print_color('UDL')

    logs.log('Print log')
    logs.info('Print \'Info\' log')
    logs.warning('Print \'Warning\' log')
    logs.error('Print \'Error\' log')

    logs.section('Print', 'log', 'section')
    logs.section('Print', 'info', 'section', _out='info')
    logs.section('Print', 'warning', 'section', _out='warning')
    logs.section('Print', 'error', 'section', _out='error')
    logs.section()
