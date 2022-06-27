'''
------MEMOIZATION -----

    MEMOIZATION IS A TECHNIQUE USED TO MAKE PROGRAMMING SOLUTIONS 
    MORE EFFECTIVE , FAST AND EFFICIENT BY STORING RESULT OF
    EACH CALL IN A DATA STRUCTURE  CALLED MEMOIZING

Q Say that you are a traveler on a 2D grid . you begin in the top
left corner and your goal is to travel to bottom right
corner . you may only move down or right .

in how many ways can you travel to the goal on a grid with 
dimension c * r
'''

def gridTraveler(c,r):
    if c==0 or r ==0: return 0
    if c==1 or r==1:return 1
    return gridTraveler(c-1,r) + gridTraveler(c,r-1)

print(gridTraveler(1,3))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
