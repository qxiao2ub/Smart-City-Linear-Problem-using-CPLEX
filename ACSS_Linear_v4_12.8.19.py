#pandas is for using reading functions
import pandas as pd

#numpy for n-dimensional array obj
import numpy as np

#read original test data test 1 period 0,2,5,8 (others btw 0-8 are same), separated with ' '
d1p0=[[float(i) for i in line.strip().split(' ')] for line in open('Test Data_Data1_Period0.txt').readlines()]
d1p2=[[float(i) for i in line.strip().split(' ')] for line in open('Test Data_Data1_Period2.txt').readlines()]
d1p5=[[float(i) for i in line.strip().split(' ')] for line in open('Test Data_Data1_Period5.txt').readlines()]
d1p8=[[float(i) for i in line.strip().split(' ')] for line in open('Test Data_Data1_Period8.txt').readlines()]

#assign dijt-(i=4,j=4,t=4), total 20 od pairs only use 4 for i and 4 for j
#total 40 time periods but now only use 4 periods
d = np.zeros((4,4,4), dtype = np.float )

#assign read dijt to list
for i in range (0,4):
  for j in range (0,4):
    d[i,j,0] = d1p0[i][j]
    d[i,j,1] = d1p2[i][j]
    d[i,j,2] = d1p5[i][j]
    d[i,j,3] = d1p8[i][j]

#test dijt assign correctly
print("Print demand input:") 
print(d[0,0,0],d[3,3,0])
print(d[0,0,1],d[3,3,1])
print(d[0,0,2],d[3,3,2])
print(d[0,0,3],d[3,3,3])

#step1-assign parameters (i=j=t=4) - set subjectively
#1.1-assign Pijt as parameter
P = np.zeros((4,4,4), dtype = np.int )

#Pijt reference
#P[0,0,0]=10
#P[0,0,1]=2
#P[0,1,0]=3 
#P[0,1,1]=4
#P[1,0,0]=9
#P[1,0,1]=5
#P[1,1,0]=9
#P[1,1,1]=6

#set P_ori is sequence 10,2,3,4,9,5,9,6 and repeat totally generate 64 numbers
P_ori = [10,2,3,4,9,5,9,6,10,2,3,4,9,5,9,6,10,2,3,4,9,5,9,6,10,2,3,4,9,5,9,6,
         10,2,3,4,9,5,9,6,10,2,3,4,9,5,9,6,10,2,3,4,9,5,9,6,10,2,3,4,9,5,9,6]

#pointer to read P_ori
k = 0

for i in range (0,4):
  for j in range (0,4):
    for t in range (0,4):
      #Price is 10 times as P_ori just to guarantee positive
      P[i,j,t] = P_ori[k] * 10
      k=k+1

#test Pijt
print ('Test pricing Pijt:', P[0,0,0], P[0,1,0], P[3,3,3])

#1.2-assign cijt as parameter
c = np.zeros((4,4,4), dtype = np.int)

c_ori = [78,3,10,39,43,10,19,2,78,3,10,39,43,10,19,2,78,3,10,39,43,10,19,2,78,3,10,39,43,10,19,2,
         78,3,10,39,43,10,19,2,78,3,10,39,43,10,19,2,78,3,10,39,43,10,19,2,78,3,10,39,43,10,19,2]

#cijt reference
#c[0,0,0]=78
#c[0,0,1]=3
#c[0,1,0]=10
#c[0,1,1]=39
#c[1,0,0]=43
#c[1,0,1]=10
#c[1,1,0]=19
#c[1,1,1]=2

#pointer to read c_ori
k = 0

for i in range (0,4):
  for j in range (0,4):
    for t in range (0,4):
      c[i,j,t] = c_ori[k]
      k=k+1

#test cijt
print ('Test cijt:', c[0,0,0], c[0,1,0], c[3,3,3])

#1.3-assign pijt (penalty) as parameter, use P_ori but 0.5 times it as penalty

p = np.zeros((4,4,4), dtype = np.int)

#pointer to read P_ori
k = 0

for i in range (0,4):
  for j in range (0,4):
    for t in range (0,4):
      #Price is 0.5 times as P_ori to make penalty small
      p[i,j,t] = P_ori[k] * 0.5
      k=k+1

#test pijt
print ('Test pijt:', p[0,0,0], p[0,1,0], p[3,3,3])

#1.4-#assign inventory cost hit
h = np.zeros((4,4), dtype = np.int )

#reference for hit
#h[0,0]=3
#h[0,1]=8
#h[1,0]=3 
#h[1,1]=10

h_ori = [3,8,3,10,3,8,3,10,3,8,3,10,3,8,3,10]

#pointer to read h_ori
k = 0

for i in range (0,4):
  for t in range (0,4):
    h[i,t] = h_ori[k]
    k=k+1

#test hit
print ('Test hit:', h[0,0], h[0,0], h[3,3])