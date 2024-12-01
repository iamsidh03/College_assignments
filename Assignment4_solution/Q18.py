def sq(user_input):
    return [x**2 for x in user_input]

user_input=input("Enter number")
user_list=list(map(int,user_input.split()))
sq_list=sq(user_list)
print(f"user input {user_input}")
print(f" square list {sq_list}")