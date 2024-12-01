#Python program that prompts the user to enter a list, determines whether it is sorted, and displays the appropriate message. The first number in the input is interpreted as the size of the list and is excluded from the actual list:

def is_sorted(lst):
   return lst==sorted(lst)

def main():
    user_input=input("Enter List ")
    num=list(map(int,user_input.split()))
    size=num[0]
    actual_lst=num[1:]

    if len(actual_lst) != size:
       print("size of list is not equal to size specified")
       return
   

    if is_sorted(actual_lst):
       print("list is sorted")
    else:
       print("List is not sorted")

main()