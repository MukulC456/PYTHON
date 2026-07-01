# positional args
#Specifiying values directly while calling func 

def total_marks(English, Maths, Science, History, Hindi):
    total = English+ Maths+ Science+ History+ Hindi
    return total

x = total_marks(English=80, Maths=85, Science=95, History=75, Hindi=80)
print(x)