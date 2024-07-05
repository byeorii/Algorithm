# https://velog.io/@seulki971227/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.1-%EC%B2%B4%EC%9C%A1%EB%B3%B5-Python

# 도난 당한 학생이 체육복 가져올 수 있으나, 남은게 하나이기에 체육복 빌려주지 못함


def solution(n, lost, reserve):
    answer = 0
    new_reserve = set(reserve) - set(lost)
    new_lost = set(lost) - set(reserve)
    #print(new_reserve, new_lost)
    
    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)
    answer = n - len(new_lost) # new_lost에는 체육복을 빌려받지 못해 수업 못듣는 학생
    
    
    return answer