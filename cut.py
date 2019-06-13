filename = "cu-water-1.lammpstrj"
total = 400
"""count from last frame"""
###################################
f = open(filename, "r")
count = 0
num = 0
num_atom = 0
final_step = 0
i = 0
for line in f:
   if(line.split()[0] == "ITEM:" and line.split()[1] == "TIMESTEP"):
      count = count + 1
   if(len(line.split()) == 1 and int(line.split()[0]) > 0):
      num = int(line.split()[0])
   if(len(line.split()) == 8 and (line.split()[3] == "O" or line.split()[3] == "H")):
      num_atom = num_atom + 1
   elif(count == 2):
      f.close()
      break
######################################
step = 0
diff = 0
f = open(filename, "r")
for line in f:
   if(len(line.split()) == 1 and int(line.split()[0]) != num):
      if(diff == 0):
         diff = int(line.split()[0]) - step
      step = int(line.split()[0])
######################################
step = step - total*diff
######################################
f = open(filename, "r")
f1 = open("data1.xyz", "w")
f1.write(str(num_atom))
f1.write("\n")
f1.write("ITEM: NUMBER OF ATOMS " + str(step))
f1.write("\n")

file = 2
s = 0

arr = []

for line in f:
   if(len(line.split()) == 1 and int(line.split()[0]) != num  and int(line.split()[0])>step):
      s = int(line.split()[0])
      
   if(len(line.split()) == 1 and s > step + diff*(total+1)):
      f.close()
      f1.close()
      break
      
   if(s > step):
      if(len(line.split()) == 8 and (line.split()[3] == "O" or line.split()[3] == "H")):
          value1=line.split()[5]
          value2=line.split()[6]
          value3=line.split()[7]
          value1=round(float(value1),4)
          value2=round(float(value2),4)
          value3=round(float(value3),4)
          f1.write(str(1) + " " + str(value1)+ " "+str(value2)+" "+str(value3))
          f1.write("\n")
      if(line.split()[0] == "ITEM:" and line.split()[1] == "TIMESTEP" and s + diff < step + diff*(total+1)):
          f1 = open("data" + str(file) + ".xyz", "w")
          f1.write(str(num_atom))
          f1.write("\n")
          f1.write("ITEM: NUMBER OF ATOMS " + str(step))
          f1.write("\n")
          file = file + 1
##################################################
