import opcode
import struct

import watch


class BaseInstruction(watch.WatchMe):
    opname = None

    def render(self, code_proxy):
        """
        Mutates state of CodeProxys
        """
        code_proxy.bytecode.add(opcode.opmap[self.opname])


class BaseArgyInstruction(BaseInstruction):
    opname = None
    arg = None

    @staticmethod
    def pack_to_short(value):
        return struct.pack("<H", value)

    def __init__(self, arg):
        self.arg = arg

    def arg_to_number(self, code_proxy):
        raise NotImplementedError()

    def render(self, code_proxy):
        super().render(code_proxy)
        for value in self.pack_to_short(self.arg_to_number(code_proxy)):
            code_proxy.bytecode.add(value)
