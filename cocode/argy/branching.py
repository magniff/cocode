import watch

from cocode.instruction_base import BaseArgyInstruction, BaseInstruction


class Label(BaseInstruction):
    instruction = watch.builtins.InstanceOf(BaseInstruction)
    label_name = watch.builtins.InstanceOf(str)

    def __len__(self):
        return len(self.instruction)

    def __init__(self, instruction, label_name):
        self.instruction = instruction
        self.label_name = label_name

    def set_position(self, position):
        self.instruction.set_position(position)

    def get_position(self):
        return self.instruction.get_position()

    def render(self, code_proxy):
        return self.instruction.render(code_proxy)


class BaseJumpInstruction(BaseArgyInstruction):
    arg = watch.builtins.InstanceOf(str)

    def arg_to_number(self, code_proxy):
        return code_proxy.label_map[self.arg]


class Jump(BaseJumpInstruction):
    opname = "JUMP_ABSOLUTE"


class PopJumpTrue(BaseJumpInstruction):
    opname = "POP_JUMP_IF_TRUE"


class PopJumpFalse(BaseJumpInstruction):
    opname = "POP_JUMP_IF_FALSE"
