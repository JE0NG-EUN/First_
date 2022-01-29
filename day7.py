

#1.
with open("test.txt",'w') as f:
    f.write('Life is too short')
with open("test.txt",'r') as f:
    lines = f.readline()
    print(lines)

#2. 
with open("test.txt",'w') as f:
    f.write('Life is too short\n you need java')

with open("test.txt",'r') as f:
    b = f.read()
    b = b.replace("java", "python")

with open("test.txt",'w') as f:
    f.write(b)


# 3. 
def d(n):
    a = n + sum(map(int, str(n)))
    return a
x = set()
for i in range(0,5001):
    x.add(d(i))
y = set()
for j in range(0,5001):
    if j not in x:
        y.add(j)
print(sum(y))

#4. 
# gravity :상자높이 배열
# [7,4,2,0,0,6,0,7,0] : 상자 높이
gravity=[7,4,2,0,0,6,0,7,0]
# 최대 낙차:7

#고민중입니다..


# 5. 회문
# 출력예시)
# 입력? abba
# 회문입니다

x = input("입력 :" )
a=list(x)
b = list(reversed(x))
if a==b:
    print("회문입니다.")
else :
    print("회문이아닙니다.")
내용을 입력하세요.
흰 배경흰 배경회색 가로줄 배경회색 가로줄 배경어두운 배경어두운 배경
삭제삭제

