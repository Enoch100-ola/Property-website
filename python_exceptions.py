# num1 = 5
# num2 = 0
# print(num1/num2)

try:
    num1=5
    num2 = 0
    print(num1/num2)
except ZeroDivisionError as message:
    print(f'U have {message}')