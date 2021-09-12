import opcode
import struct

import watch


class BaseInstruction(watch.WatchMe):
    opname = None
    position = watch.builtins.InstanceOf(int)

    def __len__(self):
        'simple instruction takes only 1 byte'
        return 1

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def render(self, code_proxy):
        """ Mutates state of CodeProxys """
        code_proxy.bytecode.add(opcode.opmap[self.opname])


class BaseArgyInstruction(BaseInstruction):
    arg = None

    @staticmethod
    def pack_to_short(value):
        return struct.pack("@H", value)

    @staticmethod
    def pack_to_byte(value):
        return struct.pack("@B", value)

    def __init__(self, arg):
        self.arg = arg

    def arg_to_number(self, code_proxy):
        raise NotImplementedError(
            "How to convert arg -> int for opcode %s?" % self.opname
        )
