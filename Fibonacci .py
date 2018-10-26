result =[0,1]

def fibo(num):
	for i in range(2,num+1):
		result.append(result[i-1]+result[i-2])

	return result
		
print(fibo(5))

