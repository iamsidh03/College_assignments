def reverse_String(s):
    rev_str=""
    for char in s:
        rev_str=char+rev_str
    return rev_str
print(reverse_String("hello"))