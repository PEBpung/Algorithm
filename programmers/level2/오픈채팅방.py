'''
https://programmers.co.kr/learn/courses/30/lessons/42888

record	
"Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"	

result
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
'''


def solution(records):
    answer, log, user_list = [], [], {}
    printer = ['님이 나갔습니다.', '님이 들어왔습니다.']
    
    for record in records:
        arg, *other = record.split()
        user = other[0]

        if arg == 'Leave':
            log.append((0, user))
        else:
            if arg == 'Enter':
                log.append((1, user))
            user_list[user] = other[1]
    
    for l in log:
        i, user = l
        answer.append(user_list[user] + printer[i])
        
    return answer

records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
result = solution(records)
print(result)