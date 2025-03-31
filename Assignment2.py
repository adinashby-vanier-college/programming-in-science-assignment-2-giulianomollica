# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(lst):
    if not lst:
        return (None, None)
    
    first = max(lst)
    remaining = [x for x in lst if x != first]
    
    second = max(remaining) if remaining else None
    return (first, second)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    return sorted(set(numbers))
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(lst):
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, n):
    if n <= 0:
        raise ValueError("Step value N must be greater than 0.")
    return lst[::n]

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(a, b):
    result = []
    for i in range(len(a)):
        row_result = []
        for j in range(len(b[0])):
            cell_sum = sum(a[i][k] * b[k][j] for k in range(len(b)))
            row_result.append(cell_sum)
        result.append(row_result)
    return result