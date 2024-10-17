# This is a concept of calculation in calculator

expression = ""

def append_to_expr(x):
    global expression
    expression += x

while True:
    x = str(input("number: "))
    
    if x == "=":
        break

    append_to_expr(x)
    print(type(x))
    print(expression)


print(expression)
print(eval(expression))
