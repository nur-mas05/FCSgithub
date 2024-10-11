list = [54, 76, 2, 4, 98, 100]
int1 = int(input("enter your first int:"))
int2 = int(input("enter your second int:"))
print("Values in the range:")
for i in list:
    if int1 <= i <= int2:
        print(i)