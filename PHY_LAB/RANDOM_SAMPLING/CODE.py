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
result = open('result/report.txt', 'w')
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

plt.title("Random sampling Histogram")
plt.xlabel("Voltage")
plt.ylabel("Frequency")

x = np.linspace(-1*v,v)

f=N*(2*v/b)/(pi*(v**2-x**2)**(.5))
h = ax.plot(x,f)

#plt.show()
plt.savefig('result/plot_histogram.png')  # save the figure to file
(n, bins, patches) = plt.hist(data,b,label='hst')
plt.close()
print 'Histogarm saved to "plot_histogram.png" sucessfully!'


#norm
fig = plt.figure(figsize=(8,8))
ax  = fig.add_subplot(111)
myHist = ax.hist(data,int(b),normed=True)

plt.title("Random sampling Histogram normalized")
plt.xlabel("Voltage")
plt.ylabel("Frequency")



#plt.show()
plt.savefig('result/plot_histogram_normed.png')  # save the figure to file
(n, bins, patches) = plt.hist(data,b,label='hst')
plt.close()
print 'Histogarm saved to "plot_histogram_normed.png" sucessfully!'
#reconturction
nv=[]
r=0
for i in range(b/2,b):
    r=r+n[i]
    nv.append(r)

fig = plt.figure(figsize=(8,8))
ax  = fig.add_subplot(111)


u = data
y=[]
for i in data:
    y.append(N*arcsin(i/v)/pi)

h2=ax.scatter(u, y,color="red")



plt.title("Random sampling reconstruction")
plt.xlabel("Voltage")
plt.ylabel("Intregated Frequency")

x = np.linspace(-1*v,v)

nvf=N*arcsin(x/v)/pi
h = ax.plot(x,nvf)

#plt.show()
plt.savefig('result/plot_reconstruction.png')  # save the figure to file
plt.close()
print 'Reconstruction Graph saved to "plot_Reconstuction.png" sucessfully!'
result.write("\n #######################################################")
result.write("\n                        raw_data            ")
result.write("\n #######################################################")

result.write("\n "+str(data))

#table
result.write("\n #################################################################################")
result.write("\n                                   table                                          ")
result.write("\n #################################################################################")
result.write("\n | S.no ||      Bin        ||    N(V)    ||     Nv      ||  v=V0*sin(pi*Nv/N) |")
for i in range(0,b/2):
    result.write("\n --------------------------------------------------------------------------------------")
    result.write("\n | "+str(i+1)+"    || "+str(bins[i+b/2])+"-"+str(bins[i+1+b/2])+"     ||     " +str(n[i+b/2])+"    ||      "+str(nv[i])+"    ||        "+str(round(float(v*sin(pi*nv[i]/N)),1))+"       |")
result.write("\n --------------------------------------------------------------------------------------")


fig = plt.figure(figsize=(8,8))
bx  = fig.add_subplot(111)


o = nv
z=[]
for i in nv:
    z.append(v*sin(pi*i/N))

h2 = bx.scatter(o,z,color="red")



plt.title("Reconstructed sine Wave")
plt.xlabel("Nv")
plt.ylabel("Voltage")

x = np.linspace(0,nv[len(nv)-1])

nvf=v*sin(pi*x/N)
h = bx.plot(x,nvf)

#plt.show()
plt.savefig('result/plot_reconstruction_sine.png')  # save the figure to file
plt.close()
print 'Reconstruction sine Graph saved to "plot_Reconstuction_sine.png" sucessfully!'
