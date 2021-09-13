import types
import watch

from cocode.instruction_base import BaseInstruction
from cocode.argy.branching import Label


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

    def register_varname(self, name):
        return self._push_value_in_context(name, self.varnames)

    def register_constant(self, name):
        return self._push_value_in_context(name, self.constants)

    def __init__(self, interface):
        self.names = list(interface.__code__.co_names)
        self.varnames = list(interface.__code__.co_varnames)
        self.constants = list(interface.__code__.co_consts)


class BytecodeProxy(watch.WatchMe):

    bytes = watch.builtins.Container(watch.builtins.InstanceOf(int), container=list)

    def add(self, value):
        self.bytes.append(value)

    @property
    def stacksize(self):
        return 1000

    def __init__(self):
        self.bytes = list()


class CodeObjectProxy(watch.WatchMe):

    bytecode = BytecodeProxy
    context = ContextProxy
    instructions = watch.builtins.Container(
        watch.builtins.InstanceOf(BaseInstruction), container=list
    )
    label_map = watch.builtins.InstanceOf(str) >> watch.builtins.InstanceOf(int)
    interface = watch.builtins.InstanceOf(types.FunctionType)

    def __init__(self, *instr, interface=(lambda: None)):
        self.instructions = list(instr)
        self.interface = interface

    def assemble(self, code_flags=67):
        # create new proxy instances on every assembly request
        self.context = type(self).context(self.interface)
        self.bytecode = type(self).bytecode()
        self.label_map = dict()

        # calculation of byte shift for every instruction
        current_position = 0
        for instruction in self.instructions:
            instruction.set_position(current_position)
            current_position += len(instruction)

        # finally setting up label map
        self.label_map = {
            label.label_name: label.get_position() for
            label in self.instructions if isinstance(label, Label)
        }

        # now everything is ready to render instructions
        for instruction in self.instructions:
            instruction.render(self)

        interface_code = self.interface.__code__

        return types.CodeType(
            interface_code.co_argcount,                # argcount
            0,                                         # positiononly argcount
            interface_code.co_kwonlyargcount,          # kwonlyargcount
            (
                len(self.context.varnames) +
                len(self.context.names))
            ,                                          # nlocals
            self.bytecode.stacksize,                   # stacksize
            code_flags,                                # flags
            bytes(self.bytecode.bytes),                # codestring
            tuple(self.context.constants),             # constants
            tuple(self.context.names),                 # names
            tuple(self.context.varnames),              # varnames
            "<string>",                                # filename
            "<code of %s>" % self.interface.__name__,  # name
            0,                                         # firstlineno
            bytes(),                                   # lnotab
            tuple(),                                   # freevars
            tuple(),                                   # cellvars
        )
