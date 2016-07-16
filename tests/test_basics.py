from cocode import (
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
    locals_dict = dict()
    eval(code, {}, locals_dict)
    assert "varname" in locals_dict
    assert locals_dict['varname'] == "Hello"


def test_variable_simple():
    code_proxy = CodeObjectProxy(
        Constant("Hello "),
        Variable("string"),
        Add(),
        Bind("new_var"),
        Variable("new_var"),
        Return()
    )

    code = code_proxy.assemble()
    locals_dict = {'string': "world!"}
    assert eval(code, {}, locals_dict) == "Hello world!"
    assert locals_dict["new_var"] == "Hello world!"


def test_list_simple():
    code_proxy = CodeObjectProxy(
        Constant("Hello"),
        Constant("world"),
        List(2),
        Return(),
    )

    code = code_proxy.assemble()
    assert eval(code) == ["Hello", "world"]
