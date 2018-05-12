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



random_list = random_numbers.random_integer_list()
print("Random List:")
print(random_list)
sorted_list = insertion(random_list)
print("Sorted List:")
print(sorted_list)
