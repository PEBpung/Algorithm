
def solution(strings, n):
    strings.sort()
    strings = sorted(strings.sort(), key = lambda x: x[n])
    return strings


'''
def solution(strings, n):
    strings = sorted(strings)
    
    for i in range(len(strings)):
        for k in range(len(strings)-1, i, -1):
            pred = strings[k-1]
            head = strings[k]
            if pred[n] > head[n]:
                strings[k-1], strings[k] = strings[k], strings[k-1]
    return strings
'''