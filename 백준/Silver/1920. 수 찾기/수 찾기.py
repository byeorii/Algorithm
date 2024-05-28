import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for m in M_list:
    start= 0
    end = N-1


    while start <= end:
        mid = (start + end) // 2
        if m > N_list[mid]:
            start = mid + 1
        elif m < N_list[mid] :
            end = mid - 1
        else :
            start = mid
            end = mid
            break

    if start == mid and end == mid:
        print(1)
    else :
        print(0)
