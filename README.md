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

Have a look at factorial example:
```python
def factorial_asm(value):
    pass


factorial_asm_proxy = CodeObjectProxy(
    VariableFast("value"),
    Dup(),
    Label(Constant(1), "loop"),
    Sub(),
    Dup(),
    Rot3(),
    Mult(),
    Rot2(),
    Dup(),
    Constant(1),
    Compare("=="),
    PopJumpFalse("loop"),
    Pop(),
    Return(),
    interface=factorial_asm,
)

fac_asm_code = factorial_asm_proxy.assemble()
factorial_asm.__code__ = fac_asm_code
```
Then you may use it as always
```python
assert factorial_asm(10) == 3628800
```
