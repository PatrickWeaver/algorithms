import random_numbers
import math

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
    n1 = q - p + 1
    n2 = r - q
    left = [math.inf] * (n1 + 1)
    right = [math.inf] * (n2 + 1)

    for i in range(0, n1):
      left[i] = number_list[p + i]

    for j in range(0, n2):
      right[j] = number_list[q + j + 1]
    
    i = 0
    j = 0

    for k in range(p, r + 1):
      if left[i] <= right[j]:
        number_list[k] = left[i]
        i = i + 1
      else:
        number_list[k] = right[j]
        j = j + 1

  def merge_sort(number_list, p, r, o):
    if p < r:
      q = (p + r) // 2
      merge_sort(number_list, p, q, 1)
      merge_sort(number_list, q + 1, r, 2)
      merge_lists(number_list, p, q, r)

  merge_sort(number_list, 0, len(number_list) - 1, 0)


random_list = random_numbers.random_integer_list()
print(random_list)
merge(random_list)
print(random_list)


