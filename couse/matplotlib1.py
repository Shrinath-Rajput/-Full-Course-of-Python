
"""import matplotlib
import matplotlib.pyplot as pt
pt.plot([1,2,3,4],[3,8,10,25])
pt.show() """

#adding label

"""import matplotlib
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5],[20,10,12,7,21])
plt.title("Match Summery")
plt.xlabel("Batting")
plt.ylabel("Runs")
plt.show()"""

"""import matplotlib
import matplotlib.pyplot as plt
x=[]
y=[]
readfile1=open("graph.txt","r")
data=readfile1.read().split()
for i in data:
    val=i.split(",")
    x.append(val[0])
    y.append(val[1])
    print(x)
    print(y)
    plt.plot(x,y)
print(data)

plt.title("Summery Of presently")
plt.xlabel("months")
plt.ylabel("present a student")
plt.show()"""

import matplotlib
import matplotlib.pyplot as plt
fig=plt.figure()
rect=fig.patch
rect.set_facecolor('green')
x=[]
y=[]
x2=[0,4,7,12]
y2=[3,7,1,12]
x3=[0,4,6,8]
y3=[13,5,8,2]
readfile=open("graph.txt","r")
data=readfile.read().split("\n")

for i in data:
    val=i.split(",")
    x.append(val[0])
    y.append(val[1])
    print(x)
    print(y)
    print(data)
graph1=fig.add_subplot(2,2,1,)
graph1.plot(x,y,'red',linewidth=4.0)
graph1.plot(x2,y2,'yellow',linewidth=8.0)
graph1.plot(x3,y3,'blue',linewidth=6.0)
graph1.tick_params(axis="x",color="white")#point la dila color manmje 1 2 chya khali
graph1.tick_params(axis="y",color="white")
graph1.spines["top"].set_color("blue")#graph madlya vr chya background la blue dila
graph1.spines["left"].set_color("orange")
graph1.spines["right"].set_color("black")
graph1.spines["bottom"].set_color("red")
graph1.set_title("Shrinath Rajput",color="orange",size=20)
graph1.set_xlabel("played_Match",color="black",size=10)
graph1.set_ylabel("Runs",color="red",size=10)

#add a new graph


graph2=fig.add_subplot(2,2,2,)
graph2.plot(x2,y2,'yellow',linewidth=8.0)
graph2.plot(x3,y3,'blue',linewidth=6.0)
graph2.tick_params(axis="x",color="white")#point la dila color manmje 1 2 chya khali
graph2.tick_params(axis="y",color="white")
graph2.spines["top"].set_color("blue")#graph madlya vr chya background la blue dila
graph2.spines["left"].set_color("orange")
graph2.spines["right"].set_color("black")
graph2.spines["bottom"].set_color("red")
graph2.set_title("Shrinath Rajput",color="orange",size=20)
graph2.set_xlabel("played_Match",color="black",size=10)
graph2.set_ylabel("Runs",color="red",size=10)


#add 3 rd graph
graph3=fig.add_subplot(2,1,2)
graph3.plot(x,y,'red',linewidth=4.0)
graph3.plot(x2,y2,'yellow',linewidth=8.0)

graph3.plot(x3,y3,'blue',linewidth=6.0)
graph3.tick_params(axis="x",color="white")#point la dila color manmje 1 2 chya khali
graph3.tick_params(axis="y",color="white")
graph3.spines["top"].set_color("blue")#graph madlya vr chya background la blue dila
graph3.spines["left"].set_color("orange")
graph3.spines["right"].set_color("black")
graph3.spines["bottom"].set_color("red")
graph3.set_title("Shrinath Rajput",color="orange",size=20)
graph3.set_xlabel("played_Match",color="black",size=10)
graph3.set_ylabel("Runs",color="red",size=10)





plt.show()