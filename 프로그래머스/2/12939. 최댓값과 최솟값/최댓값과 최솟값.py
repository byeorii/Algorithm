def solution(s):
    arr = list(map(int,s.split(' '))) # 공백 기준으로 split
    
    arr.sort() # 정렬값 리턴 안되고, 원본이 변경
    sorted(arr) #이거 사영하려면 정렬하고 새 리스트 만들어서 그 값에 넣어줘야함. 즉 원본이 안바뀜
    #arr = (sorted(arr)) # 이런식으로 써야함
    return str(arr[0]) + " " + str(arr[-1])