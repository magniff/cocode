# COCODE (code cocode, duuh)

Simple assembly-like language, which can be used to program CPython directly:
```python
from cocode import CodeObjectProxy, Constant, Return, Add

code_proxy = CodeObjectProxy(
  Constant("Hello "),
  Constant("world!"),
  Add(),
  Return()
)

code = code_proxy.assemble()
assert eval(code) == "Hello world!"
```

As you can see, `cocode` doesn't introduce any additional complexity:
```python
>>> import dis
>>> dis.dis(code)
  0           0 LOAD_CONST               0 ('Hello ')
              3 LOAD_CONST               1 ('world!')
              6 BINARY_ADD
              7 RETURN_VALUE
```

To be continued...
