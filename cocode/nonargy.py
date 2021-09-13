from cocode.instruction_base import BaseInstruction, BasePaddedInstruction


class Pop(BasePaddedInstruction):
    opname = "POP_TOP"


class Add(BasePaddedInstruction):
    opname = "BINARY_ADD"


class Sub(BasePaddedInstruction):
    opname = "BINARY_SUBTRACT"


class Mult(BasePaddedInstruction):
    opname = "BINARY_MULTIPLY"


class Nop(BaseInstruction):
    opname = "NOP"


class Yield(BasePaddedInstruction):
    """For some reason Cpython retains None on top of the stack after yield.
    WTF alarm!
    """
    opname = "YIELD_VALUE"


class Negate(BaseInstruction):
    opname = "UNARY_NEGATIVE"


class Return(BasePaddedInstruction):
    opname = "RETURN_VALUE"

class Rot2(BaseInstruction):
    opname = "ROT_TWO"


class Rot3(BaseInstruction):
    opname = "ROT_THREE"


class Dup(BaseInstruction):
    opname = "DUP_TOP"
