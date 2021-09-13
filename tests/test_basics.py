from cocode import (
    CodeObjectProxy, Constant, Variable, Return, Add, List, Bind, Yield, Pop,
    Global, CallFunction, VariableFast, BindFast
)
import dis


def test_return_constant():
    code_proxy = CodeObjectProxy(
        Constant("foobar"),
        Return()
    )

    code = code_proxy.assemble(code_flags=64)
    assert eval(code) == "foobar"


def test_add_two_constants():
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
        Constant("someconst"),
        Bind("varname"),
        Constant(None),
        Return()
    )

    code = code_proxy.assemble(code_flags=64)
    locals_dict = dict()
    eval(code, {}, locals_dict)

    assert "varname" in locals_dict
    assert locals_dict['varname'] == "someconst"


def test_variable_simple():
    code_proxy = CodeObjectProxy(
        Constant("Hello "),
        Variable("string"),
        Add(),
        Bind("new_var"),
        Variable("new_var"),
        Return()
    )

    code = code_proxy.assemble(code_flags=64)
    locals_dict = {'string': "world!"}
    assert eval(code, {}, locals_dict) == "Hello world!"
    assert locals_dict["new_var"] == "Hello world!"


def test_global_simple_0():
    code_proxy = CodeObjectProxy(
        Global('global_var'),
        Variable('local_var'),
        Add(),
        Return(),
    )

    code = code_proxy.assemble(code_flags=64)
    assert eval(code, {'global_var': 1}, {'local_var': 2}) == 3


def test_global_function_call():
    def add(a, b):
        return a + b

    code_proxy = CodeObjectProxy(
        Global("sum"),
        Constant(10),
        Constant(20),
        CallFunction(2),
        Return(),
    )

    code = code_proxy.assemble(code_flags=64)
    assert eval(code, {"sum": add}, {}) == 30


def test_global_function_call_inside_function():
    def function(a, b):
        pass

    code_proxy = CodeObjectProxy(
        Global("sum"),
        VariableFast("a"),
        VariableFast("b"),
        List(2),
        CallFunction(1),
        Return(),
        interface=function
    )

    code = code_proxy.assemble(code_flags=64)
    function.__code__ = code
    assert function(10, 20) == 30


def test_list_simple():
    code_proxy = CodeObjectProxy(
        Constant("Hello"),
        Constant("world"),
        List(2),
        Return(),
    )

    code = code_proxy.assemble(code_flags=64)
    assert eval(code) == ["Hello", "world"]


# def test_simple_generator():
#     def my_gen():
#         yield

#     code_proxy = CodeObjectProxy(
#         Constant(1),
#         Constant(2),
#         Constant(3),
#         Yield(),
#         Pop(),
#         Yield(),
#         Pop(),
#         Yield(),
#         interface=my_gen
#     )
#     my_gen.__code__ = code_proxy.assemble(code_flags=99)
#     gen = my_gen()

#     assert next(gen) == 3
#     assert next(gen) == 2
#     assert next(gen) == 1
