import math
import numpy as np

angl = 3.9 # optimum angl = 3.7 to 4.0 
q = 3.5 # optimum q = 3 to 5

#################################
def angle(x1,y1,x2,y2):
    X = abs(x2-x1)
    Y = abs(y2-y1)
    if(x2 - x1 >= 0 and y2 - y1 >= 0):
        return math.atan(Y/X)
    elif(x2 - x1 <= 0 and y2 - y1 >= 0):
        return math.atan(Y/X) + np.pi/2
    elif(x2 - x1 <= 0 and y2 - y1 <= 0):
        return math.atan(Y/X) + np.pi
    else:
        return math.atan(Y/X) + np.pi*(3/2)

##################################
f = open("final.xyz", "r")
x = 0
y = 0
z = 0
num = 0
for line in f:
    if(len(line.split()) == 4):
        x = x + float(line.split()[1])
        y = y + float(line.split()[2])
        z = z + float(line.split()[3])
        num = num + 1
f.close()

x_avg = x/num
y_avg = y/num
z_avg = z/num

####################################
f = open("final.xyz", "r")
Store = {}
for line in f:
    if(len(line.split()) == 4):
        Z = int(float(line.split()[3]))
        if(Z not in Store):
            Store[Z] = []
            save = Store[Z]
            save.append(line.split())
            Store[Z] = save
        else:
            save = Store[Z]
            save.append(line.split())
            Store[Z] = save
f.close()

######################################
f = open("final.xyz", "r")
store = {}
for line in f:
    if(len(line.split()) == 4):
        Z = int(float(line.split()[3]))
        a = angle(x_avg,y_avg,float(line.split()[1]),float(line.split()[2]))
        a = a*180/(np.pi)
        s = a - a%angl
        if(s not in store):
            store[s] = []
            save = store[s]
            save.append(line.split())
            store[s] = save
        else:
            save = store[s]
            save.append(line.split())
            store[s] = save
f.close()

######################################
p = 1
for s in store:
    f1 = open("part" + str(p) + ".xyz", "w")
    f1.write(str(len(store[s])))
    f1.write("\n")
    f1.write("ITEM: NUMBER OF ATOMS " + str(len(store[s])))
    f1.write("\n")
    for item in store[s]:
        f1.write(str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3]))
        f1.write("\n")
    p = p + 1
f1.close()
#######################################

p = p - 1
distance = 0

for i in range(p):
    f1 = open("part" + str(i+1) + ".xyz", "r")
    num = 0
    for line in f1:
        if(len(line.split()) == 4):
            x = abs(float(line.split()[1]) - x_avg)
            y = abs(float(line.split()[2]) - y_avg)
            d = math.sqrt(x*x+y*y)
            if(distance < d):
                distance = d
    f1.close()
    
    f1 = open("part" + str(i+1) + ".xyz", "r")        
    num = 0
    item = []
    num = 0
    for line in f1:
        if(len(line.split()) == 4):
            x = abs(float(line.split()[1]) - x_avg)
            y = abs(float(line.split()[2]) - y_avg)
            d = math.sqrt(x*x+y*y)
            if(d > distance - q):
                item = item + [[str(line.split()[0]),str(line.split()[1]),str(line.split()[2]),str(line.split()[3])]]
                num = num + 1
    f1.close()
    
    f1 = open("part" + str(i+1) + ".xyz", "w")
    f1.write(str(num))
    f1.write("\n")
    f1.write("ITEM: NUMBER OF ATOMS " + str(num))
    f1.write("\n")
    
    for line in item:
        f1.write(str(line[0])+" "+str(line[1])+" "+str(line[2])+" "+str(line[3]))
        f1.write("\n")

    f1.close()
    distance = 0 
############################################


