import warnings
import sys
import pandas as pd


class Context:
    '''
    expand on the methods for a python traceback frame
    '''
    def __init__(self, frame):
        '''
        args:
            frame (traceback.tb_frame)
        '''
        self._frame = frame

    def __repr__(self):
        return f'Context for {self.file_name} calling\n\t'\
               f'{self.method_name} @ line {self.line_num}'

    @property
    def line_num(self):
        return self._frame.f_lineno

    @property
    def file_name(self):
        return self._frame.f_code.co_filename

    @property
    def method_name(self):
        return self._frame.f_code.co_name

    @property
    def locals(self):
        return self._frame.f_locals

    @property
    def globals(self):
        return self._frame.f_globals


def post_mortem(traceback=None):
    if traceback is None:
        traceback = sys.last_traceback
    return get_contexts(traceback)


def get_contexts(traceback=None, frame=None):
    # TODO: traceback vs frame input
    # consider adding method to generate contexts from e.g. sys._getframe()
    if frame is not None:
        raise NotImplementedError()
    contexts = []
    while True:
        contexts.append((Context(traceback.tb_frame)))
        traceback = traceback.tb_next
        if not traceback:
            break
    return Contexts(contexts[::-1])


class Contexts(list):
    '''
    this class exists to provide an easy visual for a context stack
    '''

    def __repr__(self):
        return self.to_df().__repr__()

    def _repr_html_(self):
        return self.to_df()._repr_html_()

    def to_df(self):
        return pd.DataFrame({
            'file': [ctx.file_name for ctx in self],
            'line': [ctx.line_num for ctx in self],
            'calling': [ctx.method_name for ctx in self],
            'locals': [ctx.locals.keys() for ctx in self],
        })


class Debugger:
    '''
    a decorator class that will catch exceptions from the decorated method,
    and provide access to the collection of contexts within the
    exception-raising method and its parents.

    TODO: this class has been made largely obsolete by the post_mortem()
    function. It may be useful if I incorporate a break-point type method
    into this package and use this class to manage it.
    '''

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        try:
            return self._func(*args, **kwargs)

        except Exception as e:
            self.exception = e
            self.contexts = get_contexts(self.exception.__traceback__)
            warnings.warn(
                '\n' + '-*' * 15 + '\n'
                f'debugger caught exception @ {self.contexts[0]}'
                '\n' + '-*' * 15 + '\n')
            return self