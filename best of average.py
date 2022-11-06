print("enter the 3 internal marks")
marks1=int(input("enter the marks of 1 internal:"))
marks2=int(input("enter the marks of 2 internal:"))
marks3=int(input("enter the marks of 3 internal:"))
if marks1 < marks2 and marks1 < marks3:
 print("average of best 2 marks: ",(marks2 + marks3)/2)
elif  marks2 < marks3 and marks2 < marks1:
 print("average of best 2 marks:",(marks1 + marks3)/2)
else:
 print("average of best 2 marks:",(marks1 + marks2)/2)