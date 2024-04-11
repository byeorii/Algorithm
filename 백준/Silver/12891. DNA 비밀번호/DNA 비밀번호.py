s, p = map(int, input().split())

string = input().rstrip()

a,c,g,t = map(int,input().split())

result = 0
start = string[:p]  # 처음부터 p번 앞까지
tmp = {"A":0, "C":0, "G":0, "T":0}

for i in start :
    tmp[i] += 1
cnt = 0

if  tmp["A"] >= a and tmp["C"] >= c and tmp["G"] >= g and tmp["T"] >= t:
    cnt += 1

start_idx = 0 # 비번 시작
end_idx = start_idx + p # 비번 끝

for i in range(len(string) -p): # 비밀번호 수 유지하기 위해
    tmp[string[start_idx +i]] -= 1
    tmp[string[end_idx+i]] += 1
    if tmp["A"] >= a and tmp["C"] >= c and tmp["G"] >= g and tmp["T"] >= t:
        cnt += 1

print(cnt)

