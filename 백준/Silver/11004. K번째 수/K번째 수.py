import sys
n,m = map(int,sys.stdin.readline().split(' '))

num_list = list(map(int,sys.stdin.readline().split(' ')))
num_list.sort()

print(num_list[int(m-1)])
