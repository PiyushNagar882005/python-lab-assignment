import math

def list_primes(limit):
  primes = []
  for num in range(2, limit + 1):
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
      if num % i == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(num)
  return primes
limit = int(input("Enter the limit: "))
prime_numbers = list_primes(limit)
print("Prime numbers up to", limit, "are:", prime_numbers)