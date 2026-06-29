'''
# Snippet from Flask

@route ('api/products')
def get_products:
    # code to list from database
    pass
'''
# Creating a decorator
def logger(func):
    def wrapper():
        print("Logging execution")
        func()
        print("Done logging")
    return wrapper

@logger
def sample():
    print("-- Inside sample function")