import pandas
import matplotlib.pyplot as plt
import numpy as np

df = pandas.read_csv("sumaa.csv",delimiter=';')

data_1 = np.array(df["No"], dtype=int)
data_2 = np.array(df["Result"],dtype=np.float64)

#compression_opts = dict(method='zip',archive_name='out.csv')  
#df.to_csv('out.zip', index=False,compression=compression_opts)

#print(len(data_1))

xpoints = data_1
ypoints = data_2

plt.plot(xpoints,ypoints,alpha=0.7)
#ax = plt.axes()
# Setting the background color of the plot 
# using set_facecolor() method
#ax.set_facecolor("yellow")

plt.xlabel("Number")
plt.ylabel("Result")
plt.title("Diagrame of fun(1+1/2+1/3 ... 1/n)")

plt.grid()
plt.show()

compression_opts = dict(method='zip',archive_name='out.csv')  
df.to_csv('out.zip', index=False,compression=compression_opts)  

#print(data_2)

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
# 
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# 
# plt.plot(xpoints, ypoints)
# plt.grid()
# plt.show()