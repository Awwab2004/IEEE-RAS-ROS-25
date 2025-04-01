def prime_factors(num):
    factors = []
    i = 2
    while num > 1:
        while num % i == 0:
            factors.append(i)
            num //= i
        i += 1
    return factors
num = int(input("Enter a number: "))
print("Prime Factors:", ", ".join(map(str, set(prime_factors(num)))))