from .base import BaseInstruction


class NoArgInstruction(BaseInstruction):
    opcode = None

    def render(self, code_proxy):
        code_proxy.bytecode.add(self.opmap[self.opcode])


class Pop(NoArgInstruction):
    opcode = "POP_TOP"


class Add(NoArgInstruction):
    opcode = "BINARY_ADD"


class Nop(NoArgInstruction):
    opcode = "NOP"


class Yield(NoArgInstruction):
    opcode = "YIELD_VALUE"


class Negate(NoArgInstruction):
    opcode = "UNARY_NEGATIVE"


class Return(NoArgInstruction):
    opcode = "RETURN_VALUE"


class Rot2(NoArgInstruction):
    opcode = "ROT_TWO"


class Rot3(NoArgInstruction):
    opcode = "ROT_THREE"
