
import random

def calculate_prime_average(limit):
    primes = []
    num = 2
    while len(primes) < limit:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return sum(primes) / len(primes)

def calculate_fibonacci_average(limit):
    fibs = [0, 1]
    while len(fibs) < limit:
        fibs.append(fibs[-1] + fibs[-2])
    return sum(fibs) / len(fibs)

def calculate_even_average(limit):
    evens = [i for i in range(2, 2 * limit + 1, 2)]
    return sum(evens) / len(evens)

def calculate_random_average(count, range_min, range_max):
    random_numbers = [random.randint(range_min, range_max) for _ in range(count)]
    return sum(random_numbers) / len(random_numbers)
