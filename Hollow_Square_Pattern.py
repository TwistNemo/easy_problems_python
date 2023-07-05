# *****
# *   *
# *   *
# *   *
# *****

def hallow_patter(star):
    for i in range(0,star,1):
        if i == 0 or i == star-1:
            print('*'*star)
        else:
            print('*' + ' ' * (n-2) + '*')
            

n = int(input())
hallow_patter(n)




