def solution(record):
    answer = []
    entry = {}
    for r in record:
        com = r.split(" ")

        if com[0] == "Enter" or com[0] == "Change":
            entry[com[1]] = com[2]

    for r in record:
        com = r.split(" ")

        if com[0] == "Enter":
            answer.append(entry[com[1]]+"님이 들어왔습니다.")
        elif com[0] == "Leave":
            answer.append(entry[com[1]]+"님이 나갔습니다.")

    return answer
