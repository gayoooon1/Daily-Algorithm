score_list = [list(map(int, input().split())) for i in range(5)]
sum_score = [sum(score_list[i]) for i in range(5)]
for i in range(5):
    if sum_score[i] == max(sum_score): 
        print(i+1, sum_score[i])
        break