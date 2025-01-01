'''
#average

kor = float(input("국어 점수를 입력하세요 :"))
eng = float(input("영어 점수를 입력하세요 :"))
math = float(input("수학 점수를 입력하세요 :"))

print("당신의 평균 점수는", '%0.2f' % float((kor+eng+math)/3), "점 입니다.") 
'''
'''
#odd or even numbers

num=int(input("숫자를 입력하세요 :"))
if (num%2==0):
    print("짝수입니다.")
elif (num%2!=0):
    print("홀수입니다.")
'''
'''
#personal id numbers

pin = "881120-1068234"
yymmdd = pin[:6]
num = pin[7:]
print(yymmdd)
print(num)
'''
'''
#male or female?

pin = (input("주민등록번호를 입력해주세요(******-*******) :"))
if (pin[7]=='1' or pin[7]=='3'):
    print("남자입니다.")
elif(pin[7]=='2' or pin[7]=='4'):
    print("여자입니다.")
'''
'''
#replace : to #

a="a:b:c:d"
b=a.replace(':', '#')
print(b)
'''
'''
#sort list
a=[1, 3, 5, 4, 2]
print("a=", a)
a.sort()
print("after sort=", a)
a.reverse()
print("after reverse=", a)
'''
