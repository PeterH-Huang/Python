>>># assignment 1 
>>># Huang, Peter 
import math
##################################################################################################################################################################################################################################################################
#Question 1
############################################################################################################################################################################################################################################################
def mh2kh(s):
    ''' (number)->(float)
    Precondition: none
    Converts the given speed,s, from miles/hour to kilometres/hour'''
    kmh=s*1.60934
    return kmh
##################################################################################################################################################################################################################################################################
#Question 2
############################################################################################################################################################################################################################################################
def pythagorean_pair(a,b):
    ''' (int,int)->(boolean)
    Precondition: none
    Takes the two integers a and b, and returns True if they are a pythagorean pair and False if not'''
    test=((a**2+b**2)**(1/2))%1==0
    return test
##################################################################################################################################################################################################################################################################
#Question 3
############################################################################################################################################################################################################################################################
def in_out(xs,ys,side):
    '''(number,number,number,)->(boolean)
    Precondition:side non-negative
    Takes the coordinates inputted by the user and determines if the point is on the boundary or
    inside the square established by the side legnth and the bottom left corner coordinates(xs,ys)'''
    x=float(input("Enter a number for the x coordinate of a query point: "))
    y=float(input("Enter a number for the y coordinate of a query point: "))
    square_check= x>=xs and x<=xs+side and y>=ys and y<=ys+side
    return square_check
##################################################################################################################################################################################################################################################################
#Question 4
############################################################################################################################################################################################
def safe(n):
    ''' (int,)->(boolean)
    Precondition: n non-negative and at most 2 digits
    Tests if a number is safe(divisble by 9 or contains 9 as a digit) and returns True if it is safe and False if it is not'''
    safety=n%9!=0 and n%10!=9 and n//10!=10
    return safety
##################################################################################################################################################################################################################################################################
#Question 5
############################################################################################################################################################################################
def quote_maker(quote, name, year):
    ''' (str,str,number)->(none)
    Precondition: none
    Takes a quote, name and year to create a full coherent sentence'''
    print ("'In "+str(year)+',a person called '+name+ ' said "'+quote+'"') 
##################################################################################################################################################################################################################################################################
#Question 6
############################################################################################################################################################################################
def quote_displayer():
    '''(none)->(none)
    Precondition: none
    Let's the user input a quote,name and year to create a sentence'''
    quote=input("Give me a quote: ")
    name= input("Who said that? ")
    year= input("What year did the person say that? ")
    quote_maker(quote, name, year)
##################################################################################################################################################################################################################################################################
#Question 7
############################################################################################################################################################################################
def rps_winner():
    '''(none)-> (str)
    Precondition: none
    Using the choices of the two players, whether or not player 1 wins or if it is a tie will be anouced as true or false'''
    print ("What choice did player 1 make? ")
    p1=input ("Type one of the following options: rock, paper, scissors: ")
    print ("What choice did player 2 make? ")
    p2=input ("Type one of the following options: rock, paper, scissors: ")
    player1_win_outcome=(p1=="rock" and p2=="scissors") or (p1=="paper" and p2=="rock") or (p1=="scissors" and p2=="paper")
    tie_checker=(p1=="rock" and p2=="rock") or (p1=="paper" and p2=="paper") or (p1=="scissors" and p2=="scissors")
    print("Did player 1 win? " + str(player1_win_outcome))
    print("Was it a tie? " + str(tie_checker))
##################################################################################################################################################################################################################################################################
#Question 8
############################################################################################################################################################################################   
def fun(x):
    '''(number)->(float)
    Precondition: x must be positive
    Takes the input x and solves for y in the equation 10**(4y)=x+3'''
    y_answer=(math.log(x+3))/(math.log(10)*4)
    return y_answer
##################################################################################################################################################################################################################################################################
#Question 9
############################################################################################################################################################################################
def ascii_name_plaque(name):
    '''(str)->(none)
    Precondition: none
    Using an inputted name to create an ascii plaque with the name in the centre'''
    leng=len(name)
    print("*****"+leng*"*"+"*****")
    print("*    "+leng*" "+"    *")
    print("*  __"+name+"__  *")
    print("*    "+leng*" "+"    *")
    print("*****"+leng*"*"+"*****")
##################################################################################################################################################################################################################################################################
#Question 10
############################################################################################################################################################################################
def draw_bike():
    '''(none)->(none)
    Precondition: none
    Calling this function automatically creates a colourful bike'''
    import turtle

    turtle.pensize(10)
    turtle.circle(50)
    turtle.pensize(17)
    turtle.pencolor('grey')
    turtle.penup()
    turtle.goto(0,40)
    turtle.pendown()
    turtle.circle(10)

    turtle.penup()
    turtle.goto(5,60)
    turtle.pendown()
    turtle.pencolor('blue')
    turtle.pensize(10)
    turtle.left(55)
    turtle.forward(100)
    turtle.right(55)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(40)

    turtle.penup()
    turtle.goto(240,40)
    turtle.pendown()
    turtle.pensize(17)
    turtle.pencolor('grey')
    turtle.circle(10)
    turtle.penup()
    turtle.goto(215,10)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.pensize(10)
    turtle.circle(50)

   
    turtle.penup()
    turtle.pensize(5)
    turtle.goto(55,30)
    turtle.pendown()
    turtle.circle(20)
    turtle.penup()
    turtle.pencolor('blue')
    turtle.goto(62.5,37.5)
    turtle.pendown()
    turtle.pencolor('grey')
    turtle.circle(10)

    turtle.pencolor('black')
    turtle.right(65)
    turtle.forward(25)
    turtle.left(25)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(30)

    turtle.penup()
    turtle.goto(74,65)
    turtle.pendown()
    turtle.left(65)
    turtle.forward(25)
    turtle.left(115)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(30)

    turtle.penup()
    turtle.pensize(10)
    turtle.pencolor('blue')
    turtle.goto(52.5,37.5)
    turtle.pendown()
    turtle.goto(10,50)
    turtle.penup()

    turtle.goto(74,65)
    turtle.left(95)
    turtle.pendown()
    turtle.forward(105)
    turtle.right(100)
    turtle.pencolor('brown')
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(30)
    turtle.penup()

    turtle.pencolor('blue')
    turtle.goto(74,65)
    turtle.right(151)
    turtle.pendown()
    turtle.forward(157.5)
    turtle.left(61)
    turtle.forward(30)
    turtle.right(105)
    turtle.pencolor('grey')
    turtle.forward(15)
    turtle.left(180)
    turtle.forward(30)

    
##################################################################################################################################################################################################################################################################
#Question 11
###########################################################################################################################################################################################
def alogical(n):
    '''(number)->(float)
    Precondition: n>=1
    Returns the minimal number of times that n is divided by two to get a number smaller than or equal to 1'''
    d2=(math.log(n))/(math.log(2))
    done=math.ceil(d2)
    return done

##################################################################################################################################################################################################################################################################
#Question 12
###########################################################################################################################################################################################
def time_format(h,m):
    ''' (int,int)->(none)
        Precondition:h<24, h>=0,m<60 and m>=0
        Converts the hours (h) and minutes(m) to a descriptive time string'''
    tenth_min=m//10*10
    rnd_min=m-tenth_min

    if(rnd_min>=0 and rnd_min<2.5):
        m=tenth_min+0

    elif(rnd_min>=2.5 and rnd_min<7.5):
        m=tenth_min+5

    elif(rnd_min>=7.5 and rnd_min<=10)and h<23 and m<55:
        m=tenth_min+10

    elif(rnd_min>=7.5 and rnd_min<=10)and h<23 and m>55:
        m=0
        h=h+1

    elif(rnd_min>=7.5 and rnd_min<=10)and h==23 and m>55:
        m=0
        h=0

    elif(rnd_min>=7.5 and rnd_min<=10)and h==23 and m<55:
        m=tenth_min+10
        
    if(m==0):
        print(str(h)+" o'clock")

    elif(m==5):
        print("5 minutes past "+str(h)+" o'clock")

    elif(m==10):
        print("10 minutes past "+str(h)+" o'clock")

    elif(m==15):
        print("15 minutes past "+str(h)+" o'clock")

    elif(m==20):
        print("20 minutes past "+str(h)+" o'clock")

    elif(m==25):
        print("25 minutes past "+str(h)+" o'clock")

    elif(m==30):
        print("Half past "+str(h)+" o'clock")

    elif(m==35)and (h<23):
        print("25 minutes to "+str(h+1)+" o'clock")

    elif(m==40)and (h<23):
        print("20 minutes to "+str(h+1)+" o'clock")

    elif(m==45)and (h<23):
        print("15 minutes to "+str(h+1)+" o'clock")

    elif(m==50)and (h<23):
        print("10 minutes to "+str(h+1)+" o'clock")

    elif(m==55)and (h<23):
        print("5 minutes to "+str(h+1)+" o'clock")

    elif(m==35)and (h==23):
        print("25 minutes to 0 o'clock")

    elif(m==40)and (h==23):
        print("20 minutes to 0 o'clock")

    elif(m==45)and (h==23):
        print("15 minutes to 0 o'clock")

    elif(m==50)and (h==23):
        print("10 minutes to 0 o'clock")

    elif(m==55)and (h==23):
        print("5 minutes to 0 o'clock")
##################################################################################################################################################################################################################################################################
#Question 13
###########################################################################################################################################################################################
def cad_cashier(price,payment):
    '''(number),(number)->(float)
    Precondition: price and payment must be non-negative and has at most 2 decimal places
    Takes two numbers representing price and payment, and returns the change that is due rounded to the nearest 5 cents'''
    difference=(payment-price)
    change=round(difference*20)/20
    return change       
##################################################################################################################################################################################################################################################################
#Question 14
###########################################################################################################################################################################################
def min_CAD_coins(price,payment):
    '''(number),(number)->(int,int,int,int,int)
    Precondition: price and payment must be non-negative and has at most 2 decimal places
    Takes two numbers representing price and payment, and returns the minimal amount of coints that matches the change due rounded to the nearest 5 cents'''
    cents=cad_cashier(price,payment)*100
    t=math.floor(cents/200)
    cents=cents-t*200
    l=math.floor(cents/100)
    cents=cents-l*100
    q=math.floor(cents/25)
    cents=cents-q*25
    d=math.floor(cents/10)
    cents=cents-d*10
    n=math.floor(cents/5)

    return t,l,q,d,n










