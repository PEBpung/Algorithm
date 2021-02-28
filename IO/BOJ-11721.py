s = input()
s_len = len(s)
len_list = []

# 10 단위로 list에 저장
for i in range(10, s_len, 10):
    len_list.append(i)

# 마지막에 문자열의 길이 저장
len_list.append(s_len)

# 문자열을 10개씩 끊어서 출력
for i, v in enumerate(len_list):
    print(s[i*10:v])