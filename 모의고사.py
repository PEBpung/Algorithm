import numpy as np

def solution(answers):
    answer = []
    supo = [[1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    pred = []
    score = []
    
    for i in range(len(supo)):
        iter = []
        # 문제 정답의 크기와 예측 정답 크기를 맞춘다.
        for k in range(len(answers)):
            iter.append(supo[i][k%len(supo[i])])
        pred.append(iter)
        # 정답과 예측을 비교해본다.
        result = np.array(answers) - np.array(pred[i])
        # 비교한 값에서 맞은 개수(0)을 카운트한다. 
        score.append(result.tolist().count(0))
    
    # 가장 높은 점수를 받은 사람을 출력한다.
    for idx,s  in enumerate(score):
        if s == max(score):
            answer.append(idx+1)
    
    return answer