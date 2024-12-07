import copy

def demonstrate_copy_types():
    original_list = [['Shallow', 2, 3], [4, 5, 6]]
    
    # Shallow copy: The inner lists are not copied, references are kept
    shallow_copy = copy.copy(original_list)
    
    # Deep copy: The inner lists are also copied
    deep_copy = copy.deepcopy(original_list)
    
    # Modify the deep copy and shallow copy
    deep_copy[0][0] = 1  # Modify the first element of the first inner list in the deep copy
    shallow_copy[1][0] = 'Deep'  # Modify the first element of the second inner list in the shallow copy
    
    # Display the results
    print("Original List:", original_list)
    print("Shallow Copy:", shallow_copy)
    print("Deep Copy:", deep_copy)

# Call the function to demonstrate the copies
demonstrate_copy_types()
