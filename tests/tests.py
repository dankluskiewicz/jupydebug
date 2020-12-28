import context
import jupydebug as jpdb
import pytest
import fixtures
from fixtures import failing_test_debugger


def test_debugger_wraps_functions():
    with pytest.raises(IndexError):
        with pytest.warns(UserWarning):
            debugger = jpdb.Debugger(fixtures.failing_test())


def test_debugger_captures_globals(failing_test_debugger):
    assert 'a_global_var' in failing_test_debugger.globals.keys()
