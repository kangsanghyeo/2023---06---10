n = int(input())

data = []
for i in range(n):
    m = input()
    data.append(m)

#print(data)

for d in data:
    if 6 <= len(d) <=9:
        print('yes')
    else:
        print('no')


