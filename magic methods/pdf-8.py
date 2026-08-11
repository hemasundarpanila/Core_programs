class time_duration:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def total_minutes(self):
        return self.hours*60+self.minutes
    def __str__(self):
        return f"hours:{self.hours}\nminutes:{self.minutes}"
    def __add__(self,other):
        total=self.total_minutes()+other.total_minutes()
        return total
    def __sub__(self,other):
        minus=self.total_minutes()-other.total_minutes()
        return minus
a=time_duration(2,30)
b=time_duration(1,45)
print(a)
print(f"Total minutes for a: {a.total_minutes()}")
print("-"*13)
print(b)
print(f"Total minutes for b: {b.total_minutes()}")
print("-"*13)
print("addition:",a+b)
print("subtraction:",a-b)
