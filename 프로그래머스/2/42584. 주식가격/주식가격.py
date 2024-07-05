# def solution (prices):
#     answer = []
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] > prices[j]:
#                 answer.append(j-i) 
#                 break
#         else:
#             answer.append(len(prices)-i-1)
#     return answer
                
from collections import deque

# deque 
# def solution(prices):
#     answer = []
#     price_q = deque(prices)
    
#     while price_q:
#         price = price_q.popleft()
#         time = 0
#         for q in price_q:
#             time += 1
#             if price > q:
#                 break
#         answer.append(time)
#     return answer

# stack

def solution (prices):
    length = len(prices)
    answer = [ i for i in range (length - 1, -1, -1)]
    stack = [0]
    for i in range (1, length):
        #print(i, stack)
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
            #print(i, j, stack)
        stack.append(i)
    return answer


            