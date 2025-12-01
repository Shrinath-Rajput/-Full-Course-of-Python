import matplotlib
import matplotlib.pyplot as plt
import numpy  as np
fig=plt.figure()
rect=fig.patch
rect.set_facecolor('green')#background color

pos=np.arange(6)+0.5
years=["2011","2016","2018","2020","2022","2025"]
runs=["8000","9000","1000","11000","12000","13000",]

plt.barh(pos,(4,8,12,13,17,6),align="center",color="red")

plt.title("VIRAT KOHLI",color="white",size=20)
plt.xlabel("matches",color="black",size=20)
plt.ylabel("made a runs",color="orange",size=20)
plt.tick_params(axis="x",color="white")
plt.tick_params(axis="y" ,color="white")

plt.xticks(pos,years)
plt.yticks(pos,runs)
plt.show()
