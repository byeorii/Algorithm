# def solution(numbers):
    
#     numbers = sorted(numbers, key = lambda x : str(x)*3, reverse = True)
        
            
#     answer = ''.join(map(str,numbers))
    
#     return answer if int(answer) != 0 else '0'


import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer