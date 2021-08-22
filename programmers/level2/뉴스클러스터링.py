'''
https://programmers.co.kr/learn/courses/30/lessons/17677
'''
'''
sudo 코드
1. 모두 대문자로 변경한다.
2. 두글자 씩 추출한다. (div1, div2)
    방법 1. combination 사용. (모든 경우의 수이기 때문에 X)
    방법 2. strid 2를 사용해서 2개씩 저장
    - O(n^2)의 시간이 걸림
    - 이때 공백, 숫자, 특수 문자가 포함된 문자 제거
    - 중복 되는 걸 숫자로 표시해야 되기 때문에 Counter 함수 적용
3. 교집합과 합집합을 추출한다.
    1. set1 & set2을 사용하면 교집합
    2. set1 | set2을 사용하면 합집합
4. 교집합과 합집합을 나눈다. 
    - 각 원소의 value 값을 합쳐서 나누기
'''
from collections import Counter

def divider(s): 
    # 가독성이 떨어짐
    # [str1[i-2:i] for i in range(2, len(str1)+1) if str1[i-2:i].isalpha()]
    div = []
    for i in range(2, len(s)+1):
        d = s[i-2:i]
        if d.isalpha():
            div.append(d)
    return Counter(div)
    
def solution(str1, str2):
    div1, div2 = [], []
    str1, str2 = str1.upper(), str2.upper()
    div1, div2 = divider(str1), divider(str2)
    inter, union = (div1 & div2), (div1 | div2)
    if sum(union.values()) == 0:
        return 65536
    return int(sum(inter.values())/sum(union.values())*65536)
# 16384
print(solution('FRANCE', 'french'))
# 65536
print(solution('handshake', 'shake hands'))
# 65536
print(solution('E=M*C^2', 'e=m*c^2'))
