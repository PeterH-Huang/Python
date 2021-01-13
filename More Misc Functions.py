
# assignment 2 Part 2
# Huang, Peter Helin 

import math
##############################################
###Question 2.1
##############################################
def min_enclosing_rectangle(radius, x, y):
    '''(number,number,number)->(number,number)
    The user inputs a number representing a radius(radius) of a circle and two numbers representing the x- and y-coordinates of its center(x and y respectively).
    The function then returns either None(if side is negative) or the x- and y-coordinates of the bottom-left corner of the smallest axis-aligned rectangle containing
    the circle in the form of (x_coordinate,y_coordinate).
    Preconditions: radius must be non-negative'''
    if radius>=0:
        x_coordinate=x-radius
        y_coordinate=y-radius
        return (x_coordinate,y_coordinate)
    if radius<0:
        return None
##############################################
###Question 2.2
##############################################
def series_sum():
    '''(int)->int
    Function asks the user to input a value for n. The function returns the sum of the equation: 1000+1/2^2+1/3^2...+1/n^2. If n is negative, function returns None.
    Preconditions:n must be non negative'''
    n=int(input("Please enter a non-negative integer: "))
    sum_series=1000
    if not n <0:
        for i in range (1,n+1):
            one_over=i
            sum_series=sum_series+(1/one_over**2)
    return sum_series
##############################################
###Question 2.3
##############################################
def pell(n):
    '''(int)->int
    Function takes one integer parameter n, and returns the nth Pell number
    Preconditions: n must be non negative'''
    if not n<0:
        Pn=(((1+math.sqrt(2))**n)-((1-math.sqrt(2))**n))/(2*math.sqrt(2))
        return round(Pn)
##############################################
###Question 2.4
##############################################
def countMembers(s):
    '''(str)->int
    Funtion takes string s and counts how many extraordinary characters are in the string. Characters are considered extraordinary if the character is one of the following:
    the lower case letter between e and j (inclusive), the uppercase letters between F and X (inclusive), numerals between 2 and 6 (inclusive), and the exclamation point (!), comma (,)
    and backslash (\). It then returns an integer for the number of extraordinary characters.
    Preconditions: none'''
    number_count=0
    big_List=["e","f","g","h","i","j","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","2","3","4","5","6","!",",","\\"]
    for char in s:
        for word in big_List:
            if char== word:
                number_count=number_count+1
    return number_count
##############################################
###Question 2.5
##############################################
def casual_number(s):
    '''(str)->int
    Funtion takes string s and returns an integer representing s in numerical form. If string s looks like a number but with commas, the commas are removed. Multple '-' or multiple ','
    in sucession and letter/s, will cause the function to return None. 
    Preconditions: s must not contain multple '-' or multiple ',' in sucession and letter/s'''
    s=s.replace(",","")
    if (s.isdigit() == True) or (s[0] == "-") and (s[1:].isdigit() == True):
        return int(s)
    else:
        return None
##############################################
###Question 2.6
##############################################
def alienNumbers(s):
    '''(str)->int
    Funtion takes alien string s, and returns the integer value represented by s.
    Preconditions: No character other than T,y,!,a, N, and U are allowed in the string s '''
    occurences_T=0
    T=1024
    occurences_y=0
    y=598
    occurences_exclaimation=0
    exclaimation=121
    occurences_a=0
    a=42
    occurences_N=0
    N=6
    occurences_U=0
    U=1
    for char in s:
        if char=="T":
            occurences_T=occurences_T+1
        if char=="y":
            occurences_y=occurences_y+1
        if char=="!":
            occurences_exclaimation=occurences_exclaimation+1
        if char=="a":
            occurences_a=occurences_a+1
        if char=="N":
            occurences_N=occurences_N+1
        if char=="U":
            occurences_U=occurences_U+1
    return occurences_T*T+occurences_y*y+occurences_exclaimation*exclaimation+occurences_a*a+occurences_N*N+occurences_U*U
##############################################
###Question 2.7
##############################################
def alienNumbersAgain(s):
    '''(str)->int
    Funtion takes alien string s, and returns the integer value represented by s. Since the previous funtion alienNumbers(s) did not use any string methods, the function
    alienNumbersAgain(s) is identical.
    Preconditions: No character other than T,y,!,a, N, and U are allowed in the string s '''
    occurences_T=0
    T=1024
    occurences_y=0
    y=598
    occurences_exclaimation=0
    exclaimation=121
    occurences_a=0
    a=42
    occurences_N=0
    N=6
    occurences_U=0
    U=1
    for char in s:
        if char=="T":
            occurences_T=occurences_T+1
        if char=="y":
            occurences_y=occurences_y+1
        if char=="!":
            occurences_exclaimation=occurences_exclaimation+1
        if char=="a":
            occurences_a=occurences_a+1
        if char=="N":
            occurences_N=occurences_N+1
        if char=="U":
            occurences_U=occurences_U+1
    return occurences_T*T+occurences_y*y+occurences_exclaimation*exclaimation+occurences_a*a+occurences_N*N+occurences_U*U
##############################################
###Question 2.8
##############################################
def encrypt(s):
    '''(str)->str
    Function takes a string s, returns a string that is the encrypted version of s. Encryption process involes turing s backwards, then
    starting on both sides of the string, the characters are brought together.
    Preconditions: none'''
    backwards=s[::-1]
    encrypted=""

    for i in range((len(backwards))//2):
        encrypted=encrypted+backwards[i]+backwards[len(backwards)-1-i]

    if(len(backwards) % 2 == 1):
        encrypted=encrypted+backwards[(len(backwards)//2)]

    return encrypted
##############################################
###Question 2.9
##############################################
def oPify(s):
    '''(str)->str
    Function takes a single string s and returns a modified string. The string is modified in a way such that the letters o and p are inserted between every pair
    of consecutive characters in s. The letter o matches the case of the first character and the letter p matches the case second character. If at least one of
    the character in the pair is not a letter in the alphabet, it does not insert anything between that pair. Finally, if s has one or less characters, the function
    returns the same string as s.
    Preconditions: none'''
    lower_Case=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper_Case=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numlist=["1","2","3","4","5","6","7","8","9","0"]
    insertion=""

    if len(s)<=1:
        return s

    for i in range(len(s)-1):
        if s[i] in lower_Case and s[i+1] in lower_Case:
            insertion=insertion+s[i]+"op"
        elif s[i] in lower_Case and s[i+1] in upper_Case:
            insertion=insertion+s[i]+"oP"
        elif s[i] in upper_Case and s[i+1] in upper_Case:
            insertion=insertion+s[i]+"OP"
        elif s[i] in upper_Case and s[i+1] in lower_Case:
            insertion=insertion+s[i]+"Op"
        elif s[i] in upper_Case or s[i] in lower_Case and s[i+1] in numlist:
            insertion=insertion+s[i]
        elif s[i] in numlist:
                insertion=insertion+s[i]
        else:
            insertion=insertion+s[i]

    return insertion+s[len(s)-1]
##############################################
###Question 2.10
##############################################
def nonrepetitive(s):
    '''(str)-> boolean
    Function takes string s and returns True if s is nonrepetitive and False otherwise.A nonrepetitive word is a word that does not contain any subword twice in a row
    Precondition:none'''
    Va=""
    Vb=""
    if len(s)==0 or len(s)==1:
        return True
    for i in range(0,(len(s)-1)):
        if s[i]==s[i+1]:
            return False
    for p in range(0,len(s)):
        for m in range (1,((len(s)//2+p))):
            Va=s[p:m+1]
            Vb=s[m+1:]
            if Va in Vb:
                for x in range(0,len(Va)):
                    if Va[x]==Vb[x]:
                        return False
    return True
