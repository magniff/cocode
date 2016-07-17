from .instruction_base import BaseInstruction
from .nonargy import (
    Add, Mult, Negate, Nop, Pop, Return, Yield, Rot2, Rot3
)

from .argy import (
    Constant, Variable, List, Bind, Jump, JumpFalse, JumpTrue, Label, Compare
)
from .proxy import CodeObjectProxy
