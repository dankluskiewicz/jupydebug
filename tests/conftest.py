import pytest
import context as ctx
import jupydebug as jpdb

a_global_var = 'global var'
another_global_var = 'another global var'


def failing_test():
    a_local_var = "failing_test's local var"
    x = range(3)
    y = x[3]  # this will raise an exception
    return y


def passing_test():
    a_local_var = "passing_test's local var"
    x = range(3)
    y = x[2]
    return y


def parent_test(func, *args, **kwargs):
    pf_local_var = "parent test's local var"
    return func(*args, **kwargs)


def nested_test():
    nf_local_var = "nested_test's_local_var"
    return parent_test(failing_test)


@pytest.fixture
def failing_test_debugger():
    with pytest.warns(UserWarning):
        debugger = jpdb.Debugger(failing_test)
        debugger()
    return debugger


@pytest.fixture
def failing_test_db_frames(failing_test_debugger):
    return failing_test_debugger.frames


@pytest.fixture
def failing_test_pm_frames():
    try:
        failing_test()
    except IndexError as ie:
        return jpdb.post_mortem(ie.__traceback__)


@pytest.fixture
def nested_test_pm_frames():
    try:
        nested_test()
    except IndexError as ie:
        return jpdb.post_mortem(ie.__traceback__)
