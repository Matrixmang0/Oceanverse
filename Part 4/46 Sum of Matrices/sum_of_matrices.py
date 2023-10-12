def check_matrix(X):
  a = len(X)

  for i in X:
    if len(i)!=a:
      return False
  return True


def sum_matrices(A, B):

  if (not(check_matrix(A))) and (not(check_matrix(B))):
    return (f"Both the matrices {A} and {B} are not square matrices")
  elif not (check_matrix(A)):
    return (f"The matrix {A} is not a square matrix")
  elif not (check_matrix(B)):
    return (f"The matrix {B} is not a square matrix")
  sum_mat = []
  if len(A)==len(B):
    for i in range(len(A)):
      row = []
      for j in range(len(A[i])):
        row.append(A[i][j]+B[i][j])
      sum_mat.append(row)

    return sum_mat
  else :
    return (f"Both the matrices are square but of different dimensions")


x = [[3,5,6],[6,7,8],[4,5,6]]
y = [[4,5],[1,8],[9,7]]
q = [[6,9],[5,7],[0,1]]
w = [[5,6],[8,9]]
p = [[6,8],[3,7]]
z = [[6,0,1],[2,6,1],[8,9,1]]


print(sum_matrices(y,p))


      