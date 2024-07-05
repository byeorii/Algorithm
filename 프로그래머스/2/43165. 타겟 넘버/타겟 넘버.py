def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]  # 플러스 마이너스 인 경우 뽑아서
    n = len(numbers)
    

    while queue: # 큐 안에서 진행하는 동안
        temp, idx = queue.pop()
        idx+=1 # 다음꺼로 진행
        if idx < n: 
            queue.append([temp+numbers[idx],idx])
            queue.append([temp-numbers[idx],idx])
            #print(queue)
        else:
            if temp == target:
                answer += 1
    return answer
        
        
             
