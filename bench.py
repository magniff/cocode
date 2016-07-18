import timeit
from functools import reduce
from operator import mul
from cocode import *


def factorial_asm(value):
    pass


factorial_asm_proxy = CodeObjectProxy(
    VariableFast("value"),
    Dup(),
    Label(Constant(1), "loop"),
    Sub(),
    Dup(),
    Rot3(),
    Mult(),
    Rot2(),
    Dup(),
    Constant(1),
    Compare("=="),
    JumpFalse("loop"),
    Pop(),
    Return(),
    interface=factorial_asm,
)

fac_asm_code = factorial_asm_proxy.assemble()
factorial_asm.__code__ = fac_asm_code


assert factorial_asm(10) == 3628800, "ASM code works, but the result is wrong."


def factorial_recursive(value):
    return 1 if value == 1 else factorial_recursive(value - 1) * value


def factorial_forloop(value):
    result = 1
    for i in range(1, value + 1):
        result *= i
    return result


def factorial_whileloop(value):
    result = 1
    while value > 1:
        result *= value
        value -= 1
    return result


factorial_reduce = lambda value: reduce(mul, range(1, value + 1), 1)


print("Benching factorial asm...")
print(timeit.timeit(lambda: factorial_asm(900), number=10000))


print("Benching factorial recursive...")
print(timeit.timeit(lambda: factorial_recursive(900), number=10000))


print("Benching factorial for loop...")
print(timeit.timeit(lambda: factorial_forloop(900), number=10000))


print("Benching factorial while loop...")
print(timeit.timeit(lambda: factorial_whileloop(900), number=10000))


print("Benching factorial reduce...")
print(timeit.timeit(lambda: factorial_reduce(900), number=10000))
