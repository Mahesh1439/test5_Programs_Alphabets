'''
*
*
*
*
*
*
*
*
* * * * * *
'''
for r in range(9):
    for c in range(6):
        if c==0 or r==8:
            
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()