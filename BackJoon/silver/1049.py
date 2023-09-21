n, m = map(int, input().split())

packages = []
eaches = []
for _ in range(m):
    pack, each = map(int, input().split())
    packages.append(pack)
    eaches.append(each)

min_pack = min(packages)
min_eaches = min(eaches)

if min_pack >= min_eaches * 6:
    print(min_eaches * n)
else:
    if min_pack >= (min_eaches * (n % 6)):
        print(((n // 6) * min_pack) + ((n % 6) * min_eaches))
    else:
        print(((n // 6) + 1) * min_pack)
