'''
*         * 
*       *
*     *
*   *
* *
*   *
*     *
*       *
*         *
'''
for r in range(9):
    for c in range(6):
        if c==0 or r+c==5 or c-r==6 or (r==c+3 and c>1) :
            
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()