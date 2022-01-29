#1. "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
# 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된
# 알파벳 점수의 총합을 for 문 -> map 함수와 람다식을 이용해 구하십시오.

x = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
#for 사용
a=0
b=[]
for i in range(0,len(x)):
    if x[i] == 'A':
        a = 4
    elif x[i] == 'B':
        a = 3
    elif x[i] == 'C':
        a = 2
    else:
        a = 1
    i+=1
    b.append(a)
print(sum(b))

#map,lamdba사용
print(sum(list(map(lambda a:4 if a=='A' else(3 if a=='B' else(2 if a=='C' else 1)), x))))

#2. 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.
#lit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x**2, lit)))

#3. 다음(카카오) 입사문제
# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# (단 점들의 배열은 모두 정렬되어있다고 가정한다.)
# 예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
S={1, 3, 4, 8, 13, 17, 20}
S=list(S)
S.sort()
print(S)
b = len(S)
c = []
for i in range(0,b-1):
    a = abs(S[i] - S[i+1])
    c = c+list(map(int, str(a)))
d = list(c)
e = min(c)
print(d)
f = int(d.index(e))
print(S[f],S[f+1])

# 4. 평균값 구하기
# 다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 평균 값을
# result.txt 파일에 쓰는 프로그램을 작성하시오.
#
with open("sample.txt",'w') as f:
    f.write("70\n60\n55\n75\n95\n90\n80\n80\n85\n100")
c=0
with open("sample.txt",'r') as f:
    b = (f.read()).split("\n")
    print(b)
for i in b:
    a = int(i)
    c= c+a
d = c/len(b)
print("총합 :",c)
print("평균값 :",d)

with open("sample.txt",'w') as f:
    f.write(str(d))

# 5. ngram 기반 두 문장 유사도 구하기(n=2, 3)
# "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다."
# "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다."
#
# 1) n=2, n은 글자 수
# "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다." =>['오늘','늘 ' ,' 멀', '멀티', ... '다.']
# "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다." => ['멀티','티캠', ... '다.']
# l1=['오늘','늘 ' ,' 멀', '멀티', ... '다.']
# l2=['멀티','티캠', ... '다.']
# l1과 l2의 유사도? (l1과 l2의 중복 단어) / (l1과 l2에 있는 중복을 제외한 모든 단어의 개수)   ex)   6 /10 => 60%유사도

a1 = "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다."
a2 = "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다."
l1 = []
l2 = []
for i in range(len(a1)):
    l1.append(a1[i:i+2])
for i in range(len(a2)):
    l2.append(a2[i:i+2])
b=len(l1)+len(l2)  #l1과 l2 모든 개수 : 29+31=60
l3 = []
l4 = []
for i in l1:
    if i not in l2:
        l3.append(i)

for i in l2:
    if i not in l1:
        l4.append(i)

c = len(l3)+len(l4) #l1과 l2에 있는 중복을 제외한 모든 개수 :7+9 = 16
d = (b-c)/2 #중복된 개수
print((100*(d/(c+d))),"%")

# 2) n=3
# l1=['오늘 ', '늘 멀', ..., '했다.']
# l2=['멀티캠', '티캠퍼', ..., 웠다.']
# l1과 l2의 유사도? ( l1과 l2의 중복 단어)
# (l1과 l2에 있는 중복을 제외한 모든 단어의 개수)   ex)   4 /10 => 40%유사도

for i in range(len(a1)):
    l1.append(a1[i:i+3])
for i in range(len(a2)):
    l2.append(a2[i:i+3])
b=len(l1)+len(l2) #l1과 l2 모든 개수 : 29+31=60

for i in l1:
    if i not in l2:
        l3.append(i)

for i in l2:
    if i not in l1:
        l4.append(i)

c = len(l3)+len(l4) #l1과 l2에 있는 중복을 제외한 모든 개수 :12+14 = 26
d = (b-c)/2 #중복된 개수
print((100*(d/(c+d))),"%")
