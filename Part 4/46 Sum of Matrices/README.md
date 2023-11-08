# Matrix Operations in Python

This Python script provides functions for matrix operations, including checking if a matrix is square and adding two square matrices.

## Table of Contents

- [Description](#description)
- [Functions](#functions)
- [Usage](#usage)

## Description

This script includes two matrix-related functions:

1. **`check_matrix(X)`:** Checks if a given matrix is square, meaning it has the same number of rows and columns.

2. **`sum_matrices(A, B)`:** Adds two square matrices if they have the same dimensions.

## Functions

### `check_matrix(X)`

- **Description:** Checks if a matrix is square.
- **Arguments:**
  - `X` (list): The matrix to be checked.
- **Returns:**
  - `True` if the matrix is square.
  - `False` if the matrix is not square.

### `sum_matrices(A, B)`

- **Description:** Adds two square matrices.
- **Arguments:**
  - `A` (list): The first square matrix.
  - `B` (list): The second square matrix.
- **Returns:**
  - The sum of the two matrices if they are of the same dimensions.
  - An error message if the matrices are not square or have different dimensions.

## Usage

1. Open the script in your preferred Python environment or editor.

2. Modify the matrices `A` and `B` with your own data or create new matrices as needed.

3. Call the functions `check_matrix(X)` or `sum_matrices(A, B)` with your matrices as arguments.

4. The functions will return the results or error messages as described in the functions' descriptions.

```python
x = [[3, 5, 6], [6, 7, 8], [4, 5, 6]]
y = [[4, 5], [1, 8], [9, 7]]
q = [[6, 9], [5, 7], [0, 1]]
w = [[5, 6], [8, 9]]
p = [[6, 8], [3, 7]]
z = [[6, 0, 1], [2, 6, 1], [8, 9, 1]]

result = sum_matrices(y, p)
print(result)
```
