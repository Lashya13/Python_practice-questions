array=[1,0,2,3,0,4,5,0]
i = 0
while(i< len(array)):
    if array[i] == 0:
        array.insert(i+1,0)
        array.pop()
        i=i+2
    else:
        i=i+1    
print(array)        