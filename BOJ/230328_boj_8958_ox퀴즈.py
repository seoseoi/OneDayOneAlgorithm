# cnt와 score의 분리, 따로 세기

n_test = int(input())

answer = []
for n in range(n_test):
    test = input()

    score = 0
    cnt = 0

    for i in test:
        if i == 'O':
            score += 1
            score += cnt
            cnt += 1
        else:
            cnt = 0

    answer.append(score)

for ans in answer:
    print(ans)