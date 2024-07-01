import sys

count = int(sys.stdin.readline())

a = []

for _ in range(count):
    num = int(sys.stdin.readline())
    if a and num == 0:  # a 값이 존재하고, 입력받은게 0ㅇ이면 pop
        a.pop()
    else:
        a.append(num)

print(sum(a))