#!/usr/local/bin/wolframscript -script
(* ::Package:: *)

scriptdir = DirectoryName[ExpandFileName[First[$ScriptCommandLine]]];

Print["Calculation of contact angles :\n"]

(*UsingFrontEnd[SetDirectory[NotebookDirectory[]]];*) (* uncomment when using front end *)

SetDirectory[scriptdir]
onlyxyz=Pick[FileNames[],StringMatchQ[FileNames[],"PART*.xyz"]];
filemax=Length[onlyxyz];

Print["Number of samples = ",filemax,"\n"]

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
dot[filenum]={normal[filenum][[1]],normal[filenum][[2]],0};
unknown[filenum]=Table[pointsc[filenum][[i]],{i,1,lp[filenum]}];
tabledot[filenum]=Table[pointsc[filenum][[1]].normal[filenum],{i,1,lp[filenum]}];
sum[filenum]=Total[tabledot[filenum]];

lenofvec=1.2;
vector[p_,v_]:=Graphics3D[{Arrowheads[Small],Arrow[{p,lenofvec*(v+p)}]},AxesLabel->{"x","y","z"},Boxed->True,AspectRatio->1];
g3dv[filenum]=vector[centroid[filenum],normal[filenum]];

contactangle[filenum]=N[(ArcCos[Dot[{0,0,1},normal[filenum]]/Norm[{0,0,1}]/Norm[normal[filenum]]])/\[Degree]];
Close[strInp]];
centroids=Table[centroid[filenum],{filenum,1,filemax}];
pointss=Table[points[filenum],{filenum,1,filemax}];

(* uncomment when using front end *)
(*
r=70;
g3dp=Graphics3D[{Red,Point[centroids]},PlotRange->{{-r ,r },{-r ,r },{-r ,r }},AxesLabel->{"x","y","z"},Boxed->True,AspectRatio->1];
lp3d=ListPlot3D[pointss,PlotRange->{{-r ,r },{-r ,r },{-r ,r }},AxesLabel->{"x","y","z"},Boxed->True,AspectRatio->1];
g3dvall=Table[g3dv[filenum],{filenum,1,filemax}];
graphics=Show[lp3d,g3dp,g3dvall,AxesLabel->{"x","y","z"},Boxed->True,AspectRatio->1];
Export["graphics.jpg",graphics,ImageResolution->500]*)

tableangle=Table[contactangle[filenum],{filenum,1,filemax}];
meancontactangle=Mean[tableangle];
stddeviation=StandardDeviation[tableangle];
Print["samples of contact angles :\n\n",tableangle,"\n"];
Print["Standard deviation of contact angle = ",stddeviation,"\[Degree]\n"];
Print["Mean value of contact angle = (",meancontactangle," \[PlusMinus] ",stddeviation,")\[Degree]\n"];

(* uncomment for checking *)
(*Graphics3D[{Black,Point[Flatten[pointss,1]]},PlotRange->{{-r ,r },{-r ,r },{-r ,r }},AxesLabel->{"x","y","z"},Boxed->True,AspectRatio->1]*)


