def fibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    a,b=0,1
    for n in range(2,num+1):
        a,b=b,a+b

    return b
print(fibo(2))