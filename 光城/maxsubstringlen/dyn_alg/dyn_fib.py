def fib(n):
    if n<=1:
        return n
    Memo_0 = 0
    Memo_1 = 1
    Memo_n = 1
    for i in range(2,n+1):
        Memo_n = Memo_0 + Memo_1
        Memo_0 = Memo_1
        Memo_1 = Memo_n

    return Memo_n


a = fib(10)
print(a)