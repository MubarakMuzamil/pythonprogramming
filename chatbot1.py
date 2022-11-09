time=float(input("Enter the the military time\n"))
if(time<=12.00):
    print("Hello Good morning \n Welcome to Mubarak's chatbot")
    print("I would like to congratulate you on completing your C Programming successfully!")
    print("How may i help you")
elif(time<=18.00):
     print("Hello Good Afternoon \n Welcome to Mubarak's chatbot")
     print("I would like to congratulate you on completing your C Programming successfully!")
     print("How may i help you")
elif(time<24.00):
    print("Hello Good Night \n Welcome to Mubarak's chatbot")
    print("I would like to congratulate you on completing your C Programming successfully!")
    print("How may i help you")
else:
    print("wrong time")
print("choice")
print( " Case1 java")
print( " Case2 c++")
print( " Case3 python")
print( "Which course you want to do ?")
choice=int(input("enter the choice\n"))
if(choice==1):
    print("java")
    print("In which mode you want to do?")
    print("Case1 offline")
    print("Case2 online")
    choice=int(input("enter the choice\n"))
    if(choice==1):
        print("you can start offline from next day we will send you the venue and other details")
        print("Thank you")
    elif(choice==2):
        print("you can start online from tommorow we will send you the details on mail")
        print("Thank you")
    else:
        print("wrong choice")
elif(choice==2):
    print("c++")
    print("In which mode you want to do?")
    print("Case1 offline")
    print("Case2 online")
    choice=int(input("enter the choice\n"))
    if(choice==1):
        print("you can start offline from next day we will send you the venue and other details")
        print("Thank you")
    elif(choice==2):
        print("you can start online from tommorow  we will send you the  details on mail")
        print("Thank you")
    else:
        print("wrong choice")
elif(choice==3):
    print("python")
    print("In which mode you want to do?")
    print("Case1 offline")
    print("Case2 online")
    choice=int(input("enter the choice\n"))
    if(choice==1):
        print("you can start offline from next day we will send you the venue and other details")
        print("Thank you")
    elif(choice==2):
        print("you can start online from tommorow  we will send you the details on mail")
        print("Thank you")
    else:
        print("wrong choice")
else:
    print("wrong choice")

print("Thank you for using Mubarak's chatbot, Please keep patience")