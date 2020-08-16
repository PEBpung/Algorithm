# 작성 한 코드를 붙여넣어 주세요.
def solution(numbers):
    answer = ''
    # 리스트 원소를 숫자 -> 문자
    numbers = list(map(str, numbers))
    # 가장 큰 수를 만들 수 있는 상태로 정렬
    '''
    문자열의 정렬은 가나다 순 정렬 개념
    원소의 값이 1000이하 이기때문에 일의자리 십의자리, 백의자리까지 비교할 수 있도록 하기 위해서
    lambda x : x*3 을 해 줌
    그렇게하면 2번째 예시에서 34,3,30 순으로 정렬 가능
    '''
    numbers.sort(reverse=True, key = lambda x:x*4)
    # 문자열로 결합
    for i in numbers:
        answer += i
    answer = str(int(answer))
    return answer
