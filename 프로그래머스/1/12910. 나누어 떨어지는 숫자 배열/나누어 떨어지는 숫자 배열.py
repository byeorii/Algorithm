# def solution(arr, d):
#     answer = []
#     for i in range(len(arr)):
#         if arr[i] % d == 0:
#             answer.append(arr[i])
#     if answer == []:
#         return [-1]
#     answer.sort()
#     return answer



# def solution (arr,d):
#     answer = []
#     for i in arr:
#         if i % d == 0:
#             answer.append(i)
            
#     if answer == []: 
#         return [-1]
#     return sorted(answer)
        

# def solution (arr, div):
#     arr = [x for x in arr if x % div ==0]  # 나누어떨어지는 애들만 모으기
#     arr.sort()
#     return arr if len(arr) !=0 else [-1]


#위에거를 한줄로 한다면

def solution(arr,div):
    return sorted([x for x in arr if x % div == 0]) or [-1]


    
    
    






