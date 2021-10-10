"""
몬테카를로 난수

난수를 이용하여 함수의 값을 확률적으로 계산하는 알고리즘
"""


import math
import random

while True:
    cnt = 0

    choice = int(input("INPUT NUMBER:"))
    for i in range(1,choice):
        x=random.uniform(0,1.0)
        y=random.uniform(0,1.0)
        s = pow(x,2) + pow(y,2)
        print("%0.2f %0.2f %0.2f" %(x,y,s))
        
        if s <=1:
            cnt += 1

    print("PI",4*cnt/choice)

    z = input("quit:")
    if(z == 'z'):
        break


