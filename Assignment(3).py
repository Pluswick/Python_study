'''
#first in, first out
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
'''
'''
#sum mul of 3s in range of 1 to 1000
result=0
i=1
while i <=1000:
    if i%3==0:
        result += i
    i+=1

print(result)
'''
'''
#break stars
i=0
while True:
    i+=1
    if i>5: break
    print("*"*i)
'''
'''
#print 1 to 100 with for
for i in range(1, 101):
    print(i)
'''
'''
#class average
A=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total=0
for score in A:
    total += score
average = total/len(A)
print(average)
'''
'''
#express with list comprehension
"""
numbers = [1, 2, 3, 4, 5]

result=[]
for n in numbers:
    if n%2==1:
        result.append(n*2)
print(result)
"""
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2==1]
print(result)
'''
