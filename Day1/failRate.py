def failrate(n, stages):
    stageing = []
    stagearrived = []
    for i in range(n):
        stageing.append(0)
        stagearrived.append(0)

    for i in stages:
        if i < n + 1:
            stageing[i - 1] += 1
            for j in range(i):
                stagearrived[j] += 1
        elif i == n + 1:
            for j in range(n):
                stagearrived[j] += 1

    stagerate = {}
    for i in range(n):
        stagerate[i+1] = stageing[i]/stagearrived[i]

    sortedrate = dict(sorted(stagerate.items(), reverse=True, key=lambda x: x[1]))
    answer = list(sortedrate.keys())
    return answer
