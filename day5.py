#1. 리스트에서 20 보다 작은 3의 배수를 출력하라
a =[13, 21, 12, 14, 30, 18]
i = a[0]
for i in a:
    if i%3 == 0 and i<20:
        print(i)
    else :
        i = a[:i+1]

#2. 리스트에서 세 글자 이상인 단어를 화면에 출력하라
a = ["I", "study", "python", "language", "!"]
for i in a:
    if (len(i)>4):
        print(i)

#3. 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라.
a = ['hello.py', 'ex01.py', 'intro.hwp']
for i in a:
    b = i.split(".")
    print(b[0])

# 4. my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]
print(my_list[0],my_list[1])
print(my_list[1],my_list[2])
print(my_list[2],my_list[3])

#5. 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]

for i in range(1,len(my_list)):
    print(my_list[-i],my_list[-i-1])

#6.리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때,
# low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
i = 0
volatility = []
while i<5:
    x = high_prices[i]-low_prices[i]
    volatility.append(x)
    i = i + 1
print(volatility)

#7.리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
i = 0
while i<3:
    a= apart[i]
    print(a[0],"호")
    print(a[1], "호")
    print("-"*5)
    i+=1
