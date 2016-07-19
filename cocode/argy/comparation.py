import opcode
import watch
from ..instruction_base import BaseArgyInstruction


class Compare(BaseArgyInstruction):
    """NOTE: Pops from stack both of args.
    """

    opname = "COMPARE_OP"
    arg = watch.Pred(lambda arg: arg in opcode.cmp_op)

    def arg_to_number(self, code_proxy):
        return opcode.cmp_op.index(self.arg)
