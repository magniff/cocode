import watch
from .base import BaseInstruction


class Bind(BaseInstruction):

    varname = watch.builtins.InstanceOf(str)

    def __init__(self, varname):
        self.varname = varname

    def render(self, code_proxy):
        name_index = code_proxy.context.register_name(self.varname)
        code_proxy.bytecode.add(self.opmap['STORE_NAME'])
        for value in self.pack_to_short(name_index):
            code_proxy.bytecode.add(value)
