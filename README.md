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

###EXAMPLE: factorial function:
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


###EXAMPLE: fibonacci generator:
```python
def fibonacci(a, b):
    pass

fib_asm_code = CodeObjectProxy(
    VariableFast('a'),
    VariableFast('b'),
    Label(Dup(), "loop"),
    Rot3(),
    Add(),
    Dup(),
    Yield(),
    Pop(),
    Jump("loop"),
    interface=fibonacci,
)

fib_code = fib_asm_code.assemble(code_flags=99)  # make me generator
fibonacci.__code__ = fib_code

iterator = fibonacci(1, 1)

>>> print(next(iterator))
2
>>> print(next(iterator))
3
>>> print(next(iterator))
5
```

Even though this code runs faster then
```python
def fib(a, b):
    while 1:
        a,b = b,a+b
        yield b
```
it seams that most of the time interpreter spending at YIELD_VALUE instruction.
