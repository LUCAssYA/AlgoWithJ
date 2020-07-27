from itertools import combinations

'''
DFS/BFS (깊이/너비 우선 탐색) 문제
n개의 음이 아닌 정수를 더하거나 빼서 타겟 넘버 구하기
사용할 수 있는 숫자 담긴 배열 numbers, 타겟 넘버 target
타겟 넘버를 만드는 방법의 수 구하기.
주어진 숫자의 개수는 2개 이상 20개 이하, 각 숫자는 1이상 50이하 자연수, 타겟넘버는 1이상 1000이하
'''


def add_minus_to_list(numbers, minus_num):
    result_list = []
    index_list = []
    for i in range(len(numbers)):
        index_list.append(i)
    minus_index = list(combinations(index_list, minus_num))
    print(minus_index)
    for i in range(len(minus_index)):
        temp_list = numbers.copy()
        for j in minus_index[i]:
            temp_list[j] *= -1
        result_list.append(temp_list)
    return result_list

def target_number(numbers, target):
    answer = 0
    minus_count = 0
    while minus_count <= len(numbers):
        for tempList in add_minus_to_list(numbers, minus_count):
            list_sum = sum(tempList)
            if list_sum == target:
                answer += 1
        minus_count += 1
    return answer


print(target_number([1, 1, 1, 1, 1], 3))
