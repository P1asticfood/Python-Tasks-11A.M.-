#WAP to demonstrate the difference between is and ==

num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
num3=num2

print(num1 == num2)
print(num1 is num2)
print(num3 is num2)
print(id(num1))
print(id(num2))
print(id(num3))