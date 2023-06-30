# https://codeforces.com/group/yg7WhsFsAp/contest/355490/problem/P06

math = input()
expression = math.split("+")
numbers = [int(num) for num in expression]
numbers.sort()
re_arr = "+".join(str(num) for num in numbers)
print(re_arr)