sub = []
for _ in range(10):
    a =int(input()) % 42
    sub.append(a)

print(len(set(sub)))