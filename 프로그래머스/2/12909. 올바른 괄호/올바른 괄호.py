



def solution (s):
    stack = []  # 이 스택에서 ()괄호가 쌍이 맞으면 (가 쌓이는 거임

    for c in s:
        if c == "(": # 스택에 괄호 추가
            stack.append(c)
        else:  # ) 로 시작
            if stack: # 스택 값이 짝을 이루면 스택에서 ( 제거 
                stack.pop()   
            else:
                return False   # 스택 값 없으면 
         # 마지막 결과    
    if stack : 
        return False
    
    return True

"""
접근방법

기본적으로 '( )' 라는 짝이 되어야 올바른 괄호이다.
스택에는 '(' 만 넣어두고 ')'이 들어올 때에만 삭제시킨다.
스택에 비어있는데 ')'가 들어온다면 올바른 짝이 될 수 없으므로 False를 반환한다.
for문을 다 돌았는데 stack 안에 '('가 남아있으면 올바른 짝이 아니므로 False를 반환한다.

"""
            
        
        
    
    