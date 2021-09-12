import struct

import watch
from ..instruction_base import BaseTwoByteInstruction


class CallFunction(BaseTwoByteInstruction):
    arg = watch.builtins.InstanceOf(int)
    opname = "CALL_FUNCTION"

    def arg_to_number(self, code_proxy):
        return self.arg
