# 1.random module

''' import random
var1=random.randint(0,100)
while True:
    var2=int(input("enter the number"))
    if var2>var1:
        print("hello")

    elif var2<var1:
        print("hiii")
    else:
        print("succesfully")
    break '''


#2. choice module
'''import random
shri=("vadapav","pavbhaji","mishal","puribhaji")
print(random.choice(shri))
random.shuffle(shri)
print(shri)'''


#3 sys module
'''import sys
inputstatement=sys.stdin.readline()
'this is a password '
print(inputstatement)
inputstatement1=sys.stdout.write("virat")
print(inputstatement1)
sys.version'''


#4 time module
import time
def number(max):
    time1=time.time()
    for i in range(0,max):
        print(i)
    time2=time.time()
    print(str(time1-time2))
number(100)
tup=(2005,10,15,8,45,12,6,0,0)
time.asctime(tup)
time.localtime()
for i in range(0,5):
    print(i)
    time.sleeo(1)