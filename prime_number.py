def is_prime(num):
  prime = num != 1
  if prime:
    for n in range(2, num):
      if (num % n == 0):
        prime = False
  return prime

print(is_prime(23))