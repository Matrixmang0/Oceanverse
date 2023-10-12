def check_matrix(X, Y):
  rowsX = len(X)
  colsX = len(X[0])

  rowsY = len(Y)
  colsY = len(Y[0])

  if rowsX == colsY:
    if colsX == rowsY:
      return True
  else: 
    return False


def product_matrices(A, B):

  prod_mat = []

  if check_matrix(A, B):
    for i in range(len(A)):
      row = []
      for j in range(len(A)):
          elem = 0
          for k in range(len(A[i])):
            elem += A[i][k]+B[k][j]
          row.append(elem)
      prod_mat.append(row)
    return prod_mat
  else :
    return (f"The matrices {A} and {B} cannot be multiplied")
  

x = [[3,5,6],[6,7,8],[4,5,6]]
y = [[4,5],[1,8],[9,7]]
q = [[6,9],[5,7],[0,1]]
w = [[5,6],[8,9]]
p = [[6,8],[3,7]]
z = [[6,0,1],[2,6,1],[8,9,1]]


print(product_matrices(x,z))