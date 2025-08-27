 #conditional statements 
#if , if-else , elif ladder , nested if 
# if statements 
# == , !=,  > , >= < , <=
#age = 17
#if age >= 18:
 #   print("You are eligible to vote ")
 # if else 
#age = int(input("Enter your age: "))
#if age >= 18:
 #   print("You are eligible to vote.")
#else:
#    print(" you are not eligible to vote.")

#marks = int(input("enter your marks : "))
#if marks >= 90:
#    print("Grade  A+")

#elif marks >= 70 :
#    print("Grade b ")
#else:
#    print("Fail")
age = 17
if age >= 18:
    if age >= 21:
        print("You can drive and vote")
    else:
        print("You can only vote")
else:
    print("Not eligible for anything")

