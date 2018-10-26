number = [1,'a',2,'b',5,'c']

print("Current List:", number)

for i in number:
	if type(i) == str:
		number.remove(i)
	else:
		None

print("Current List:",number)
