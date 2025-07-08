#WAP to print the first 10 Fibonacci numbers using a while loop
a, b = 0 , 1

count = 0
print("The first 10 fibinacci numbers are: ")
while count<10:
    print(a, end="\t")
    a ,b = b , a+b
    count += 1