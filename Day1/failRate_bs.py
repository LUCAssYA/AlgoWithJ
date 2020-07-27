def failrate(N, stages):
    stageing = []
    stagearrived = []
    for i in range(N):
        stageing.append(0)
        stagearrived.append(0)

    for i in stages:
        if i < N + 1:
            stageing[i - 1] += 1
            for j in range(i):
                stagearrived[j] += 1
        elif i == N + 1:
            for j in range(N):
                stagearrived[j] += 1

    stagerate = {}
    for i in range(N):
        if stagearrived[i] != 0:
            stagerate[i+1] = stageing[i]/stagearrived[i]
        else:
            stagerate[i+1] = 0

    sortedrate = dict(sorted(stagerate.items(), reverse=True, key=lambda x: x[1]))
    answer = list(sortedrate.keys())
    return answer

print(failrate(8, [1,2,3,4,5,6,7]))