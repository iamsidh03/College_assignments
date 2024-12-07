import math
def mean_(lst):
    return sum(lst)/len(lst)
def std_deviation(num,mean):
    var=sum((x-mean)**2 for x in num)/(len(num)-1)
    return math.sqrt(var)
def main():
    user_input=input("Enter Numbers ")
    num=list(map(float,user_input.split()))

    if len(num)!=10:
        print("you number must be exactly 10 length")
        return
    mean=mean_(num)
    std_dev=std_deviation(num,mean)
    print(f"Mean: {mean}")
    print(f"deviation: {std_dev}")
main()