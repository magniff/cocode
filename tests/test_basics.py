from stackmachine import (
    CodeObjectProxy, Constant, Variable, Return, Add, List, Bind
)


def test_constants():
    code_proxy = CodeObjectProxy(
        Constant("Hello "),
        Constant("world!"),
        Add(),
        Return()
    )

    code = code_proxy.assemble()
    assert eval(code) == "Hello world!"


def test_name_binding():
    code_proxy = CodeObjectProxy(
        Constant("Hello"),
        Bind("varname"),
        Constant(None),
        Return()
    )

    code = code_proxy.assemble()
    g = l = dict()
    eval(code, g, l)
    assert "varname" in l
    assert l['varname'] == "Hello"
