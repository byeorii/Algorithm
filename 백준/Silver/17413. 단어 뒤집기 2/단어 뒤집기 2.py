import sys

S = sys.stdin.readline().strip() + ' '
stack = []

result = ''

cnt = 0 # 괄호 있는지 체크

for i in S:
    if i == "<" :
        cnt = 1
        for _ in range(len(stack)): # 괄호 만나기 전 비워줌
            result += stack.pop()
    stack.append(i)

    if i ==">":
        cnt = 0 # 괄호 나왔음을 표현
        for _ in range(len(stack)):
            result += stack.pop(0) # pop(0) 첫번쨰 데이터 제거
    if i == ' ' and cnt == 0: # 공백 만나고 괄호 없다면
        stack.pop() # 공백 빼주고
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '
print(result)


