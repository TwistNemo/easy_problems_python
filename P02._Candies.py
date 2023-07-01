# https://codeforces.com/group/yg7WhsFsAp/contest/355490/problem/P02

def solve():
    n = int(input())
    my_list = list(map(int, input(). split()))
    a,b= map(int, input(). split())
    total_sum = sum(my_list[a:b+1])
    print(total_sum)
    
    
solve()    