import opcode
import struct

import watch


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
