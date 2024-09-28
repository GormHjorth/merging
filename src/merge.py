"""Code for merging two sorted lists."""

def merge(x:list[int], y:list[int]) -> list[int]:
    x = sorted(x)  #Sorting both lists prior to running
    y = sorted(y)
    z = []

    i = 0
    j = 0

    while i < len(x) and j < len(y):   #Keeps going until both lists have reached the last value
    
        if x[i] < y[j]:  # If the value of the placement in the x-list is smaller than the current placement in the y-list, then we append the current x-list value
            z.append(x[i]) 
            i += 1    #And count up 1 for the x-list related value, i, so we now check the next value
        elif x[i] >= y[j]:  #If the value of x[i] is bigger (or equal to) y[j], then we append y[j]
            z.append(y[j])
            j += 1  #And count up 1 for the y-list related value

    if i >= len(x):     #check if it was the x list that reached its end first and if so, appends the rest of the y list (extend not append, if using append then it adds as a seperate list)
        z.extend(y[j:len(y)])
    elif j >= len(y):   #Same as with the x list, but now with the y list
        z.extend(x[i:len(x)])
    
    return(z)
