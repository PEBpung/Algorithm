try:
    print('h, b, c, s 순으로 입력 하시오.')
    h, b, c, s = map(int, input().split())
    if h > 48000 or b > 32 or c > 5 or s > 6000:
        raise IOError
except ValueError:
    print('숫자를 입력하세요')
except IOError:
    print('숫자가 너무 큽니다.')
else: 
    val = h * b * c * s
    print(str(round(val / (8 * 1024 * 1024), 1)) + ' MB')