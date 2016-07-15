import types
import struct
import opcode


import watch


class BaseEntityDescriptor(watch.WatchMe):

    def __init__(self, value):
        self.value = value


class Const(BaseEntityDescriptor):
    pass


class Name(BaseEntityDescriptor):
    value = watch.builtins.InstanceOf(str)


class BaseInstruction(watch.WatchMe):
    opmap = opcode.opmap

    def pack_to_short(self, value):
        return struct.pack("<H", value)

    def render(self, code_proxy):
        """
        Mutates state of CodeProxy
        """
        raise NotImplementedError(
            "method 'render' is not implemented for %s." % repr(self)
        )


class Push(BaseInstruction):
    entity_descriptor = watch.builtins.InstanceOf(BaseEntityDescriptor)

    def __init__(self, entity_descriptor):
        self.entity_descriptor = entity_descriptor

    def push_constant(self, code_proxy, value_to_push):
        constant_index = code_proxy.context.register_constant(value_to_push)

        code_proxy.bytecode.add(self.opmap['LOAD_CONST'])
        for value in self.pack_to_short(constant_index):
            code_proxy.bytecode.add(value)

    def push_name(self, code_proxy, value_to_push):
        name_index = code_proxy.context.register_name(value_to_push)

        code_proxy.bytecode.add(self.opmap['LOAD_NAME'])
        for value in self.pack_to_short(name_index):
            code_proxy.bytecode.add(value)

    def render(self, code_proxy):
        value_to_push = self.entity_descriptor.value
        if isinstance(self.entity_descriptor, Const):
            self.push_constant(code_proxy, value_to_push)
        elif isinstance(self.entity_descriptor, Name):
            self.push_name(code_proxy, value_to_push)
        else:
            raise TypeError(
                "Unknown entity descriptor %s." % self
            )


class Bind(BaseInstruction):

    entity_descriptor = watch.builtins.InstanceOf(Name)

    def __init__(self, entity_descriptor):
        self.entity_descriptor = entity_descriptor

    def render(self, code_proxy):
        name_index = code_proxy.context.register_name(
            self.entity_descriptor.value
        )
        code_proxy.bytecode.add(self.opmap['STORE_NAME'])
        for value in self.pack_to_short(name_index):
            code_proxy.bytecode.add(value)


class Pop(BaseInstruction):
    """
    Pops tip of the stack.
    """

    def render(self, code_proxy):
        code_proxy.bytecode.add(self.opmap['POP_TOP'])


class Add(BaseInstruction):
    """
    Pops tip of the stack.
    """

    def render(self, code_proxy):
        code_proxy.bytecode.add(self.opmap['BINARY_ADD'])


class Nop(BaseInstruction):
    """
    Do nothing instruction.
    """

    def render(self, code_proxy):
        code_proxy.bytecode.add(self.opmap['NOP'])


class Yield(BaseInstruction):

    def render(self, code_proxy):
        code_proxy.bytecode.add(self.opmap['YIELD_VALUE'])


class Ret(BaseInstruction):

    def render(self, code_proxy):
        code_proxy.bytecode.add(self.opmap['RETURN_VALUE'])


class ContextProxy:

    def _push_value_in_context(self, value, context_field):
        if value in context_field:
            index = context_field.index(value)
        else:
            context_field.append(value)
            index = self._push_value_in_context(value, context_field)
        return index

    def register_name(self, name):
        return self._push_value_in_context(name, self.names)

    def register_constant(self, name):
        return self._push_value_in_context(name, self.constants)

    @property
    def nlocals(self):
        return len(self.names)

    def __init__(self):
        self.names = list()
        self.varnames = list()
        self.constants = list()


class BytecodeProxy:

    def add(self, value):
        self.bytes.append(value)

    @property
    def stacksize(self):
        return 10

    def __init__(self):
        self.bytes = list()


class CodeObjectProxy(watch.WatchMe):

    bytecode = BytecodeProxy
    context = ContextProxy
    instructions = watch.ArrayOf(watch.builtins.InstanceOf(BaseInstruction))

    def __init__(self, *instructions):
        self.instructions = instructions
        self.context = self.context()
        self.bytecode = self.bytecode()

    def assemble(self):
        for instruction in self.instructions:
            instruction.render(self)

        return types.CodeType(
            0,                              # argcount
            0,                              # kwonlyargcount
            self.context.nlocals,           # nlocals
            self.bytecode.stacksize,        # stacksize
            67,                             # flags
            bytes(self.bytecode.bytes),     # codestring
            tuple(self.context.constants),  # constants
            tuple(self.context.names),      # names
            tuple(self.context.varnames),   # varnames
            '<string>',                     # filename
            '<noname code object>',         # name
            0,                              # firstlineno
            bytes()                         # lnotab
        )
