#python program to perform simple arhmatic calculation
# to perform simple simple arthmatic equations
num1=int(input("enter the first number :"))
num2=int(input("enter the second  number  :"))
print("enter which of the operation do u want to perfrom?:")
ch=input("use any of these operators'+','-','*','/':")
result = 0
if ch == '+':
    result= num1+num2
elif ch == '-':
    result = num1-num2
elif ch == '*':
    result = num1*num2
elif ch == '/':
    result = num1/num2
else:
    print("input charecter is not recoginzed:")
print(num1,ch,num2,':',result)