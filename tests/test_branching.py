from cocode import (
    CodeObjectProxy, Constant, Jump, JumpTrue, JumpFalse, Label, Return
)


def test_absolute_jump0():
    code_proxy = CodeObjectProxy(
        Constant("First"),
        Jump("mylabel"),
        Return(),
        Constant("Second"),
        Label(Return(), "mylabel"),
    )

    code = code_proxy.assemble()
    assert eval(code) == "First"


def test_jump_true0():
    code_proxy = CodeObjectProxy(
        Constant(True),
        JumpTrue("mylabel"),
        Return(),
        Label(Constant("True branch!"), "mylabel"),
        Return(),
    )

    code = code_proxy.assemble()
    assert eval(code) == "True branch!"


def test_jump_true1():
    code_proxy = CodeObjectProxy(
        Constant(False),
        JumpTrue("mylabel"),
        Constant("False branch!"),
        Return(),
        Label(Constant("True branch!"), "mylabel"),
        Return(),
    )

    code = code_proxy.assemble()
    assert eval(code) == "False branch!"
