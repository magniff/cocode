from cocode.instruction_base import BaseInstruction


class Pop(BaseInstruction):
    opname = "POP_TOP"


class Add(BaseInstruction):
    opname = "BINARY_ADD"


class Sub(BaseInstruction):
    opname = "BINARY_SUBTRACT"


class Mult(BaseInstruction):
    opname = "BINARY_MULTIPLY"


class Nop(BaseInstruction):
    opname = "NOP"


class Yield(BaseInstruction):
    opname = "YIELD_VALUE"


class Negate(BaseInstruction):
    opname = "UNARY_NEGATIVE"


class Return(BaseInstruction):
    opname = "RETURN_VALUE"


class Rot2(BaseInstruction):
    opname = "ROT_TWO"


class Rot3(BaseInstruction):
    opname = "ROT_THREE"
