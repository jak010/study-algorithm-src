"""
    Average Program
    
    Input in Message Exit!


"""


# 평균을 구해주는 코드
# ValueError를 발생 시키면 평균값을 보여줌

number = []



while 1:
        try:
            isnumber = int(input("input Number:"))	
            number.append(isnumber)

        except ValueError:
            choice = input("Continue the Value?(y/n(y=continue,n=Exit)):")
            if choice == 'y':
                continue
            else:
                print("===input Value====")
                print(number)
                print("==================")
                print("Average:",sum(number)/len(number))
                break

