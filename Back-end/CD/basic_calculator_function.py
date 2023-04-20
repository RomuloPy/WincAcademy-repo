def basic_calculator(a,b,operation):

    a=float(a)
    b=float(b)
    if operation == "add":
      result = a + b
    elif operation == "subtract":
      result = a - b
    elif operation == "divide":
      result = a / b
    elif operation == "multiply":
      result = a * b
    else:
      result = "Operations supported: add, subtract, divide, multiple only"
        

    return result
