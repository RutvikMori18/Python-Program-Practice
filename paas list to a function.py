def even_odd(lst):
    even=0
    odd=0
    for i in lst:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd

list=(12,15,14,16,11,13,26,23,27,28,56,54,55,53)
even,odd=even_odd(list)
print("even",even)
print("odd",odd)

