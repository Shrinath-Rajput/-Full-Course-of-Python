import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
fig=plt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,3,4,5,1,6,2,1,7,2]
z=[0,0,0,0,0,0,0,0,0,0,]
dx=np.ones(10)
dy=np.ones(10)
dz=[20,55,45,35,67,25,45,33,61,65]
chart.bar3d(x,y,z,dx,dy,dz,color="red")
chart.set_title("Shrinath Rajput",color="Orange",size=20)
chart.set_xlabel("THIS IS X_LABEL",color="orange",size=10)
chart.set_ylabel("THIS IS Y_LABEL",color="orange",size=10)
chart.set_zlabel("THIS IS Z_LABEL",color="orange",size=10)

plt.show()


#wireframe plot
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
fig=plt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')
x,y,z=axes3d.get_test_data(0.05)
chart.plot_wireframe(x,y,z,rstride=10,cstride=10,color="red")
chart.set_title("Shrinath Rajput",color="Orange",size=20)
chart.set_xlabel("THIS IS X_LABEL",color="orange",size=10)
chart.set_ylabel("THIS IS Y_LABEL",color="orange",size=10)
chart.set_zlabel("THIS IS Z_LABEL",color="orange",size=10)

plt.show()
