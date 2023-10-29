# the 100 doors problem

#The link is here: https://compucademy.net/100-doors-python-coding-challenge/

import numpy as np

#create 100 closed doors. closed = 0 and opened = 1
lol = [0] * 100

print("before:",lol)


#Since we need to iterate 100 times since we have to open/close between 1 and 100 doors 100 times
# first all then every second, then every third etc.

k = 1 # sets counter so we can iterate everything 100 times
while k <= 100:
    b = 1 #sets parameter so we can iterate over all doors
    for i in range(len(lol)): #a loop through every door
        if b % k == 0: # if every 1'st 2nd 3rd 4th and so on then open/close the door 
            if lol[i] == 0:
                lol[i] = 1
                b +=1
            elif lol[i] == 1:
                lol[i] = 0
                b +=1
        else: 
            b +=1
            continue
    k +=1 # increment counter by 1 so we can se if b % k == 0

list = [] #make a list


for i in range(len(lol)): #this is in order to see which positions the 1's/opened doors are at
    if lol[i] == 1:
        list.append(i+1)

print("index of 1's",list) 
print("after:",lol) #the finished list of opened/ closed doors 
