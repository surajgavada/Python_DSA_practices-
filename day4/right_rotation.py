num = [5,8,4,6,2,6,5]
k =10
n = len(num)
rotation= k%n
for _ in range(rotation):
    e = num.pop()
    num.insert(0,e)

print(num)
