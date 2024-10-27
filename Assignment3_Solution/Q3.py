def sun_squares_even():
    tsum=0
    for num in range(1,51):
        if num%2==0:
           tsum+=num**2
    return tsum
print(sun_squares_even())