# For entering the data for students
score=0
name=input("Enter the Name\n")
USN=input("Enter the USN\n")
print("multiple choice Questions \n Instructions: Read the following question carefully and choose the correct option")
#Questionn 1
print("\n1.The Battle of Plassey was fought in ?")
# For print options and Entering the options
print("options are")
print("option1 1757")
print("option2 1782")
print("option3 1748")
print("option4 1764")
answer=int(input("enter the option\n"))
if(answer==1):
    print("answer is correct")
    score=score+1
    print("your score is",score)
else:
    print("answer is wrong")
    print("Your score is",score)


#Question 2
print("\n2.The territory of Porus who offered strong resistance to Alexander was situated between the rivers of")
# For print options and Entering the options
print("options are :")
print("option1 Sutlej and Beas")
print("option2 Jhelum and Chenab")
print("option3 Ravi and Chenab")
print("option4 Ganga and Yamuna")
answer=int(input("enter the option\n"))
if(answer==2):
    print("answer is correct")
    score=score+1
    print("your score is",score)
else:
    print("answer is wrong")
    print("your score is",score)

#Question 3
print("\n3.Under Akbar, the Mir Bakshi was required to look after")
# For print options and Entering the options
print("options are :")
print("option1 military affairs")
print("option2 the state treasury")
print("option3 the royal household")
print("option4 the land revenue system")
answer=int(input("enter the option\n"))
if(answer==1):
    print("answer is correct")
    score=score+1
    print(" your score is",score)
else:
    print("answer is wrong")
    print("your score is",score)

#Question 4
print("\n4.Tripitakas are sacred books of")
# For print options and Entering the options
print("options are :")
print("option1 Buddhists")
print("option2 Hindus")
print("option3 Jains")
print("option4 None of the above")
answer=int(input("enter the option\n"))
if(answer==1):
    print("answer is correct")
    score=score+1
    print(" your score is",score)
else:
    print("answer is wrong")
    print("your score is",score)

#Question 5
print("\n5.The trident-shaped symbol of Buddhism does not represent")
# For print options and Entering the options
print("options are :")
print("option1 Buddha")
print("option2 Sangha")
print("option3 Nirvana")
print("option4 Dhamma")
answer=int(input("enter the option\n"))
if(answer==3):
    print("answer is correct")
    score=score+1
    print("your score is",score)
else:
    print("answer is wrong")
    print("your score is",score)
print("Name is",name)
print("USN is",USN)
print("your final score is ",score)
print("thank you")