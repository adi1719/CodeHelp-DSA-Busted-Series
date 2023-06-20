def sieve():
    prime = [True] * 1000001  # Initialize all numbers as prime

    # Sieve of Eratosthenes
    for i in range(2, 1000001):
        if prime[i]:
            # Mark multiples as non-prime
            for j in range(2*i, 1000001, i):
                prime[j] = False

    prime[0] = prime[1] = False
    return prime


def main():
    primes = sieve()

    while True:
        n = int(input("Enter a number (enter -1 to exit): "))
        if n == -1:
            break

        if primes[n]:
            print("It is a prime number")
        else:
            print("It is not a prime number")

