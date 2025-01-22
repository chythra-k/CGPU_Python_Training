a, b = 0, 1
number= int(input("Enter the number "))
for _ in range(number):
    print(a,end=" ")
    a, b = b, a + b