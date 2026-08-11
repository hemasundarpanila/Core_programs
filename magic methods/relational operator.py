class values:
    def __init__(self,value):
        self.value=value
    def __eq__(self,w1):
        return (self.value==w1.value)
a=values(20)
b=values(20)
print((a==b))