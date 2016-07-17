from cocode import (
    CodeObjectProxy, Constant, JumpToLabel, Label, Return
)


def test_constants():
    code_proxy = CodeObjectProxy(
        Constant("First"),
        JumpToLabel("mylabel"),
        Return(),
        Constant("Second"),
        Label(Return(), "mylabel"),
    )

    code = code_proxy.assemble()
    assert eval(code) == "First"
