num = [5,4,2,8,7]
k =3
n = len(num)
rotation= k%n
for _ in range(rotation):
    e = num.pop()
    num.insert(0,e)
print(num)