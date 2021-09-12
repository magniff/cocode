from cocode import (
    CodeObjectProxy, Variable, Return, Compare,
)


def test_cmp_op():
    code_proxy = CodeObjectProxy(
        Variable("first"),
        Variable("second"),
        Compare("<"),
        Return(),
    )

    code = code_proxy.assemble(code_flags=64)
    assert eval(code, {}, {"first": 1, "second": 2}) == True
    assert eval(code, {}, {"first": 2, "second": 1}) == False
