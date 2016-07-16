import watch
from .base import BaseInstruction


class BasePusher(BaseInstruction):
    pass


class Constant(BasePusher):
    value = watch.builtins.Whatever

    def __init__(self, value):
        self.value = value

    def render(self, code_proxy):
        constant_index = code_proxy.context.register_constant(self.value)

        code_proxy.bytecode.add(self.opmap['LOAD_CONST'])
        for value in self.pack_to_short(constant_index):
            code_proxy.bytecode.add(value)


class Variable(BasePusher):
    varname = watch.builtins.InstanceOf(str)

    def __init__(self, varname):
        self.varname = varname

    def render(self, code_proxy):
        name_index = code_proxy.context.register_name(self.varname)

        code_proxy.bytecode.add(self.opmap['LOAD_NAME'])
        for value in self.pack_to_short(name_index):
            code_proxy.bytecode.add(value)


class List(BasePusher):
    count = watch.builtins.InstanceOf(int)

    def __init__(self, count):
        self.count = count

    def render(self, code_proxy):
        code_proxy.bytecode.add(self.opmap['BUILD_LIST'])
        for value in self.pack_to_short(self.count):
            code_proxy.bytecode.add(value)
