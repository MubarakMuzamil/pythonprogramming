#finding the sum of the first"n" whole numbers using for loop
endpoint = int(input("enter the value of n:"))
sum_of_numbers = 0
for i in range(endpoint):
   print("sum of numbers value is :",sum_of_numbers)
   print("index i value is :",i)
   sum_of_numbers  = sum_of_numbers + i
print("the sum of first {} whole number is {}".format(endpoint,sum_of_numbers))