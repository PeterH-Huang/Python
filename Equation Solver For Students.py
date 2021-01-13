
# assignment 2 Part 1 
# Huang, Peter Helin 


import math
import random


def primary_school_quiz(flag, n):
    # Your code for primary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    ''' (int,int)->(int)
    The function, primary_school_quiz helps user either practice subtraction(if flag is 0) or exponentiation( if flag is 1). The function generates n math problems that the user must
    answer and checks if the answer is correct.The questions are generated with two random positive, single-digit numbers. Afterwards, the function returns the number of correct answers
    the user inputted
    Preconditions: flag must be 0 or 1, n must be a positive integer greater than 0 '''
    first_digit=0
    second_digit=0
    check=0
    correct_answers=0
    if flag==0:
        for i in range(1,n+1):
            print("Question",i)
            first_digit=random.randint(1, 9)
            second_digit=random.randint(1, 9)
            check=(second_digit-first_digit)
            user_answer=int(input("What is the result of {0} - {1}? ".format(second_digit,first_digit)))
            if user_answer==check:
                correct_answers=correct_answers+1
    if flag==1:
        for i in range(1,n+1):
            print("Question",i)
            first_digit=random.randint(1, 9)
            second_digit=random.randint(1, 9)
            check=(first_digit**second_digit)
            user_answer=int(input("What is the result of {0} ^ {1}? ".format(first_digit,second_digit)))
            if user_answer==check:
                correct_answers=correct_answers+1
    return correct_answers
    
            


    


def high_school_eqsolver(a,b,c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    '''(number,number,number)->none
    User inputs numbers for the a,b,c parameters that represents the a,b and c values of the quadratic equation. The function then solves for the roots of the equation
    and returns the solution.
    Preconditions: none'''
    discriminant=(b**2)-(4*a*c)
    solution1=0
    solution2=0
    if a==0 and b==0 and c==0:
        print("The quadratic equation 0x+0=0\nis satisfied for all numbers x")
    elif a==0 and b==0:
        print("The quadratic equation 0·x + " + str(c)+"=0\nis satisfied for no number x")
    elif a==0:
        solution1=(0-c)/b
        print("The linear equation "+str(b)+"x + "+str(c)+"=0\nhas the following root/solution:\n"+str(solution1))
    elif discriminant>0:
        solution1=(-b+math.sqrt(discriminant))/(2*a)
        solution2=(-b-math.sqrt(discriminant))/(2*a)
        print("The quadratic equation "+str(a)+"x^2+"+str(b)+"x+"+str(c)+"=0\nhas the following real roots:\n" +str(solution1)+" and "+str(solution2))
    elif discriminant<0:
        solution1=(-b/(2*a))
        solution2=(-b/(2*a))
        discriminant=(math.sqrt(abs(discriminant))/(2*a))
        print("The quadratic equation "+str(a)+"x^2+"+str(b)+"x+"+str(c)+"=0\nhas the following two complex roots:\n" +str(solution1)+" +i "+str(discriminant)+" \nand\n"+str(solution2)+" -i "+str(discriminant))
    elif discriminant==0:
        solution1=(-b/(2*a))
        print("The quadratic equation "+str(a)+"x^2+"+str(b)+"x+"+str(c)+"=0\nhas only one solution, a real root:\n" +str(solution1))
    






# main

# your code for the welcome tmessage goes here
print(60*"*")
print("*"+58*" "+"*")
print("* __Welcome to my math quiz-generator / equation-solver__  *")
print("*"+58*" "+"*")
print(60*"*")
name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    # your code goes here
    print(4*"*"+len(name)*"*"+64*"*")
    print("*"+(len(name)+66)*" "+"*")
    print("*  __"+name+", welcome to my quiz-generator for primary school students.__ *")
    print("*"+(len(name)+66)*" "+"*")
    print(4*"*"+len(name)*"*"+64*"*"+"\n")
    flag=int(input(name+" what would you like to practice? Enter\n0 for subtraction\n1 for exponentiation\n"))
    n=int(input("How many practice questions would you like to do?"))
    print(name+", here is your "+str(n)+" questions:")
    grade=primary_school_quiz(flag, n)
    if grade/n>=.9:
        print("Congratulations "+name+"! You’ll probably get an A tomorrow. Now go eat your dinner and go to sleep.")
    elif grade/n<.9 and grade/n>=.7:
        print("You did well "+name+", but I know you can do better.")
    elif grade/n<.7:
        print("I think you need some more practice "+name+".")

elif status=='2':

    # your code for welcome message
    print(55*"*"+len(name)*"*"+4*"*")
    print("*"+(57+len(name))*" "+"*")
    print("* __quadratic equation, a·x^2 + b·x + c= 0, solver for "+name+"__ *")
    print("*"+(57+len(name))*" "+"*")
    print(55*"*"+len(name)*"*"+4*"*")
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ").strip().lower()

        # your code to handle varous form of "yes" goes here
        if question!="yes":
            flag=False

        else:
            print("Good choice!")
            a=int(input("Enter a number for the coefficient a:"))
            b=int(input("Enter a number for the coefficient b:"))
            c=int(input("Enter a number for the coefficient c:"))
            high_school_eqsolver(a,b,c)
 
else:
    print(name+" you are not a target audience for this software.")
    pass

print("Good bye "+name+"!")
