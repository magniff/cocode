from cocode import (
    CodeObjectProxy, Variable, Return, Dup, Rot2, Rot3, VariableFast,
    Compare, Constant, Label, PopJumpTrue, Jump, Add, Sub, Bind, Mult,
    Pop, PopJumpFalse, Yield
)


def test_slow_factorial():
    code_proxy = CodeObjectProxy(
        Constant(1),
        Bind("result"),
        Label(Variable("value"), "start"),
        Constant(1),
        Compare("=="),
        PopJumpTrue("all_done"),
        Variable("value"),
        Variable("result"),
        Mult(),
        Bind("result"),
        Variable("value"),
        Constant(-1),
        Add(),
        Bind("value"),
        Jump("start"),
        Label(Variable("result"), "all_done"),
        Return(),
    )

    code = code_proxy.assemble()
    assert eval(code, {}, {"value": 10}) == 3628800


def test_fast_factorial():
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
    assert factorial_asm(10) == 3628800


def test_fib():
    def fib(a, b):
        pass

    fib_asm = CodeObjectProxy(
        VariableFast('a'),
        VariableFast('b'),
        Label(Dup(), "loop"),
        Rot3(),
        Add(),
        Dup(),
        Yield(),
        Pop(),
        Jump("loop"),
        interface=fib,
    )

    fib_code = fib_asm.assemble(code_flags=99)
    fib.__code__ = fib_code

    f = fib(1, 1)
    assert next(f) == 2
    assert next(f) == 3
    assert next(f) == 5
