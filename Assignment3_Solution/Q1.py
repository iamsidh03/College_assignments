def first_second_third_greater(num):
    first=second=third=-1
    for digit in str(num):
        digit=(int)(digit)
        if digit>first:
            third=second
            second=first
            first=digit
        elif digit>second:
            second=first
            second=digit
        elif digit>third:
            digit=third

    return first,second,third

print(first_second_third_greater(6237))
