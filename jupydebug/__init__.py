
import warnings
import sys


class Debugger:
    '''
    a decorator class that will catch exceptions from the decorated function,
    and provide access to the functions global and (when possible) local
    namespaces
    '''

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        try:
            return self._func(*args, **kwargs)

        except Exception as e:
            self.exception = e
            self.frames = get_frames(self.exception.__traceback__)
            warnings.warn(
                '\n' + '-*' * 15 + '\n'
                f'debugger caught exception @ {self._func.__name__}'
                '\n' + '-*' * 15 + '\n')
            print('')
            raise e


class Frame:
    '''
    expand on the methods for a traceback frame
    '''
    def __init__(self, tb_frame):
        self._tb_frame = tb_frame

    def __repr__(self):
        return f'jupyterdebug Frame for {self.file_name} calling\n\t'\
               f'{self.method_name} @ line {self.line_num}'

    @property
    def line_num(self):
        return self._tb_frame.f_lineno

    @property
    def file_name(self):
        return self._tb_frame.f_code.co_filename

    @property
    def method_name(self):
        return self._tb_frame.f_code.co_name

    @property
    def locals(self):
        return self._tb_frame.f_locals

    @property
    def globals(self):
        return self._tb_frame.f_globals


def post_mortem():
    last_traceback = sys.last_traceback()
    # TODO


def get_frames(traceback=None, frames=None):
    frames = []
    # TODO: tb vs frames input
    while True:
        frames.append((Frame(traceback.tb_frame)))
        traceback = traceback.tb_next
        if not traceback:
            break
    return frames
