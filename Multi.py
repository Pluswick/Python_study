n,k = (input().split())
n=int(n)
k=int(k)

for i in range (1,10):
    
    if(i <= k):
        print(n, " * ", i ," = ", n * i)
    else:
        break
