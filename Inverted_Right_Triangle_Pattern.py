# *****
# ****
# ***
# **
# *

def reverse_triangle(star):
    for i in range(star,0,-1):
        print('*'* i)
n = int(input())
reverse_triangle(n)