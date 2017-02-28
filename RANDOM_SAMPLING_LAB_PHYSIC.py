#PHYSICS_LAB_RANDOM_SAMPLING
#---Coder: Ojas-singh
#---www.github/Ojas-singh/Oja
import random
import math
print "-------------------PHYSICS_LAB_RANDOM_SAMPLING----------------------------"
N=int(raw_input("Enter N :"))
bin=float(raw_input("Enter bin size :"))
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
result.write("\n bin size :"+str(bin))
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

