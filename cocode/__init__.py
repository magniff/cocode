from .instruction_base import BaseInstruction
from .nonargy import (
    Add, Sub, Mult, Negate, Nop, Pop, Return, Yield, Rot2, Rot3
)

from .argy import (
    Constant, Variable, List, Bind, Jump, JumpFalse, JumpTrue, Label, Compare,
    VariableFast, BindFast
)
from .proxy import CodeObjectProxy
