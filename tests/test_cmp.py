from cocode import (
    CodeObjectProxy, Variable, Return,
    Compare, Constant, Label, JumpTrue, Jump, Add, Bind, Mult,
)


def test_cmp_op():
    code_proxy = CodeObjectProxy(
        Variable("first"),
        Variable("second"),
        Compare("<"),
        Return(),
    )

    code = code_proxy.assemble()
    assert eval(code, {}, {"first": 1, "second": 2}) == True
    assert eval(code, {}, {"first": 2, "second": 1}) == False


def test_slow_factorial():
    code_proxy = CodeObjectProxy(
        Constant(1),
        Bind("result"),
        Label(Variable("value"), "start"),
        Constant(1),
        Compare("=="),
        JumpTrue("all_done"),
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
