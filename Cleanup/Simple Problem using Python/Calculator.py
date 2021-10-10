# 계산기!

def sum(n1,n2):
    return n1+n2
def min(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2
def mul(n1,n2):
    return n1*n2

def input_():
    n1 = int(input("Num1:"))
    n2 = int(input("Num2:"))
    return n1,n2

def searchOp(op):
    oper = '+-/*'
    result = oper.find(op)
    if result == -1:
        return result
    else:
        return result

while(1):
    input_value = str(input("Input the Operated:"))

    if searchOp(input_value) == 0:
        print(input_value)
        num1,num2 =input_()
        print(sum(num1,num2))
        
    elif searchOp(input_value) == 1:
        print(input_value)
        input_()
        print(min(num1,num2))

    elif searchOp(input_value) == 2:
        print(input_value)
        input_()
        print(div(num1,num2))

    elif searchOp(input_value) == 3:
        print(input_value)
        input_()
        print(mul(num1,num2))

    elif input_value == 'help':
        print("help Text")
    else:
        print("Not Support Operated")
