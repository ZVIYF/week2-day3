# תרגיל 1

def format_receipt(items):
    def line(name, price):
        return name.ljust(10) + str(price)
    
    lines = [line(n, a) for n, a in items]
    return "\n".join(lines)

print(format_receipt([("Milk", 6), ("Bread", 9)]))

# # # # #

# תרגיל 2

def make_greeter(message):
    def greet(name):
        return message + " " + name
    return greet

hello = make_greeter("Hello")
shalom = make_greeter("Shalom")
print(hello("Dana"))
print(shalom("Avi"))

# # # # #

# תרגיל 3

""""
def outer():
    message = "outer"
    
    def show():
        print("show:", message)
    
    def change():
        nonlocal message
        message = "changed"
    
    show() # ידפיס "outer"
    change() # ישנה ל- "changed"
    show() # ידפיס "changed"
outer()

"""