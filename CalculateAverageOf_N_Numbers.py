n = int(input("Enter the count of numbers: "))
sum = 0

for i in range(n):
    num = float(input("Enter a number: "))
    sum += num

average = sum / n

print("The average of the", n, "numbers is:", average)
