def fun(name):
    return {f"hello,{name}"}
shiva=fun # no ()-we store the function itself,not its result
print(shiva("panila"))