'''
*                       * 
  *                   *
    *       *       *
      *   *   *   *
        *       *
'''
for r in range(5):
    for c in range(13):
        if r==c or (c+r==8 and r>1) or (c-r==4 and r>2) or r+c==12:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
