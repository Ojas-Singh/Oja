#PHYSICS_LAB_RANDOM_SAMPLING
#---Coder: Ojas-singh
#---www.github/Ojas-singh/Oja
#required mathplotlib
#required numpy
import random
import math
print "-------------------PHYSICS_LAB_RANDOM_SAMPLING----------------------------"
print "--------------------------by:Ojas Singh-----------------------------------"
N=int(raw_input("Enter N :"))
b=int(raw_input("Enter number bins:"))
data=[]
v=float(raw_input("Enter maximum Voltage :"))
f=int(raw_input("Enter AC Source Frequency :"))
for i in range(0,N):
    t=random.random()
    w=2*3.14159265359*f
    Volt=math.sin(w*t)*v
    data.append(round(Volt,2))
result = open('result.txt', 'w')
result.write("PHYSICS_LAB_RANDOM_SAMPLING--Result-Report")
result.write("\n" "#############  Configuration#############\n")
result.write("\n Number   :"+str(N))
result.write("\n Maximum Voltage  :"+str(v))
result.write("\n Frequency of AC Source :"+str(f))
result.write("\n bins number :"+str(b))
result.write("\n" "#########################################\n")

result.write("\n" "--------DATA Collected(Simulated)--------\n")
for i in range(0,len(data)):
    s=str(i+1)+".   "+str(data[i])
    result.write("%s\n" % s)
result.write("\n ################ result ####################" "\n")
result.write("\n Maximum Voltage Observed:"+str(max(data)))
s=0
for i in data:
    s=s+i
result.write("\n Average Voltage Observed :"+str(s/N))


#bin distribtion

import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import numpy as np
fig = plt.figure(figsize=(8,8))
ax  = fig.add_subplot(111)
myHist = ax.hist(data,int(b))

plt.title("Random sampling")
plt.xlabel("Voltage")
plt.ylabel("Frequency")

x = np.linspace(-1*v,v)

f=N*(2*v/b)/(pi*(v**2-x**2)**(.5))
h = ax.plot(x,f)

#plt.show()
plt.savefig('plot_histogram.png')  # save the figure to file
(n, bins, patches) = plt.hist(data,b,label='hst')
plt.close()
print 'Histogarm saved to "plot_histogram.png" sucessfully!'
