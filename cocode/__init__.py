from .instruction_base import BaseInstruction
from .nonargy import (
    Add, Sub, Mult, Negate, Nop, Pop, Return, Yield, Rot2, Rot3, Dup
)

from .argy import (
    Constant, Variable, Global, List, Bind, Jump, PopJumpFalse, PopJumpTrue,
    Label, Compare, VariableFast, BindFast, CallFunction
)
from .proxy import CodeObjectProxy
