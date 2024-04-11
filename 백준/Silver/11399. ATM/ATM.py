# 기다리는 시간을 sort로 정렬하여 구간합 구하기


n = input()

array = list(map(int,input().split()))

array.sort()

tmp = 0
sum = 0

for i in array:
    tmp += i
    sum += tmp

print(sum)