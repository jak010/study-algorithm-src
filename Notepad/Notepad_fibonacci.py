def find_fibonacchi_seq_iter(n):
    if n < 2: pass
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(find_fibonacchi_seq_iter(10))
