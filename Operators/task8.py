#WAP to use logical operators to check if a number id between 10 and 100

num= int(input("Enter a number: "))
if num>10 and num<100:
    print(f"{num} is between 10 and 100")
else:
    print(f"{num} is not between 10 and 100")