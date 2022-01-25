import random
# Peter Huang    
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    print("Shuffling the deck...\n\n\n")
    random.shuffle(deck)
    wait_for_player()
    return deck

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    if p1 !=p2 or discovered[p1-1] == "*" or discovered[p2-1] =="*":
        discovered[p1-1]=original_board[p1-1]
        discovered[p2-1]=original_board[p2-1]
    print(discovered)
    if discovered[p1-1] != discovered[p2-1]:
        discovered[p1-1]="*"
        discovered[p2-1]="*"
    return discovered
    wait_for_player()

#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=l
    while "*" in l:
        l.remove("*")
    for word in l:
        if l.count(word)%2>0:
            l.remove(word)
    return playable_board


def is_rigorous(l):
    '''list of str->bool
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''
    count_Element=0
    if l==[]:
        return True
    for word in l:
        if l.count(word)==2:
            count_Element=count_Element+1
    if count_Element==len(l):
        return True
    else:
        return False              
        

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")
    discovered=[]
    guess=0
    shuffle_deck(board)
    discovered=["*"]*len(board)
    print_board(discovered)
    print()
    if len(board)==0:
        print("The resulting board is empty.\nPlaying Concentration game is impossible.\nGoodbye!")
    while "*" in discovered:
        print("Enter two distinct positions on the board you want revealed \ni.e two integers in the range "+str([1,len(board)]))
        p1=int(input("Enter first position "))
        p2=int(input("Enter second position "))
        if discovered[p1-1] != "*" or discovered[p2-1] !="*" and not p1==p2:
            print("One or both of your chosen positions has already been paired.\nPlease try again. This guess did not count. Your current number of guesses is "+str(guess))
        elif p1 == p2:
            print("You chose the same positions.\nPlease try again. This guess did not count. Your current number of guesses is "+str(guess))
        else:
            guess=guess+1
            print_revealed(discovered,p1,p2,board)
        print()
        print_board(discovered)
        print()
        
    print("Congratulations! You completed the the game with "+str(guess)+" guesses. That is "+str(guess-(len(board)//2))+" more than the best possible")
    # this is the funciton that plays the game
   




#main
    
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE

# YOUR CODE FOR OPTION 1 GOES HERE
print("*"*40)
print("*"+" "*38+"*")
print("* __Welcome to my Concentration game__ *")
print("*"+" "*38+"*")
print("*"*40)

choice=int(input("Would you like (enter 1 or 2 to indicate your choice): \n(1)me to generate a rigorous deck of cards for you \n(2)or, would you like me to read a deck from a file? \n"))
while choice <1 or choice>2:
    choice=int(input(str(choice)+" is not an existing option. Please try again. Enter 1 or 2 to indicate your choice\n"))
if choice ==1:
    size=-1
    print("You chose to have a rigorous deck of cards for you\n")
    while size%2!=0 or size<0 or size>53:
        size=int(input("How many cards do you want to play with? \nEnter an even number between 0 and 52: "))
    board=create_board(size)
    play_game(board)
        

# In option 1 somewhere you need to and MUST have a call like this:
# board=create_board(size)

# YOUR CODE FOR OPTION 2 GOES HERE
if choice ==2:
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")
    board=read_raw_board(file)
    board=clean_up_board(board)
    rig=" "
    if is_rigorous(board)==True:
        rig=" and is rigorous "
    elif is_rigorous(board)==False:
        rig=" but not rigorous "
    print("*"*29+"*"*(len(rig))+"*"*11+"*"*len(str(len(board)))+"*"*11)
    print("*"+" "*28+" "*(len(rig))+" "*11+" "*len(str(len(board)))+" "*10+"*")
    print("* __This deck is now playable"+rig+"and it has "+str(len(board))+" cards.__ *")
    print("*"+" "*28+" "*(len(rig))+" "*11+" "*len(str(len(board)))+" "*10+"*")
    print("*"*29+"*"*(len(rig))+"*"*11+"*"*len(str(len(board)))+"*"*11)
    play_game(board)


# In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
#
#print("You chose to load a deck of cards from a file")
#file=input("Enter the name of the file: ")
#file=file.strip()
#board=read_raw_board(file)
#board=clean_up_board(board)

