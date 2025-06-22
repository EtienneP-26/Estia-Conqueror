level = 5
lvls = [5]
print(level)

for i in range(1, 100):
    level = level * 1.2 + 12
    print(level//1)
    lvls.append(int(level//1))

print(lvls)