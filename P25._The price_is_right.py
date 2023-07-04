# https://codeforces.com/group/yg7WhsFsAp/contest/355494/problem/P25

# using loop 
def find_index(seq):
    n = len(seq)
    min_value = float('inf')  # Initialize with a large value
    min_index = -1  # Initialize with an invalid index
    for i in range(n):
        if seq[i] < min_value:
            min_value = seq[i]
            min_index = i
    print(min_index)

n = int(input())
my_list = list(map(int, input().split()))
find_index(my_list)


# using max function 
def find_index(seq):
    n = len(seq)
    min_value = min(seq)
    min_index = seq.index(min_value)
    print(min_index)
n = int(input())
my_list = list(map(int, input().split()))
find_index(my_list)