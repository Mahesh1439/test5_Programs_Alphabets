'''
*               * 
* *             *
*   *           *
*     *         *
*       *       *
*         *     *
*           *   *
*             * *
*               *
'''
for r in range(9):
    for c in range(9):
        if c==0 or (r==c )  or c==8:
            
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()