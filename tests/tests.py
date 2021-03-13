import context as ctx
import jupydebug as jpdb


def test_post_mortem_frames(failing_test_pm_frames,
                              nested_test_pm_frames):
    frames = failing_test_pm_frames
    bottom_frame = frames[0]
    assert 'a_local_var' in bottom_frame.locals.keys()
    assert 'a_global_var' in bottom_frame.globals.keys()

    frames = nested_test_pm_frames
    assert 'a_local_var' in frames[0].locals.keys()
    assert 'pf_local_var' in frames[1].locals.keys()
    assert 'nf_local_var' in frames[2].locals.keys()
    assert 'a_global_var' in frames[0].globals.keys()
    assert 'a_global_var' in frames[1].globals.keys()
    assert 'a_global_var' in frames[2].globals.keys()


def test_debugger_captures_frames(failing_test_db_frames):
    frames = failing_test_db_frames
    bottom_frame = frames[0]
    assert 'a_local_var' in bottom_frame.locals.keys()
    assert 'a_global_var' in bottom_frame.globals.keys()
