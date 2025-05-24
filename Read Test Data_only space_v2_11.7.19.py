#pandas is for using reading functions
import pandas as pd

#numpy for n-dimensional array obj
import numpy as np

#read original test data d1p0 & d1p1, separated with ' '
d1p0=[[float(i) for i in line.strip().split(' ')] for line in open('Test Data_Data1_Period0.txt').readlines()]
d1p1=[[float(i) for i in line.strip().split(' ')] for line in open('Test Data_Data1_Period2.txt').readlines()]

#test to print all, 1st and last-pass
#print (o_d)
#print (o_d[0][0])
#print (o_d[19][19])

#assign dijt-(i=20,j=20,t=2) 
d = np.zeros((20,20,2), dtype = np.float )
#test assign o_d to d-pass
#d[0,0,0] = o_d[0][0]
#print (d[0,0,0])

for i in range (0,20):
  for j in range (0,20):
    d[i,j,0] = d1p0[i][j]
    d[i,j,1] = d1p1[i][j]
    
print(d[0,0,0])
print(d[19,19,0])
print('\n')

print(d[0,0,1])
print(d[19,19,1])
    
