from cocode.instruction_base import BaseInstruction


class Pop(BaseInstruction):
    opname = "POP_TOP"


class Add(BaseInstruction):
    opname = "BINARY_ADD"

    def render(self, code_proxy):
        super().render(code_proxy)
        code_proxy.bytecode.add(0)


class Sub(BaseInstruction):
    opname = "BINARY_SUBTRACT"


class Mult(BaseInstruction):
    opname = "BINARY_MULTIPLY"


class Nop(BaseInstruction):
    opname = "NOP"


class Yield(BaseInstruction):
    """For some reason Cpython retains None on top of the stack after yield.
    WTF alarm!
    """
    opname = "YIELD_VALUE"


class Negate(BaseInstruction):
    opname = "UNARY_NEGATIVE"


class Return(BaseInstruction):
    opname = "RETURN_VALUE"

    def render(self, code_proxy):
        super().render(code_proxy)
        code_proxy.bytecode.add(0)


class Rot2(BaseInstruction):
    opname = "ROT_TWO"


class Rot3(BaseInstruction):
    opname = "ROT_THREE"


class Dup(BaseInstruction):
    opname = "DUP_TOP"
