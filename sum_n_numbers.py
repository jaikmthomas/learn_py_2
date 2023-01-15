#Write a program that inputs a number n and prints the sum of all of the numbers from 1 to n:
n = int(input("enter a number:"))
add_num = 0
if n != 0:
    for i in range(0,n+1):
        add_num += i
    print("sum = " + str(add_num))
else:
    print("sum = 0")

#another easy method
n = int(input("Input a value for n: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print(sum)