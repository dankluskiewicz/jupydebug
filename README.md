# jupydebug

```python
a_failing_test()
```

```python

---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-14-ac3ec94daf8d> in <module>()
----> 1 a_failing_test()

/home/dan/Documents/jupydebug/tests/conftest.py in nested_test()
     28 def nested_test():
     29     nf_local_var = "nested_test's_local_var"
---> 30     return parent_test(failing_test)
     31 
     32 

/home/dan/Documents/jupydebug/tests/conftest.py in parent_test(func, *args, **kwargs)
     23 def parent_test(func, *args, **kwargs):
     24     pf_local_var = "parent test's local var"
---> 25     return func(*args, **kwargs)
     26 
     27 

/home/dan/Documents/jupydebug/tests/conftest.py in failing_test()
     10     a_local_var = "failing_test's local var"
     11     x = range(3)
---> 12     y = x[3]  # this will raise an exception
     13     return y
     14 

IndexError: range object index out of range
    
```

get access to the traceback stack with jupydebug's post_mortem function:

```python
contexts = jpdb.post_mortem()
```
inspect the stack:
```python
contexts
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>file</th>
      <th>line</th>
      <th>calling</th>
      <th>locals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>/home/dan/Documents/jupydebug/tests/conftest.py</td>
      <td>12</td>
      <td>failing_test</td>
      <td>(a_local_var, x)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>/home/dan/Documents/jupydebug/tests/conftest.py</td>
      <td>25</td>
      <td>parent_test</td>
      <td>(func, args, kwargs, pf_local_var)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>/home/dan/Documents/jupydebug/tests/conftest.py</td>
      <td>30</td>
      <td>nested_test</td>
      <td>(nf_local_var)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>&lt;ipython-input-12-ac3ec94daf8d&gt;</td>
      <td>1</td>
      <td>&lt;module&gt;</td>
      <td>(__name__, __doc__, __package__, __loader__, __spec__, __builtin__, __builtins__, _ih, _oh, _dh, _sh, In, Out, get_ipython, exit, quit, _, __, ___, sys, _i, _ii, _iii, _i1, context, jpdb, conftest, _i2, contexts, _i3, _3, _i4, _i5, _i6, _6, _i7, debugger, _7, _i8, _8, _i9, _i10, _i11, a_failing_test, _i12, _i13, _13, _i14, df, _i15, _15, _i16)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>/home/dan/miniconda3/envs/jupydebug/lib/python3.7/site-packages/IPython/core/interactiveshell.py</td>
      <td>2898</td>
      <td>run_code</td>
      <td>(self, code_obj, result, old_excepthook, outflag)</td>
    </tr>
  </tbody>
</table>

and access the local or global variables in each context with

```python
contexts[0].locals
```

```
{'a_local_var': "failing_test's local var", 'x': range(0, 3)}
```

```python
contexts[0].globals
```

```
{'__name__': 'conftest',
 '__doc__': None,
 '__package__': '',
 '__loader__': <_frozen_importlib_external.SourceFileLoader at 0x7fac7027d990>,
 '__spec__': ModuleSpec(name='conftest', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7fac7027d990>, origin='/home/dan/Documents/jupydebug/tests/conftest.py'),
 '__file__': '/home/dan/Documents/jupydebug/tests/conftest.py',
 '__cached__': '/home/dan/Documents/jupydebug/tests/__pycache__/conftest.cpython-37.pyc',
 '__builtins__': {'__name__': 'builtins',
  '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.",
  '__package__': '',...
```

