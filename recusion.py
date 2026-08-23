"""def fun (x,n):
    if n == 0:
        return
    print (x)
    fun(x,n-1)
fun("suraj",5)"""

def fun(i,n):
    if i>n:
        print("recusion stop here")
        return
    fun(i+1,n)
    print (i)
fun(1,5)

def su30(sum,i,n):
    if i > n:
        print(sum)
        return
    su30(sum+i,i+1,n)

su30(0,0,20)