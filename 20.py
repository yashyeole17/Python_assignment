#Q.20) write a python program to add two matrices

m1=[[1,2,3],
     [4,5,6],
     [7,8,9]]

m2=[[9,8,7],
    [6,5,4],
     [3,2,1]]

add=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(m1)):
  for j in range(len(m1[0])):
    add[i][j]=m1[i][j]+m2[i][j]

for r in add:
  print(r)
