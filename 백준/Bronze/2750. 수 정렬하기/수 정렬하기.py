num = int(input())

num_list = []

for i in range(num):
    num_list.append(int(input()))


num_list.sort()

for i in range(len(num_list)):
    print(num_list[i])