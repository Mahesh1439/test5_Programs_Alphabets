'''
* * * * *   
*         *
*         *
*         *
* * * * *
*
*
*
*
'''
for r in range(9):
    for c in range(6):
        if c==0 or (r==0 and c!=5) or (r==4 and c!=5) or (r>0 and r<4 and c==5)  :
            
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()