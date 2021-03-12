import context as ctx
import jupydebug as jpdb


def test_post_mortem_contexts(failing_test_pm_contexts,
                              nested_test_pm_contexts):
    contexts = failing_test_pm_contexts
    bottom_context = contexts[0]
    assert 'a_local_var' in bottom_context.locals.keys()
    assert 'a_global_var' in bottom_context.globals.keys()

    contexts = nested_test_pm_contexts
    assert 'a_local_var' in contexts[0].locals.keys()
    assert 'pf_local_var' in contexts[1].locals.keys()
    assert 'nf_local_var' in contexts[2].locals.keys()
    assert 'a_global_var' in contexts[0].globals.keys()
    assert 'a_global_var' in contexts[1].globals.keys()
    assert 'a_global_var' in contexts[2].globals.keys()


def test_debugger_captures_contexts(failing_test_db_contexts):
    contexts = failing_test_db_contexts
    bottom_context = contexts[0]
    assert 'a_local_var' in bottom_context.locals.keys()
    assert 'a_global_var' in bottom_context.globals.keys()
