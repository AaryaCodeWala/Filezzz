n = input("Enter numbers as a string for ex: '123456789'  :")
k = []
for i in range (len(n)):
    s = int(n[i])
    k.append(s)
target= int(input("Enter target"))
listz = []
for i in range (len(k)):
     x = target - (k[i])
     for j in range (i+1,len(k)):
         if k[j] == x and i!=j:
             listz.append({k[j],k[i]})

print(listz)
             
             
             
         

        
