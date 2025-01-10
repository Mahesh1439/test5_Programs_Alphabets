'''
*       * 
  *   *
    *
    *
    *
'''
for r in range(5):
    for c in range(5):
        if (c==2 and r>2) or (r==c or r+c==4) and r<3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()