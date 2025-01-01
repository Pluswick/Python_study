year=int(input("연도를 입력하세요: "))

if (year%4==0) and (year%100!=0):
    print(1)
elif (year%400==0):
    print(1)
else:
    print(0)
