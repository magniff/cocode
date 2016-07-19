import struct

import watch
from ..instruction_base import BaseArgyInstruction


class CallFunction(BaseArgyInstruction):
    """
    arg parameter:
       type: tuple of list of len 2
       item0: func call arg count
       item1: func call kwarg count
    """
    arg = watch.CombineFrom(
        watch.ArrayOf(watch.builtins.InstanceOf(int)),
        watch.Pred(lambda value: len(value) == 2)
    )
    opname = "CALL_FUNCTION"

    def arg_to_number(self, code_proxy):
        packed, *_ = struct.unpack("<H", bytes(self.arg))
        return packed
