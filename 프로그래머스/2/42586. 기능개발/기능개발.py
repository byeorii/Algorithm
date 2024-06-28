import math
def solution(progresses, speeds):
    
    # 남은 일수를 구해서 비교한 다음에 쌓아버리기?
    
    a = []
    answer = []
    
    for i in range(len(progresses)):
        b = math.ceil((100 - progresses[i]) / speeds[i])
        
        a.append(b)
        
    print(a)
    index = 0
    for j in range(len(a)):
        if a[index] < a[j]:
            answer.append(j-index)
            index = j
    answer.append(len(a) - index)
    return answer


# import math

# def solution(progresses, speeds):
#     answer = []

#     # 작업완료까지 걸리는 작업일을 먼저 전부 계산해서 리스트에 담아둔다.
#     days = [math.ceil((100-p) / s) for p, s in zip(progresses, speeds)]

#     index = 0 # 현재인덱스
    
#     print(days)

#     for i in range(len(days)) :
#         if days[index] < days[i] :      # 현재 인덱스의 작업일보다 큰 작업일이 나오면
#             answer.append(i - index)    # 둘의 차이(배포 개수)를 추가 
#             index = i                   # 현재 인덱스를 갱신
            
#     answer.append(len(days) - index)    # 갱신된 인덱스부터 마지막 인덱스까지의 개수

#     return answer
            
    