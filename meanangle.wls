#!/usr/local/bin/wolframscript -script
(* ::Package:: *)

scriptdir = DirectoryName[ExpandFileName[First[$ScriptCommandLine]]];
(*UsingFrontEnd[SetDirectory[NotebookDirectory[]]];*) (* Open comment when use front end *)
SetDirectory[scriptdir]
onlyxyz=Pick[FileNames[],StringMatchQ[FileNames[],"PART*.xyz"]];
filemax=Length[onlyxyz];
For[filenum=1,filenum<= filemax,filenum++,
file=onlyxyz[[filenum]];
strInp=OpenRead[File[file]];
str=ReadLine[strInp];
points[filenum]={};
While[str=!= EndOfFile,
list=StringSplit[str];
len=Length[list];
If[len==4,
x=list[[2]];
y=list[[3]];
z=list[[4]];
points[filenum]=Append[points[filenum],{x,y,z}]];
str=ReadLine[strInp]
;];
points[filenum]=ToExpression[points[filenum]];
lp[filenum]=Length[points[filenum]];
centroid[filenum]=Mean[points[filenum]];
pointsc[filenum]=Table[points[filenum][[i]]-centroid[filenum],{i,1,lp[filenum]}];
pc[i_]:=pointsc[filenum][[i]];
kp[i_]:=KroneckerProduct[pc[i],pc[i]];
Omega=Sum[kp[i],{i,1,lp[filenum]}];
{evalue,evector}=Eigensystem[Omega];
ordering=Ordering[evalue];
evalue[[ordering[[1]]]];
normal[filenum]=evector[[ordering[[1]]]];
contactangle[filenum]=N[ArcCos[Dot[{0,0,1},normal[filenum]]/Norm[{0,0,1}]/Norm[normal[filenum]]]/\[Degree]];
Close[strInp];]
tableangle=Table[contactangle[filenum],{filenum,1,filemax}];
meancontactangle=Mean[tableangle];
Print[meancontactangle]
