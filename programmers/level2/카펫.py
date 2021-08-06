def solution(brown, yellow):
    answer = []
    sum = brown + yellow
	# brown보다 가로길이가 작다는 건 확실
    for x in range(1, brown + 1): 
        # sum / x = 세로 길이는 정수여야 함
        if(sum % x == 0): 
        # x를 구하고자 하는 가로길이, y를 세로길이라고 할 때, 
        # yellow = (x-2)(y-2), y = sum/x 이므로, yellow = (x-2)(sum/x-2)
            if(brown == 2 * x + 2 * (sum / x) - 4): 
                answer = [x, sum / x]
    return answer