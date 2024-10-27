def count(n):
    if n<0:
        raise("input must be postive")
    count=0
    while n>0:
     n //=10
     count+=1
    return count
print(count(124253453))