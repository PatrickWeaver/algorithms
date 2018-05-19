def multiply(a, b):
  n = len(a)
  c = [ [0] * n for _ in range(n)]
  for i in range(0, n):
    for j in range(0, n):
      for k in range(0, n):
        t = a[i][k] * b[k][j]
        c[i][j] += t
  return c

