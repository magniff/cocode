import types
import watch

from .base import BaseInstruction


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
