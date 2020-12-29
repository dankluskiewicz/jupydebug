import pytest
import jupydebug as jpdb

a_global_var = 'global var'
another_global_var = 'another global var'


def failing_test():
    a_local_var = "failing_test's local var"
    x = range(3)
    y = x[3]  # this will raise an exception
    return y


def passing_test():
    a_local_var = "failing_test's local var"
    x = range(3)
    y = x[2]  # this will raise an exception
    return y


def parent_function(func, *args, **kwargs):
    pf_local_var = 'parent funcs local var'
    return func(*args, **kwargs)


def nested_funcs():
    nf_local_var = 'nf_local_var'
    return parent_function(failing_test)


def get_frame():
    a_local_var = 'a_local_var'
    import sys
    return sys._getframe()


@pytest.fixture
def failing_test_debugger():
    with pytest.raises(IndexError):
        with pytest.warns(UserWarning):
            debugger = jpdb.Debugger(failing_test)
            debugger()
    return debugger