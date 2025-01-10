'''
*               * 
* *           * *
*   *       *   *
*     *   *     *
*       *       *
*               *
*               *
*               *
*               *
'''
for r in range(9):
    for c in range(9):
        if c==0 or (r==c and r<5) or (r+c==8 and r<4 ) or c==8:
            
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()