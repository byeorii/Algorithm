import sys
input = sys.stdin.readline # 여러줄 입력받아야될때 사용

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0]
tmp = 0

# 누적 합 구하기
# 합 배열을 미리 구해놔서 시간 복잡도 고려할것
for i in arr:
    tmp +=i
    sum.append(tmp)

# 구간합 구하기
for _ in range(m):
    i,j = map(int,input().split())
    print(sum[j]-sum[i-1])
