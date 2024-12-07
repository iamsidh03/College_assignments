import random
def generate_random(size=4):
    return [[random.randint(0,1) for _ in range(size)]for _ in range(size)]

def find_max_row(matrix):
    row_sum=[sum(row) for row in matrix]
    return row_sum.index(max(row_sum))

def find_max_col(matrix):
    col_sum=[sum(row[col] for row in matrix) for col in range(len(matrix[0]))]
    return col_sum.index(max(col_sum))

def print_(matrix):
    for row in matrix:
        print("".join(map(str,row)))

matrix=generate_random()
print("Generate 4 by 4 matrix")
print_(matrix)

r=find_max_row(matrix)
c=find_max_col(matrix)
print(f" largest row : {r}")
print(f" largest column : {c}")
