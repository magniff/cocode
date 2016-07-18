from cocode import (
    CodeObjectProxy, Constant, Variable, Jump,
    PopJumpTrue, PopJumpFalse, Label, Return
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


def test_jump_true():
    code_proxy = CodeObjectProxy(
        Variable("condition"),
        PopJumpTrue("mylabel"),
        Constant("False branch!"),
        Return(),
        Label(Constant("True branch!"), "mylabel"),
        Return(),
    )

    code = code_proxy.assemble()
    assert eval(code, {}, {"condition": True}) == "True branch!"
    assert eval(code, {}, {"condition": False}) == "False branch!"


def test_jump_false():
    code_proxy = CodeObjectProxy(
        Variable("condition"),
        PopJumpFalse("mylabel"),
        Constant("False branch!"),
        Return(),
        Label(Constant("True branch!"), "mylabel"),
        Return(),
    )

    code = code_proxy.assemble()
    assert eval(code, {}, {"condition": False}) == "True branch!"
    assert eval(code, {}, {"condition": True}) == "False branch!"
