def prime_factorization(n):
    if n < 2:
        return []
    factors = []
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            exponent = 0
            while n % factor == 0:
                n //= factor
                exponent += 1
            factors.append((factor, exponent))
        factor += 1 if factor == 2 else 2
    
    if n > 1:
        factors.append((n, 1))
    
    return factors

def main():
    while True:
        try:
            num = int(input("Enter a positive integer (or 0 to exit): "))
            if num == 0:
                print("Exiting the program.")
                break
            if num < 0:
                print("Please enter a positive integer.")
                continue
            
            result = prime_factorization(num)
            
            if not result:
                print(f"{num} has no prime factors (it is 1).")
            else:
                print(f"Prime factorization of {num}:")
                factorization = " * ".join([f"{factor}^{exponent}" for factor, exponent in result])
                print(factorization)
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()