#WAP to print a pyramid pattern of stars

print("=====pyramid of stars=====")


for i in range(1,11):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


rows = 5  # You can change this number for a bigger pyramid

for i in range(1, rows + 1):
    # Print spaces
    print(' ' * (rows - i), end=' ')
    # Print stars
    print(' *' * (2 * i - 1))
