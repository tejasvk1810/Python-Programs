#add two matrices

#python proggram to add two matrices
#in this program, you'ii learn to add two matrices using nested loop & next  list comprenhsion & display it

#matrices addition  through nested loop

x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1],[6,7,3],[4,5,7]]
result=[[0,0,0],[0,0,0],[0,0,0]]
 #iterate through row
for i in range(len(x)):
  #iterate through columns
  for j in range(len(x[0])):
    result[i][j]=x[i][j] + y[i][j]

for r in result:
  print(r)


#matrix addition how by using the nested list comprehsion:
x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1],[6,7,3],[4,5,7]]
result=[[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
for r in result:
  print(r)


