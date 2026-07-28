def html(tag,**attribute):
    s=""
    for key,value in attribute.items():
        s=s+(f"{key} = '{value}'")
    print(f"<{tag}  {s}>")
html("a",href="hdsjhgfhdjshghd",target="vheuh")