def is_armstrome(num):
    num_digit=len(str(num))
    tsum=0
    temp=num
    while temp>0:
        digit=temp%10
        tsum+=digit**num_digit
        temp//=10

    return tsum==num

print(is_armstrome(153))

     