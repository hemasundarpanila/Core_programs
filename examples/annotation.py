def greet(name:str,age=int)->int:
    """just experimenting with functions"""
    print(f"hello,{name}")
    print(f"age:{age}")
    print(greet.__class__)
    print(greet.__name__)
    print(greet.__doc__)
    print(greet.__class__.__name__)
    print(greet.__closure__)
greet("shiva",21)

