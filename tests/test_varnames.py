import pytest

from cocode import (
    CodeObjectProxy, Variable, Return, Dup, Rot2,
    Compare, Constant, Label, PopJumpTrue, Jump, Add, Bind, Mult
)

from cocode.argy.load_store import VariableFast


def test_simple_varname_0():

    def func(varname0, varname1):
        pass

    code_proxy = CodeObjectProxy(
        VariableFast("varname1"),
        Return(),
        interface=func
    )
    code = code_proxy.assemble(code_flags=67)
    func.__code__ = code

    assert func("hello", "world") == "world"


def test_simple_varname_1():

    def func(varname0, varname1):
        pass

    code_proxy = CodeObjectProxy(
        VariableFast("varname0"),
        VariableFast("varname1"),
        Add(),
        Return(),
        interface=func
    )
    code = code_proxy.assemble(code_flags=67)
    func.__code__ = code

    assert func("hello", "world") == "helloworld"


def test_simple_varname_2():

    def func(varname0, varname1):
        pass

    code_proxy = CodeObjectProxy(
        VariableFast("varname0"),
        Constant("_"),
        Add(),
        VariableFast("varname1"),
        Add(),
        Return(),
        interface=func
    )
    code = code_proxy.assemble(code_flags=67)
    func.__code__ = code

    assert func("hello", "world") == "hello_world"
