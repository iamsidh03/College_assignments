
numbers=[10,3,7,1,9,4,2,8,5,6]
list(map(lambda x:x**2,filter(lambda x:x%2!=0,numbers)))

'''
 Let's break down the code and address each question:

### Given Code:
```python
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
```

### Explanation:
1. **Filter operation (`filter(lambda x: x % 2 != 0, numbers)`)**:
   - The filter function iterates over each element in the `numbers` list and applies the lambda function `lambda x: x % 2 != 0` to check if the number is odd (`x % 2 != 0`).
   - Only the odd numbers are passed on to the next operation.
   
2. **Map operation (`map(lambda x: x ** 2, ...)`)**:
   - The map function takes the result from the filter (odd numbers) and applies the lambda function `lambda x: x ** 2` to square each of the odd numbers.

### Now let's answer the questions:

---

### a) **How many times does the filter operation call its lambda argument?**

The `filter` function applies its lambda function (`lambda x: x % 2 != 0`) to each element in the `numbers` list. 

The `numbers` list has 10 elements, and the filter function checks each element to see if it is odd. Since `filter` processes each element once, it will call the lambda argument **10 times** (once for each number in the list).

### Answer: **10 times**

---

### b) **How many times does the map operation call its lambda argument?**

The `map` function applies its lambda function (`lambda x: x ** 2`) to each element returned by the `filter` operation. The `filter` operation only allows the odd numbers through.

Let's first identify the odd numbers in the list:
- `numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]`
- Odd numbers: `3, 7, 1, 9, 5` (5 odd numbers)

So, the `map` function will apply the lambda function to **5 odd numbers** (the output of the filter), and the lambda will be called once for each odd number.

### Answer: **5 times**

---

### c) **If you reverse the filter and map operations, how many times does the map operation call its lambda argument?**

If you reverse the filter and map operations, the code would look like this:

```python
list(filter(lambda x: x % 2 != 0, map(lambda x: x ** 2, numbers)))
```

1. **Map operation first**: The map function will apply `lambda x: x ** 2` to each element of the `numbers` list, squaring every element.
2. **Filter operation second**: The filter function will then apply `lambda x: x % 2 != 0` to each squared number, allowing only the odd squared numbers through.

The `map` function will apply its lambda to **all 10 elements** of the `numbers` list (since the map is applied to the entire list).

### Answer: **10 times**

---

### Summary of Answers:
- a) **10 times** (filter function calls its lambda 10 times, once for each element in the list)
- b) **5 times** (map function calls its lambda 5 times, once for each odd number)
- c) **10 times** (map function calls its lambda 10 times when reversed, once for each element in the list)

Let me know if you need further clarification!
'''