import random_numbers


def insertion(number_list):
  for j in range(1, len(number_list)):
    k = number_list[j]
    i = j - 1
    while i >= 0 and number_list[i] > k:
      number_list[i + 1] = number_list[i]
      i = i - 1
      number_list[i + 1] = k
  return number_list  

def merge(number_list):

  def merge_lists(number_list, p, q, r):
    print(number_list)
    n1 = q - p + 1
    n2 = r - q
    l = [None] * (n1 + 1)
    r = [None] * (n2 + 1)

    for i in range(0, n1):
      l[i] = number_list[p + i - 1]

    for j in range(0, n2):
      r[j] = number_list[q + j]
    
    print(l)
    print(r)



  n = [0,1,2,3,4,5,6,7]
  merge_lists(n, 0, 3, 7)

  pass


merge([])


