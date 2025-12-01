f=open("shri.txt","r")
data=f.read()


print(data)
f.tell()



#WRITE A FILE

'''f1=open("shri.txt","w")
f1.write("i like and my ideal is VIRAT KOHLI")
data1=f1.write
print(data1)
print(data)
f2=open("shri.txt","a")
f2.write("\n\nI am Shrinath Rajput")
data3=f2.write
print(data3)'''

'''file=open(ufn,"r")
ufn=ufn+".txt"
file1 =open(ufn,"r")
file2=open("shri.txt","w")
file2.write(file1.read())
file1.close()
file2.close()
file2=open("shri.txt","r")
file2.read()'''


with open ("shri.txt","r")as fri:
    data2=fri.read()
print(data)
fri.close()

import os
os.remove('shri.txt')

