'''
*             *
  *         *
    *     *
      * *
      * *
    *     *
  *         *
*             *
'''
# for r in range(8):
#     for c in range(13):
#         if r==c or r+c==7:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



'''
*       * 
  *   *
    *
  *   *
*       *
'''

for r in range(5):
    for c in range(5):
        if r==c or r+c==4:
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()