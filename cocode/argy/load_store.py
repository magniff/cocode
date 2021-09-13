import watch
from cocode.instruction_base import BaseTwoByteInstruction


class Constant(BaseTwoByteInstruction):
    opname = 'LOAD_CONST'
    arg = watch.builtins.Whatever

    def arg_to_number(self, code_proxy):
        return code_proxy.context.register_constant(self.arg)

class Variable(BaseTwoByteInstruction):
    opname = 'LOAD_NAME'
    arg = watch.builtins.InstanceOf(str)

    def arg_to_number(self, code_proxy):
        return code_proxy.context.register_name(self.arg)

class Global(Variable):
    opname = 'LOAD_GLOBAL'


class VariableFast(BaseTwoByteInstruction):
    opname = 'LOAD_FAST'
    arg = watch.builtins.InstanceOf(str)

    def arg_to_number(self, code_proxy):
        return code_proxy.context.register_varname(self.arg)


class Bind(BaseTwoByteInstruction):
    opname = 'STORE_NAME'
    arg = watch.builtins.InstanceOf(str)

    def arg_to_number(self, code_proxy):
        return code_proxy.context.register_name(self.arg)

class BindFast(BaseTwoByteInstruction):
    opname = 'STORE_FAST'
    arg = watch.builtins.InstanceOf(str)

    def arg_to_number(self, code_proxy):
        return code_proxy.context.register_varname(self.arg)


class List(BaseTwoByteInstruction):
    opname = 'BUILD_LIST'
    arg = watch.builtins.InstanceOf(int)

    def arg_to_number(self, code_proxy):
        return self.arg
