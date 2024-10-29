def binary_decimal(num):
    dec_value=0
    length=len(num)
    for i in range (length):
        bit=int(num[length-1-i])
        dec_value+=bit*(2**i)
    return dec_value
print(binary_decimal("111"))

def decimal_binary(deci_num):
    if deci_num==0:
      return "0"
    
    bin_num=""
    while deci_num>0:
        rem=deci_num%2
        bin_num=str(rem)+bin_num
        deci_num//=2
    return bin_num
print(decimal_binary(8))


