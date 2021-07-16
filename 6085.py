class MyError(Exception):
    def __str__(self):
        return '입력된 b는 4의 배수가 아닙니다.'

try:
    print('w, h, b 순으로 입력 하시오.')
    w, h, b = map(int, input().split())
    if w > 1024 or h > 1024 or b > 40:
        raise IOError
    if b % 4 != 0:
        raise MyError()

except ValueError:
    print('숫자를 입력하세요')
except IOError:
    print('숫자가 너무 큽니다.')
except MyError as e:
    print(e)

else: 
    val = w * h * b
    print(str(round(val / (8 * 1024 * 1024), 2)) + ' MB')