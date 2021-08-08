'''
https://programmers.co.kr/learn/courses/30/lessons/42888

record	
"Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"	

result
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
'''


def solution(records):
    answer = []
    user_list = {}

    def enter(user, name):
        answer.append(f'{name}님이 들어왔습니다.')
        user_list[user] = name

    def leave(user):
        answer.append(f'{user_list[user]}님이 나갔습니다.')
        del user_list[user]

    def change(user, name):
        pass

    for record in records:
        arg, *other = record.split()

        if arg == 'Enter':
            enter(other[0], other[1])
        elif arg == 'Leave':
            leave(other[0])
        elif arg == 'Change':
            change(other[0], other[1])
    return answer

records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
result = solution(records)
print(result)