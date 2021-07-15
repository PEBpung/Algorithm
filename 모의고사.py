def solution(answers):
    pattern1 = [1, 2, 3, 4, 5] 
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    
    for i, answer in enumerate(answers):
        # 비교해서 맞은 개수를 카운트한다. 
        if answer == pattern1[i % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[i % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[i % len(pattern3)]:
            score[2] += 1
    
    # 가장 높은 점수를 받은 사람을 출력한다.
    answer = [i + 1 for i in range(3) if score[i] == max(score)]
    return answer

answers = list(map(int,input().split()))
print(answers)
print(solution(answers))