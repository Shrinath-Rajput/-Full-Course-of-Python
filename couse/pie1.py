import matplotlib
import matplotlib.pyplot as plt
sizes=[50,20,8,18,10]
labels=['c','c++','java','java advance','python',]

colors=["pink","yellow","blue","green","red"]
plt.pie(sizes,colors=colors,startangle=90,labels=labels)
plt.title('PIE CHART')
plt.legend(title="legend")
plt.axis("equal")
plt.show()

