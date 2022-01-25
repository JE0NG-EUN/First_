
#1. a 리스트에서 중복 숫자를 제거해 보자.

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

print(list(set(a)))


#2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수이면서 7의 배수인수의 합을 구해 보자.

a=0

sum=0

while a<1000:

if a%3 == 0 and a%7 ==0:

sum = sum+a

a+=1

print(sum)


#3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

#(1)

a=''

while a<'*****':

a=a+'*'

print(a)


#(2)

a=''

while a<'*****':

a=a+'*'

print(a.rjust(6))


#(3)

a='*'

print(a.center(9))

while a<'*********':

a=a+'**'

print(a.center(9))


#4.for문을 사용해 1부터 100까지의 숫자를 출력해 보자.

for a in range(1,101):

print(a)


#4-1.(adv)

#for문을 사용해 2부터 100까지의 숫자 중에서 소수를(prime number) 출력해 보자.

#*소수란? 1과 자기 자신으로만 나누어 떨어지는 수(ex. 2, 3, 5, 7, 11, 13,...)

for a in range(2,101):

num = 0

for b in range(1,a+1):

if a%b == 0:

num +=1

if num == 2:

print(a)


#5. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

#[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

#for문을 사용하여 A 학급의 평균 점수를 구해 보자.

a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

a_sum = 0

for b in a:

a_sum = a_sum + b

print(a_sum / len(a))


#6. 로또 당첨 번호 제작(adv) *주의:중복된 수 나오면 안됨

import random

x = random.sample(range(1,46), 6)

print(x)


#7. 자판기

coffe=10

a = 300

while coffe:

x = int(input("돈을 넣어주세요 : "))

if x<a:

print("돈이 부족합니다.")

elif x==a:

print("커피를 줍니다.")

coffe = coffe-1

print(f"남은 커피의 양은 {coffe} 입니다.")

else :

b = x-300

print(f"커피를 줍니다. 거스름돈:{b}")

coffe = coffe - 1

print(f"남은 커피의 양은 {coffe} 입니다.")

if coffe==0:

print("커피가 없습니다.")

﻿
