n1 = int(input("Enter a number :"))
n2 = int(input("Enter a number : "))
n3 = int(input("Enter a number : "))
n4 = int(input("Enter a number : "))
n5 = int(input("Enter a number : "))
c=0
d=0

l = [n1,n2,n3,n4,n5]
mx = max(l)
for i in range (1,mx+1):
    c=0
    for j in l:
        if j%i == 0:
            c=c+1
        if c == 5:
            d = i
print(f"The Answer is {d}")

