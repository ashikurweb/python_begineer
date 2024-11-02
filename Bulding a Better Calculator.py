_num1 = float(input("Enter Your First Number: "))
_op = input("Enter Your Any Operator: ")
_num2 = float(input("Enter Your Second Number: "))

if _op == '+':
    print("Summation is: " + str(_num1 + _num2))
elif _op == '-':
    print("Subtraction is: " + str(_num1 - _num2))
elif _op == '*':
    print("Multiplication is: " + str(_num1 * _num2))
elif _op == "/":
    print("Division is: " + str(_num1 / _num2))
elif _op == "%":
    print("Remainder is: " + str(_num1 % _num2))
else:
    print("Invalid Operator!")