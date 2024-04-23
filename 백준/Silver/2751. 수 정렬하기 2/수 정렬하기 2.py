import sys
n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))


num_list.sort()

#print(num_list)  리스트 형태로 출력됨

for i in num_list:
    print(i)