
import warnings


class Debugger:
    '''
    a decorator class that will catch exceptions from the decorated function,
    and provide access to the functions global and (when possible) local
    namespaces
    '''

    def __init__(self, func):
        self._func = func
        self.name = func.__name__

    def __call__(self, *args, **kwargs):
        try:
            return self._func(*args, **kwargs)

        except Exception as e:
            # for normal exceptions, it won't be possible to access the function's
            # local namespace
            self.exception = e
            self.globals = self._func.__globals__
            warnings.warn(
                '\n' + '-*' * 15 + '\n'
                + f'debugger caught exception @ {self.name}'
                + '\n' + '-*' * 15 + '\n'
            )

            raise e

