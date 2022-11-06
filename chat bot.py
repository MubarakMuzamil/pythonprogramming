#desingning a simple chatbot using if else
print("hello,i am a chatbot")
print("how may i help you?\n")
print("hit 1 for software installation request")
print("hit 2 for software update")
print("hit 3 for software uninstall request")
print("hit 4 for software repair request" )
print("hit 5 for other request")

#accepting the user input
userinput =int(input("enter your choice:"))

#using if else to process the user input
if userinput==1:
    softwareneeded=input("please provide the software name")
elif userinput ==2:
     softwareupdate = input("please provide the software name to be updated")
elif userinput == 3:
    softwareuninstall = input("please provide the software name to be uninstalled")
elif userinput == 4:
   softwarerepair = input("please provide the software name to be repaired")
else:
    otherrequest=input("please provide the detail of your request")
print("thank you for using our service,our team will get back to you soon")