import string
import math

import hypothesis
from hypothesis import strategies

from cocode import (
    CodeObjectProxy, Constant, Variable, Jump, Add,
    PopJumpTrue, PopJumpFalse, Label, Return
)


ALPHABET = string.ascii_letters + "_" + string.digits


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


@hypothesis.given(
    varname0=strategies.text(min_size=1, alphabet=ALPHABET),
    varname1=strategies.text(min_size=1, alphabet=ALPHABET),
    value0=strategies.floats(),
    value1=strategies.floats(),
)
def test_add_floats(varname0, varname1, value0, value1):
    hypothesis.assume(varname0 != varname1)
    code_proxy = CodeObjectProxy(
        Variable(varname0),
        Variable(varname1),
        Add(),
        Return(),
    )

    stack_result = eval(
        code_proxy.assemble(), {}, {varname0: value0, varname1: value1}
    )
    regular_result = value0 + value1

    assert (
        (stack_result == regular_result) or
        all(map(math.isnan, (stack_result, regular_result)))
    )
