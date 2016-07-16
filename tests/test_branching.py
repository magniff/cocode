from cocode import (
    CodeObjectProxy, Constant, Return, Add, JumpTo, Label, Return
)

# 
# def test_constants():
#     code_proxy = CodeObjectProxy(
#         Constant("First"),
#         JumpTo()
#         Return(),
#         
#         Constant("Second"),
#         Label("")
#         Return()
#     )
# 
#     code = code_proxy.assemble()
#     assert eval(code) == "Hello world!"
