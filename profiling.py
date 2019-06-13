s = 1.9
# optimum s = 1.79 to 2.3 
h = 3.3*s

##########################################
import os
for filename in os.listdir(os.getcwd()):
	f1 = open(filename, "r")

x_min = float("inf")
x_max = -float("inf")
y_min = float("inf")
y_max = -float("inf")
z_min = float("inf")
z_max = -float("inf")

num = 0
arr = []
for line in f1:
    if(len(line.split()) == 4):
        if(float(line.split()[1]) < x_min):
            x_min = float(line.split()[1])
        if(float(line.split()[1]) > x_max):
            x_max = float(line.split()[1])
        if(float(line.split()[2]) < y_min):
            y_min = float(line.split()[2])
        if(float(line.split()[2]) > y_max):
            y_max = float(line.split()[2])
        if(float(line.split()[3]) < z_min):
            z_min = float(line.split()[3])
        if(float(line.split()[3]) > z_max):
            z_max = float(line.split()[3]) 
        arr.append(line.split())
        num = num + 1
f1.close()

x_min = int(x_min) - 1
x_max = int(x_max) + 1
y_min = int(y_min) - 1
y_max = int(y_max) + 1
z_min = int(z_min) - 1
z_max = int(z_max) + 1
  
#######################################
store = []
def check(i, j, k, box):
    Pass = 0
    ans = []
    num = 0
    for p in range(-3,3,1):
        for q in range(-3,3,1):
            for r in range(-3,3,1):
               I = i + p
               J = j + q
               K = k + r
               if((I, J, K) in box):
                   num = num + len(box[(I, J, K)])
    store.append(num)
    if(num >= 16):
        return True
    else:
        return False

#####################################
box = {}
for a in arr:
    x = int(float(a[1]))
    y = int(float(a[2]))
    z = int(float(a[3]))
    x1 = x 
    y1 = y 
    z1 = z 
    if((x1,y1,z1) not in box):
        box[(x1,y1,z1)] = []
        box_bar = box[(x1,y1,z1)]
        box_bar.append(a)
        box[(x1,y1,z1)] = box_bar
    else:
        box_bar = box[(x1,y1,z1)]
        box_bar.append(a)
        box[(x1,y1,z1)] = box_bar

final = []
for i in range(x_min,x_max):
    for j in range(y_min,y_max):
        for k in range(z_min,z_max):
            if((i,j,k) in box):
               if(check(i,j,k,box)):
                  b = box[(i,j,k)]
                  for inside in b:
                     final.append(inside)

####################################
z_min = float("inf")
z_max = -float("inf")
for point in final:
    if(float(point[3]) > z_max):
        z_max = float(point[3])
    if(float(point[3]) < z_min):
        z_min = float(point[3])

###################################

f3 = open("final.xyz", "w")
f3.write(str(len(final)))
f3.write("\n")
f3.write("ITEM: NUMBER OF ATOMS 50000")
f3.write("\n")

num = 0
for point in final:
   if(float(point[3]) < (z_min + h)):
       num = num + 1

f3 = open("final.xyz", "w")
f3.write(str(num))
f3.write("\n")
f3.write("ITEM: NUMBER OF ATOMS 50000")
f3.write("\n")

for point in final:
    if(float(point[3]) < (z_min + h)):
       f3.write(point[0]+" "+point[1]+" "+point[2]+" "+point[3])
       f3.write("\n")

f3.close()

#################################
