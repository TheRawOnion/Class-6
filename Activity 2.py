a = 10
b = 12
c = 12
print(not(a == b))
print(not(b == c))
a = "python"
b = "coding"
if not(a == b):
    print(a + " and " + b + " are not the same")
a = 4
b = 5
if not ((a == 1) == (b == 5)):
    print("Hello")
num = int(input("Enter a number: "))
if not num % 2 == 0:
    print(num, "is an odd number.")