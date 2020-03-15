#-*- coding:utf-8 -*-
"""
    IT's 8 word bleow Make String len(8)
"""

while 1:
	msg = input("input Here Your MSG:")
	msglen = len(msg)

	if msglen%8 != 0:
		fillersize = "*"*(8-(msglen%8))
		msg += fillersize
		break
	elif msglen%8 == 0:
		print("This is Text become 8string or 8multiple number!!")
		print ("Again!")

print("Input length MSG:",msg)
print("Output length MSG Number:" ,len(msg))
