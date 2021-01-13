# assignment 5 part 1 
# Huang, Peter Helin 
# 300021511

def largest_34(a):
    '''(list)->number'''
    a=sorted(a, key=int, reverse=True)
    return a[2]+a[3]

def largest_third(a):
    '''(list)->number'''
    num=len(a)//3
    suma=0
    a=sorted(a, key=int, reverse=True)
    for i in range(num):
        suma=suma+a[i]
    return suma

def third_at_least(a):
    '''(list)->number'''
    num=len(a)//3+1
    occur=[]
    for i in a:
        if a.count(i)>=num and i not in occur:
            occur.append(i)
    if occur==[]:
        return None
    else:
        return min(occur)
    
def sum_tri(a,x):
    '''(list)->bool'''
    check=0
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if a[i]+a[j]+a[k]==x:
                    check=check+1
    if check>0:
        return True
    elif check<1:
        return False
                    
