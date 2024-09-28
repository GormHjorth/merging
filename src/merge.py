"""Code for merging two sorted lists."""


def merge(x:list[int], y:list[int]) -> list[int]:
    x = sorted(x)  #Sorting both lists prior to running
    y = sorted(y)
    z = []
    
    if not x:
        return y
    if not y:
        return x
    i = 0
    j = 0

    while i < len(x) or j < len(y):   #Keeps going until both lists have reached the last value
        if x[i] < y[j]:  # If the value of the placement in the x-list is smaller than the current placement in the y-list, then we append the current x-list value
            z.append(x[i]) 
            i += 1    #And count up 1 for the x-list related value, i, so we now check the next value
        elif x[i] >= y[j]:  #If the value of x[i] is bigger (or equal to) y[j], then we append y[j]
            z.append(y[j])
            j += 1  #And count up 1 for the y-list related value
    
    if i >= len(x):
        z.append(y[j:len(y)])
    elif j >= len(y):
        z.append(x[i:len(x)])
        
        
    return(z)
