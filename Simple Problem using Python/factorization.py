
# 인수분해를 하고 그 순서쌍을 찾아줌
num1 = int(input("Number INput:"))

insu_list = []

for i in range(1,num1):
    if num1 % i == 0:
        insu_list.append(int(i))
    else:
        pass
    
insu_list.append(num1)
print(insu_list)

for i in insu_list:
    for j in insu_list:
        if i*j == insu_list[-1]:
            print("순서쌍:",i,j)
