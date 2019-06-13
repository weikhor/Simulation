ang = 10 # optimum ang = 9.5 to 15
numberofsample= 1000 # optimum numberofsample = 1000 to 5000

########################################
import os
import math
import numpy as np
import random
########################################
item = []
n = 0
for filename in os.listdir(os.getcwd()):
   if "part" in filename:
      n = n + 1
	
for i in range(1,int(n+1)):
   f = open("part"+str(i)+".xyz")
   for line in f:
       if(len(line.split()) == 4):
            item = item + [[line.split()[0],line.split()[1],line.split()[2],line.split()[3]]]
f.close()

#########################################
num = len(item)
f = open("store.xyz", "w")
f.write(str(num))
f.write("\n")
f.write("ITEM: NUMBER OF ATOMS " + str(num))
f.write("\n")
for line in item:
    f.write(str(line[0])+" "+str(line[1])+" "+str(line[2])+" "+str(line[3]))
    f.write("\n")
f.close()

##########################################
def angle(x1,y1,x2,y2):
    X = abs(x2-x1)
    Y = abs(y2-y1)
    if(X == 0):
       X = 0.1
    if(x2 - x1 >= 0 and y2 - y1 >= 0):
        return math.atan(Y/X)
    elif(x2 - x1 <= 0 and y2 - y1 >= 0):
        return math.atan(Y/X) + np.pi/2
    elif(x2 - x1 <= 0 and y2 - y1 <= 0):
        return math.atan(Y/X) + np.pi
    else:
        return math.atan(Y/X) + np.pi*(3/2)

###########################################
def distance(x1,y1,x2,y2):
   return math.sqrt((x1-x2)**2+(y1-y2)**2)

###########################################
f = open("final.xyz","r")
x_avg = 0
y_avg = 0
num = 0

for line in f:
   if(len(line.split()) == 4):
      x_avg = x_avg + float(line.split()[1])
      y_avg = y_avg + float(line.split()[2])
      num = num + 1
f.close()

x_avg = x_avg/num
y_avg = y_avg/num

########################################################
i = 0
while(i < numberofsample):
   f2 = open("PART"+str(i+1)+".xyz","w")
   a1 = random.uniform(0.000,360.000)
   a2 = (a1+ang)
   List = []
   
   if(a2 > 360):
      f1 = open("store.xyz","r")
      for line in f1:
         if(len(line.split()) == 4):
            x = float(line.split()[1])
            y = float(line.split()[2])
            z = float(line.split()[3])
            a = angle(x_avg,y_avg,x,y)*180/np.pi
            a2 = (a1+ang)%360
            if((a>=a1 and a<=360) or (a>=0 and a < a2)):
               List.append([x, y, z])
               num = num + 1
      f1.close()
            
   else:
      f1 = open("store.xyz","r")
      for line in f1:
         if(len(line.split()) == 4):
             x = float(line.split()[1])
             y = float(line.split()[2])
             z = float(line.split()[3])
             a = angle(x_avg,y_avg,x,y)*180/np.pi
             if(a>=a1 and a<=a2):
                List.append([x, y, z])
                num = num + 1
      f1.close()

   num = 0
   i = i + 1
   f2.write(str(len(List)))
   f2.write("\n")
   f2.write("ITEM: NUMBER OF ATOMS " + str(num))
   f2.write("\n")
   for item in List:
      f2.write(str(1)+" "+str(item[0])+" "+str(item[1])+" "+str(item[2]))
      f2.write("\n")
   f2.close()
   f1.close()






