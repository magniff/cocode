from cocode import (
    CodeObjectProxy, Variable, Return,
    Compare, Constant, Label, JumpTrue, Jump, Add, Bind, Mult,
)
from cocode.argy.load_store import VariableFast


def test_simple_varname():

    def func(varname0, varname1):
        pass

    code_proxy = CodeObjectProxy(
        VariableFast("varname1"),
        Return(),
        args=2,
        interface=func
    )
    code_proxy.flags = 67
    code = code_proxy.assemble()
    func.__code__ = code

    assert func("hello", "world") == "world"
