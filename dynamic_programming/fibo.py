def fibo(n, memo):
    if n == 0 or n == 1:
        return n
    if memo[n] == 0:
        memo[n] = fibo(n-1, memo)+fibo(n-2, memo)
    
    return memo[n]
print(fibo(9,[0]*(9+1)))