N = int(input())
divisors = [divisor for divisor in range(1,N+1) if N % divisor == 0]
print(*divisors)
