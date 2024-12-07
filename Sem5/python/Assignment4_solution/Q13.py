#WriteaPythonfunctionthatsortsalistoftuplesbasedonthesecondelementofeachtuple.
def sorted_t(t):
    return sorted(t,key=lambda x :x[1])

t=[(2,3),(4,1),(4,0),(10,8)]
sorted_tupple=sorted_t(t)
print("original list of tuples ",t)
print("Sorted List of tuples ",sorted_tupple)


'''
    sorted() Function:
The sorted() function in Python is used to sort an iterable (e.g., list, tuple) and returns a new sorted list. 
It does not modify the original iterable.
Syntax:

        sorted(iterable, key=None, reverse=False)
    iterable: The collection to sort (e.g., a list of tuples).
    key: A function that specifies a "sort key," i.e., which part of the elements to use for sorting.
    reverse: A boolean that, if set to True, sorts in descending order. Default is False (ascending order).
    '''

'''
              key=lambda x: x[1]:
The key parameter tells sorted() how to evaluate each element during sorting.
A lambda function is a small, anonymous function defined as lambda arguments: expression.
Here, lambda x: x[1] means:
x represents an individual tuple in the list.
x[1] extracts the second element of the tuple.  
                '''