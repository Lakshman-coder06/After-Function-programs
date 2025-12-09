try:
    b=int(input("Enter a number:"))
    print(b)
except ValueError:
    print("Write a integer value correctly")




try:
    c=400/1
except ZeroDivisionError:
    print("It wrong")








try:
    num=50/0
    a=chr(input("Enter your name:"))
    print(a)
except ZeroDivisionError:
    print("Dividing by zero is not correct")
except TypeError:
    print("type a name")
