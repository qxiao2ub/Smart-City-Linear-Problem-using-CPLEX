#pandas is for using reading functions
#import pandas as pd

#numpy for n-dimensional array obj
import numpy as np

#step1-assign parameters (i=j=t=2)
#assign cijt-(i=j=t=2) 
c = np.zeros((2,2,2), dtype = np.int )

c[0,0,0]=78
c[0,0,1]=3
c[0,1,0]=10 
c[0,1,1]=39
c[1,0,0]=43
c[1,0,1]=10
c[1,1,0]=19
c[1,1,1]=2

#test input
print ('Test cijt:', c[0,0,0], c[0,1,1], c[1,1,1])
#print ('\n')

#assign pijt-(i=j=t=2) 
p = np.zeros((2,2,2), dtype = np.int )

p[0,0,0]=10
p[0,0,1]=2
p[0,1,0]=3 
p[0,1,1]=4
p[1,0,0]=9
p[1,0,1]=5
p[1,1,0]=9
p[1,1,1]=6

print ('Test pijt:', p[0,0,0], p[0,1,1], p[1,1,1])
#print ('\n')

#assign hijt-(i=j=t=2) 
h = np.zeros((2,2), dtype = np.int )

h[0,0]=3
h[0,1]=8
h[1,0]=3 
h[1,1]=10

print ('Test hit:', h[0,0], h[1,1])
#print ('\n')

#assign dijt-(i=j=t=2) 
d = np.zeros((2,2,2), dtype = np.int )

d[0,0,0]=78
d[0,0,1]=30
d[0,1,0]=10 
d[0,1,1]=39
d[1,0,0]=43
d[1,0,1]=10
d[1,1,0]=19
d[1,1,1]=20

print ('Test dijt:', d[0,0,0], d[1,1,1])
#print ('\n')

#assign dijt-(i=j=t=2) 
alpha = np.zeros((2,2,2,2), dtype = np.int )

#here set if i!=j, alpha=1
alpha[0,0,0,0]=0
alpha[0,0,0,1]=0
alpha[0,0,1,0]=0 
alpha[0,0,1,1]=0
alpha[0,1,0,0]=1
alpha[0,1,0,1]=1
alpha[0,1,1,0]=1
alpha[0,1,1,1]=1
alpha[1,0,0,0]=1
alpha[1,0,0,1]=1
alpha[1,0,1,0]=1 
alpha[1,0,1,1]=1
alpha[1,1,0,0]=0
alpha[1,1,0,1]=0
alpha[1,1,1,0]=0
alpha[1,1,1,1]=0

print ('Test taoijt:', alpha[0,0,0,0], alpha[1,1,1,1])
print ('\n')

#step 1 - read parameters from csv
#read cijt-cost from csv
#cijt-i,j,t all from 0-1, total 8 numbers, value range [1,100]
#cijt = pd.read_csv('cijt.csv',header=None)
#cijt = cijt.values.tolist()
#print('cijt: ', cijt)
#print(cijt[1][4])
#read pijt-penalty of not satisfying demand from csv
#pijt-i,j,t all from 0-1, total 8 numbers, value range [1,10]
#pijt = pd.read_csv('pijt.csv',header=None)
#pijt = pijt.values.tolist()
#print('pijt: ', pijt)
#read hit-inventory cost from csv
#hit-i,t all from 0-1, value range [1,10]
#hit = pd.read_csv('hit.csv',header=None)
#hit = hit.values.tolist()
#print('hit: ', hit)
#read dijt-demand from csv
#dijt-i,j,t all from 0-1, value range [1,100]
#dijt = pd.read_csv('dijt.csv',header=None)
#dijt = dijt.values.tolist()
#print('dijt: ', dijt)
#read alpha_ijtaot-possible to reach in time t from csv
#alpha_ijtaot-i,j,tao,t, value binary
#alpha_ijtaot = pd.read_csv('alpha-ijtaot.csv',header=None)
#alpha_ijtaot = alpha_ijtaot.values.tolist()
#print('alpha_ijtaot: ', alpha_ijtaot)

#step 2 - initialize model
#python calls cplex
from docplex.mp.model import Model
mdl = Model(name='Zhiheng Linear Model')

#step 3 - define variables
#define 3 types decision variables: Uijt-2*2*2, Xijt-2*2*2, Vit-2*2
#X variables in 3 dimension
X = {(i,j,t): mdl.integer_var(lb=0, name="X[{0}][{1}][{2}]".format(i,j,t)) 
for i in range(0,2) for j in range(0,2) for t in range(0,2) }

U = {(i,j,t): mdl.integer_var(lb=0, name="U[{0}][{1}][{2}]".format(i,j,t)) 
for i in range(0,2) for j in range(0,2) for t in range(0,2) }

V = {(i,t): mdl.integer_var(lb=0, name="V[{0}][{1}]".format(i,t)) 
for i in range(0,2)  for t in range(0,2) }

#idx = [(i, j, k) for i in range(0,2) for j in range(0,2) for k in range(0,2)]
#X = mdl.integer_var_matrix(idx, "X" , lb=0)
#for i in range(0,2):
   # for j in range(0,2):
    #    for t in range(0,2):
   #         #set lower bound 0 for variable
  #          Uijt.append (mdl.integer_var(name="U[{0}][{1}][{2}]".format(i,j,t) , lb=0 ))
 #           Xijt.append (mdl.integer_var(name="X[{0}][{1}][{2}]".format(i,j,t) , lb=0 ))
#Vit=[]
#for i in range(0,2):
#    for t in range(0,2):
#        Vit.append (mdl.integer_var(name="V[{0}][{1}]".format(i,t) , lb=0 ))

#step 4 - setup objective
#moving cost:sum cijt*Xijt
mdl.moving_cost = mdl.sum(c[i,j,t] * X[i,j,t]
 for i in range(0,2) for j in range(0,2) for t in range(0,2) )

#penalty:sum pijt*Uijt
mdl.penalty = mdl.sum( p[i,j,t] * U[i,j,t]
 for i in range(0,2) for j in range(0,2) for t in range(0,2) )

#inventory cost:sum hit*Vit
mdl.inventory_cost = mdl.sum( h[i,t] * V[i,t]
 for i in range(0,2) for t in range(0,2) )

#minimize total cost
mdl.minimize(mdl.moving_cost + mdl.penalty + mdl.inventory_cost)

#mdl.total_moving_cost = mdl.sum(c[i,j,t] * Xijt for i in range(0,2) for j in range(0,2) for t in range(0,2) )    
#mdl.total_moving_cost = mdl.sum(c[i,j,t] * Xijt for i in range(0,2) for j in range(0,2) for t in range(0,2) )    
#mdl.minimize(mdl.total_moving_cost)

#step 5 - constraints
#constr (#2)
#t = 1
for i in range(0,2):
    for j in range(0,2):
        mdl.add_constraint(U[i,j,1] >= U[i,j,0] + d[i,j,1] - X[i,j,1])
          
#U[i,j,t]=0 if i=j
for i in range(0,2):
    for j in range(0,2):
        for t in range (0,2):
          if i == j:
                mdl.add_constraint(U[i,j,t] == 0)

#U[i,j,0] = 0
for i in range(0,2):
    for j in range(0,2):
        mdl.add_constraint(U[i,j,0] == 0)
        #elif i == j:
        
#X[i,j,t]=0 if i=j
#for i in range(0,2):
 #   for j in range(0,2):
  #      for t in range (0,2):
   #         if i == j:
    #            mdl.add_constraint(X[i,j,t] == 0)

#iterative
#for i in range(0,2):
 #   for j in range(0,2):
  #          mdl.add_constraint( U[i,j,1] == U[i,j,0] + d[i,j,1] - X[i,j,1] )
   #        mdl.add_constraint( U[i,j,1] == 0 )
            #break
    #     elif U[i,j,0] + d[i,j,1] - X[i,j,1] >= 0:
     #      mdl.add_constraint( U[i,j,1] == U[i,j,0] + d[i,j,1] - X[i,j,1] )
            #break

#constr (#3)
#for i in range(0,2):
 #   for j in range(0,2):
  #      mdl.add_constraint(X[i][j][0] + X[i][j][0] >= U[i][j][1] )
       
#constr (#4)
#here t = 1, tao = 0
for i in range(0,2):
    mdl.add_constraint( V[i,1] == V[i,0] + mdl.sum( alpha[j,i,0,1] * X[i,j,0]
    for j in range(0,2) ) - mdl.sum( X[i,j,1] for j in range(0,2) ) )

#constr (#5)
# t = 1
mdl.add_constraint(mdl.sum(V[i,0] for i in range(0,2)) == 
                   mdl.sum(V[i,1] for i in range(0,2)))

#step 6 - print information
mdl.print_information()
print('\n')

#step 7 - solve problem
s = mdl.solve()

#step8-solution status details
print(mdl.solve_details)


#mdl.print_solution()
#print('\n')

#step 9 - print solution
from docplex.util.environment import get_environment

if mdl.solve():
    print(mdl.solve_details)
    mdl.print_solution()
    # Save the CPLEX solution as "solution.json" program output
    with get_environment().get_output_stream("solution.json") as fp:
        mdl.solution.export(fp, "json")
else:
    print("Problem has no solution")

print("---------------")   
#To get all variable values
print("Decision Variable Values are:")
print(mdl.solution.get_all_values())

print("---------------")
#To get objective value
print("Optimal Objective Values is:")
print(mdl.solution.get_objective_value())











