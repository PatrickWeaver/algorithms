import random

def random_integer_list():
  
  random_list = []
  
  for n in range(0, 99):
    random_number = random.randint(0, 999)
    random_list.append(random_number)

  return random_list
