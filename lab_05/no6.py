n = int(input("Enter the number of lines: "))

for i in range(n):
    for j in range(i + 1, 0,-1):
        print(pow(2, j - 1), end=" ")
    print()