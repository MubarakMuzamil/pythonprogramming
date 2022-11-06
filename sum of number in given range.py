#finding the sum of number between a given range(start point,endpoint)
start_point = int(input("enter the start point:"))
endpoint = int(input("enter the end point"))
sum_of_numbers = 0
for i in range(start_point,endpoint):
    sum_of_numbers = sum_of_numbers + i
print("the sum of numbers between{} and {} is {}".format(start_point,endpoint,sum_of_numbers))