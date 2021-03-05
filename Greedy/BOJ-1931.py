'''
https://www.acmicpc.net/problem/1931

너무 복잡하게 생각해서 어려웠던 문제,, 결국 블로그 참고해서 작성했다.
sorted(key=)를 요긴하게 사용하면 코드의 효율이 좋아진다. 
'''

def greedy(meeting):
    count = 0
    start = 0
    for v in meeting:
        if v[0] >= start:
            start = v[1]
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    meeting = []

    for i in range(n):
        s, e = map(int, input().split())
        meeting.append((s, e))

    meeting = sorted(meeting, key=lambda x: x[0])
    meeting = sorted(meeting, key=lambda x: x[1])

    count = greedy(meeting)
    print(count)
    