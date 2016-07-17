from cocode import (
    CodeObjectProxy, Constant, Jump, Label, Return
)


def test_constants():
    code_proxy = CodeObjectProxy(
        Constant("First"),
        Jump("mylabel"),
        Return(),
        Constant("Second"),
        Label(Return(), "mylabel"),
    )

    code = code_proxy.assemble()
    assert eval(code) == "First"
