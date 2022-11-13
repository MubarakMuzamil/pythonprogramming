print(" which one of the following operations you want to do ")
print("choices are")
print("1.factorial of number")
print("2.average of n numbers")
print("3.sum of n numbers")
print("4.even numbers in given range")
print("5.odd numbers in given range")
choice=int(input("enter the choice\n"))
if(choice==1):
#Factorial
    n = int(input("Enter a number\n"))
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print("Factorial of {} is {}".format(n, fact))

elif(choice==2):
    #Average of n numbers
    n1 = int(input("Enter value of n \n"))
    arr = []
    avg = 0
    for i in range(n1):
        arr.append(int(input("Enter elements\n ")))
    for i in arr:
        avg += i
    avg = avg/n1
    print("Average of given numbers is", avg)
elif(choice==3):
    #Sum of given numbers
    n2 = int(input("Enter value of n\n"))
    arr1 = []
    sum = 0
    for i in range(n2):
        arr1.append(int(input("Enter elements\n ")))
    for i in arr1:
        sum += i
    print("Sum of given numbers is", sum)

elif(choice==4):
    #Even numbers
    lower = int(input("Enter lower range"))
    upper = int(input("Enter upper range"))

    print("Even numbers")
    for i in range(lower, upper):
        if(i % 2 == 0):
            print(i)

elif(choice==5):
    #Odd numbers
    lower = int(input("Enter lower range"))
    upper = int(input("Enter upper range"))

    print("Odd numbers")
    for i in range(lower,upper):
        if(i % 2 !=0):
            print(i)
else:
    print("wrong choice")