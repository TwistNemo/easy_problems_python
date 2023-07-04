# *
# ***
# *****
# *******
# *********
# here input n = 9
def pyramid_pattern(star):
    for i in range(1, star+1, 2):
        print('*'*i)
        
n = int(input())
pyramid_pattern(n)


#     *
#    ***
#   *****
#  *******
# *********


