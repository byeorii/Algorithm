def solution(words, n):
    words.sort()
    return sorted(words, key=lambda x:x[n])


# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.