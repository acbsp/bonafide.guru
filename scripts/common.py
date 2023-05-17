import signal
import traceback
from typing import Callable

from .exceptions import NoTracebackException
from .logs import logs

__all__ = [
    'return_exit_code',
]


def signal_handler(signal_number, stack_frame):
    raise KeyboardInterrupt


def return_exit_code(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> int:
        signal.signal(signal.SIGTERM, signal_handler)

        try:
            func(*args, **kwargs)
            return 0
        except NoTracebackException:
            return 1
        except Exception:  # pylint: disable=broad-except
            logs.section('Traceback start', _out='error')
            traceback.print_exc()
            logs.section('Traceback end', _out='error')
            return 1

    return wrapper
