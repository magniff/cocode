import watch
from cocode.instruction_base import BaseArgyInstruction


class Constant(BaseArgyInstruction):
    opname = 'LOAD_CONST'
    arg = watch.builtins.Whatever

    def __len__(self):
        return 2

    def arg_to_number(self, code_proxy):
        return code_proxy.context.register_constant(self.arg)
    
    def render(self, code_proxy):
        super().render(code_proxy)
        for value in self.pack_to_byte(self.arg_to_number(code_proxy)):
            code_proxy.bytecode.add(value)

class Variable(BaseArgyInstruction):
    opname = 'LOAD_NAME'
    arg = watch.builtins.InstanceOf(str)

    def arg_to_number(self, code_proxy):
        return code_proxy.context.register_name(self.arg)


class Global(Variable):
    opname = 'LOAD_GLOBAL'


class VariableFast(BaseArgyInstruction):
    opname = 'LOAD_FAST'
    arg = watch.builtins.InstanceOf(str)

    def arg_to_number(self, code_proxy):
        return code_proxy.context.register_varname(self.arg)


class Bind(BaseArgyInstruction):
    opname = 'STORE_NAME'
    arg = watch.builtins.InstanceOf(str)

    def arg_to_number(self, code_proxy):
        return code_proxy.context.register_name(self.arg)


class BindFast(BaseArgyInstruction):
    opname = 'STORE_FAST'
    arg = watch.builtins.InstanceOf(str)

    def arg_to_number(self, code_proxy):
        return code_proxy.context.register_varname(self.arg)


class List(BaseArgyInstruction):
    opname = 'BUILD_LIST'
    arg = watch.builtins.InstanceOf(int)

    def arg_to_number(self, code_proxy):
        return self.arg
