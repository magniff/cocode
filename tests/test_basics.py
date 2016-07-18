from cocode import (
    CodeObjectProxy, Constant, Variable, Return, Add, List, Bind, Yield, Pop,
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


def test_simple_generator():
    def my_gen():
        pass

    code_proxy = CodeObjectProxy(
        Constant(1),
        Constant(2),
        Constant(3),
        Yield(),
        Pop(),
        Yield(),
        Pop(),
        Yield(),
        interface=my_gen
    )
    my_gen.__code__ = code_proxy.assemble(code_flags=99)
    gen = my_gen()

    assert next(gen) == 3
    assert next(gen) == 2
    assert next(gen) == 1
