import watch

from cocode.instruction_base import BaseInstruction


class Label(BaseInstruction):
    label_name = watch.builtins.InstanceOf(str)

    def __init__(self, label_name):
        self.label_name = label_name

    def render(self, code_proxy):
        code_proxy.bytecode.set_label(self.label_name)


class JumpTo(BaseInstruction):
    label_name = watch.builtins.InstanceOf(str)
    condition = watch.SomeOf(
        watch.builtins.InstanceOf(bool),
        watch.builtins.EqualsTo(None)
    )

    def __init__(self, label_name, condition=None):
        self.label_name = label_name
        self.condition = condition

    def render(self, code_proxy):
        target = code_proxy.bytecode.get_label(self.label_name)
        code_proxy.bytecode.add(self.opmap["JUMP_ABSOLUTE"])
        for value in self.pack_to_short(target):
            code_proxy.bytecode.add(value)
