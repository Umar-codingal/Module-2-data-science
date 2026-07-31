def is_prime(n):
    for d in range(2,int(n)):
        if n % d== 0:
            return False
    return True

print([n for n in range(10, 100) if is_prime(n)])