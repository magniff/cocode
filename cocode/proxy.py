import types
import watch

from cocode.instruction_base import BaseInstruction


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
        self.varnames = self.names
        self.constants = list()


class BytecodeProxy:

    def get_label(self, label_name):
        return self.labels[label_name]

    def set_label(self, label_name):
        if label_name not in self.labels:
            self.labels[label_name] = self.current_position
        else:
            raise ValueError("Redifinition of label %s." % label_name)

    def add(self, value):
        self.bytes.append(value)

    @property
    def current_position(self):
        return len(self.bytes)

    @property
    def stacksize(self):
        return 3

    def __init__(self):
        self.labels = dict()
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
            64,                             # flags
            bytes(self.bytecode.bytes),     # codestring
            tuple(self.context.constants),  # constants
            tuple(self.context.names),      # names
            tuple(self.context.varnames),   # varnames
            '<string>',                     # filename
            '<noname code object>',         # name
            0,                              # firstlineno
            bytes()                         # lnotab
        )
