#load balancing test
import copy


inputs = [4,2,1,3,0,1,0,1]

result = [[1],[2,2],[2,2],[2,2,1],[1,2,1],[2],[2],[1],[1],[0],[15]]

def something():
    outputs = []
    
    time_task, user_max = inputs[:2]
    users = inputs[2:]
    users_copy = copy.deepcopy(users)
    count = 0
    while True:
        for user in users:
            user_per_server = outputs[-1] if outputs else []
            total_user = sum(user_per_server) + user
            new_line = []
            if total_user > user_max: 
                while total_user >= user_max:
                    if total_user >= user_max:
                        new_line.append(user_max)
                    total_user -= user_max
                    if total_user > 0 and total_user < user_max:
                        new_line.append(total_user)
                        total_user = 0

            else:
                if users_copy:
                    new_line.append(total_user)

            if count >= time_task:
                if users_copy:
                    expired = users_copy.pop(0)
                    users_copy.pop(0)
                    new_line[0] -= expired
                    if new_line[0] > 0:
                        new_line.pop(0)
            outputs.append(new_line)
            count += 1
        if not users_copy:
            break
    print(outputs)



if __name__ == "__main__":
    something()
