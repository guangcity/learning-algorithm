def fib(n, Memo):
    if Memo[n] != -1:
        return Memo[n]
    if n <= 2:
        Memo[n] = 1
    else:
        Memo[n] = fib(n - 1, Memo) + fib(n - 2, Memo)
    return Memo[n]

def Fib(n):
    if n<=0:
        return n
    Memo = {}
    for i in range(n+1):
        Memo[i]=-1
    return fib(n,Memo)
if __name__ == '__main__':
    res = Fib(10)
    print(res)
