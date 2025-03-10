


# Input dimensions for both matrices
n1, n2 = map(int, input("Enter number of rows and columns (space-separated) for the matrices: ").split())

# Initialize the two matrices
arr1 = []
arr2 = []
for i in range(n1):
    row = list(map(int, input(f"Enter row {i+1} for matrix 1: ").split()))
    arr1.append(row)

for i in range(n1):
    row = list(map(int, input(f"Enter row {i+1} for matrix 2: ").split()))
    arr2.append(row)

# Initialize result matrix with zeroes
tot = []
for i in range(n1):
    row = []
    for j in range(n2):
        row.append(arr1[i][j] + arr2[i][j])
    tot.append(row)

# Print the result matrix
for row in tot:
    for element in row:
        print(element, end=" ")
    print()  # Move to the next line after each row
