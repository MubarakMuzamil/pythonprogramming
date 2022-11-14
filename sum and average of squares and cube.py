nums = []
sum = 0
avg = 0
sqrs = []
sumOfSqrs = 0
avgOfSqrs = 0
cube = []
sumOfCube=0
avgOfCube=0

for i in range(10):
    nums.append(int(input("Enter number\n")))
    sum += nums[i]
avg = sum/10

print("Sum of Numbers = ", sum)
print("Average = ", avg)

print("\nSquares are ")
for i in nums:
    sqrs.append(i**2)
    sumOfSqrs+= i**2
    print("Square of {} is {}".format(i,i**2))

avgOfSqrs = sumOfSqrs/10
print("Sum of Squares = ", sumOfSqrs)
print("Average of Squares = ", avgOfSqrs)

print("\nCubes are")
for i in nums:
    cube.append(i**3)
    sumOfCube += i**3
    print("Cube of {} is {}".format(i, i**3))

avgOfCube = sumOfCube/10
print("Sum of cubes = ", sumOfCube)
print("Average of cube = ", avgOfCube)