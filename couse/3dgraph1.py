"""from mpl_toolkits.mplot3d import axes3d
import matplotlib
import matplotlib.pyplot as plt
fig=plt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')
X,Y,Z=[1,2,3,4,5,6,7,8],[2,5,3,8,9,5,6,1],[3,6,2,7,5,4,5,6]
chart.plot(X,Y,Z)
plt.show()"""

#3D scatter plot

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
fig=plt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')
X,Y,Z=[1,2,3,4,5,6,7,8],[2,5,3,8,9,5,6,1],[3,6,2,7,5,4,5,6]
Xx,Yy,Zz=[-1,-2,-3,-4,-5,-6,-7,-8],[-2,-5,-3,-8,-9,-5,-6,-1],[-3,-6,-2,-7,-5,-4,-5,-6]

chart.scatter(X,Y,Z,color='red',marker='x')
chart.scatter(Xx,Yy,Zz,color="blue",marker="*")
chart.set_title("3D Scatter Plot")
chart.set_xlabel("THIS IS X_LABEL")
chart.set_ylabel("THIS IS Y_LABEL")
chart.set_zlabel("THIS IS Z_LABEL")
plt.show()
