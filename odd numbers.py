start_point = int(input ('enter the values of start_point:'))
endpoint = int(input('enter the value of endpoint: '))
sum_of_odd_numbers = 0
for i in range(start_point , endpoint+1,2):
  print('sum of the odd numbers value is: ',sum_of_odd_numbers)
  print('index 1 value is: ',i)
sum_of_odd_numbers = sum_of_odd_numbers + i
print (sum_of_odd_numbers)