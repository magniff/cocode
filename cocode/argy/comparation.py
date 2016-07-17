import dis
import watch

from cocode.instruction_base import BaseArgyInstruction


class Compare(BaseArgyInstruction):
    """NOTE: Pops from stack both of args.
    """

    opname = "COMPARE_OP"
    arg = watch.Pred(lambda arg: arg in dis.cmp_op)

    def arg_to_number(self, code_proxy):
        return dis.cmp_op.index(self.arg)
