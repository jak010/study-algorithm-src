""" String Revesed"""

s = input("Input the Sentence:")

new_s = str()

for x in range(len(s)-1 ,-1 , -1):
    new_s += s[x]

print(new_s)
