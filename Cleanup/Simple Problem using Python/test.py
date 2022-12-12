num = int(input("input Number:"))
d = 1
n_sum = []
n2_sum = []
while d <= num:
    if num % d == 0:
        n_sum.append(d)
        d = d + 1
    else:
        d = d + 1

print(n_sum)

for i in n_sum:
    if ((n_sum[0] * n_sum[1 + (i - 1)]) == n_sum[-1]):
        n2_sum.append(i)


    else:
        pass

print(n2_sum)
