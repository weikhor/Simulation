#! /bin/bash

##Make Sure that the cu-water-1.lammpstraj, cut.py, ##profiling.py, divide.py, store.py, visualisevector.wls, ##meanangle.wls and standarddeviation.wls are in the same ##working directory 
#############################################################
#rm -rf nohup.out
rm -rf *xyz
rm -rf samplemean.txt
rm -rf samplemeanvalue.dat
rm -rf stddeviationvalue.dat
rm -fr data*

python cut.py

echo files with XYZ format :
echo $(ls -art *xyz)

listf=($(ls -art *xyz))
count=0

for i in "${listf[@]}"; 
do 
echo processing "$i";

let count=$count+1;
mkdir "data"$count;
cp $i $(pwd)/"data"$count;
cd "data"$count;
python ../profiling.py
rm $i
python ../divide.py
python ../store.py

#rm final.xyz
#rm -fr part*.xyz
#rm store.xyz

echo Sample mean $count >> ../samplemean.txt
#echo $'\n' >> ../samplemean.txt
printf "\n" >> ../samplemean.txt

cp ../visualisevector.wls .
wolframscript -script visualisevector.wls >> ../samplemean.txt
rm visualisevector.wls
cat ../samplemean.txt
cp ../meanangle.wls .
wolframscript -script meanangle.wls >> ../samplemeanvalue.dat
rm meanangle.wls
cp ../standarddeviation.wls .
wolframscript -script standarddeviation.wls >> ../stddeviationvalue.dat
rm standarddeviation.wls

#cat ../samplemean.txt

cd ..

done



