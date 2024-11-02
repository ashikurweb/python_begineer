_num1 = int(input("Enter Your First Number: "))
_num2 = int(input("Enter Your Second Number: "))
_num3 = int(input("Enter Your Third Number: "))

if _num1 <= _num2 and _num1 <= _num3:
    print("_num1 is: " + str(_num1))
elif _num2 <= _num1 and _num2 <= _num3:
    print("_num2 is: " + str(_num2))
else:
    print("_num3 is: " + str(_num3))