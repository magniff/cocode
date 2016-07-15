from carbon import CodeObjectProxy, Const, Name, Ret, Push, Add

cp = CodeObjectProxy(
    Push(Const("This ")),
    Push(Const("seams to be ")),
    Push(Const("working")),
    Add(),
    Add(),
    Ret()
)

code = cp.assemble()
print(eval(code))
