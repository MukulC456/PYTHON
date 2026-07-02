def add(num1, num2, num3, *args, **kwargs):
    print("num1: ",num1)
    print("num2: ",num2)
    print("num3: ",num3)
    print("*args: ",args)
    print("**kwargs: ",kwargs)

add(5,10,15,100,200,300,400,456,name="Mukul")

# args gives tuples and kwargs gives dictionary
# first 3 values will go to num1,num2,num3
# rest of thee values will go to args
# key value pair values will go kwargs
# we use * with args and ** with kwargs for parameters in func.