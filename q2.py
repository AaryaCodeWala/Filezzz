n = int(input("Enter a number to create a spiral : "))
square = []
for i in range (n):
        square.append([0]*n)
        
k =1
u=0
r=n
d=n
l=0

while k <= (n**2):
  for i in range (l,r):
    if square[u][i] == 0:
     square[u][i] = k
     k+=1
  u+=1
    
    
  for i in range (u,d):
     if square[i][r-1] == 0:
         square[i][r-1] = k
         k+=1
  r-=1

  for i in range (r-1,l-1,-1):
     if square[d-1][i] == 0:
         square[d-1][i] = k
         k+=1
  d-=1

  for i in range (d-1,u-1,-1):
     if square[i][l] == 0:
         square[i][l] = k
         k+=1
  l+=1
 
for i in range (len(square)):
  for j in range (len(square[i])):
    print(square[i][j],end=" ")
  print("\n")
        
         
 

    


        
        
