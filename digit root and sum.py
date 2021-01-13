
# assignment 5 part 3 
# Huang, Peter Helin 

def digit_sum(n):
    '''(number)->number'''
    if n==0:
        return 0
    else:
        return (n%10) + digit_sum(n//10)

def digital_root(n):
    '''(number)->number'''
    if len(str(n))==1:
        return n
    else:
        return digital_root(digit_sum(n))

        
