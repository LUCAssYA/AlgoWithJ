# Day 1 정리

1. 실패율 문제 (2019 KAKAO BLIND RECRUITMENT)

- 알아두면 좋은 풀이 1
```python
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
```
- 알아두면 좋은 풀이2
```python
def solution(N, stages):
    fail = {}
    for i in range(1,N+1):
        try:
            fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i])
        except:
            fail_ = 0
        fail[i]=fail_
    answer = sorted(fail, key=fail.get, reverse=True)
    return answer
```
내 코드에서 적용한 방식

먼저 스테이지 별 실패율을 구한 뒤 이를 Dictionary 로 key 값은 스테이지, value 값은 실패율로 정해 저장한다.

이를 sorted 함수를 통해 Value 로 Reverse Sort 하는 방식

알아두면 좋은 sorted 예제 코드
```python
sorted(result, key = lambda x: x[1], reverse=True)
```

2. 타겟 넘버 (DFS/BFS 문제)

1) DFS (깊이 우선 탐색): 모든 정점을 방문하는 가장 단순하고 고전적인 방법

- 현재 정점과 인접한 간선들을 하나씩 검사하다가, 아직 방문하지 않은 정점으로 향하는 간선이 있다면 그 간선을 무조건 방문
- 이 과정에서 더 이상 방문할 곳이 없다면, 마지막에 방문했던 간선을 따라 뒤로 돌아감.
- 마지막에 방문했던 곳으로 돌아간다는 것은 Stack 과 유사한 동작방식
- 재귀함수가 내부적으로 스택으로 구현되어 있으므로, DFS 의 구현은 재귀함수의 형태로 많이 구현

크게 인접행렬을 이용해 구현하거나, 인접 리스트를 이용해 구현을 한다.

2) BFS (너비 우선 탐색): 시작점에서 가까운 정점부터 방문하는 탐색 알고리즘, 가까운 정점을 모두 저장해놓고 순서대로 방문하므로 큐 구조를 사용

- 큐를 이용해서 지금 위치에서 갈 수 있는 것을 모두 큐에 넣는 방식, 큐에 넣을 때 동시에 방문했다고 체크를 한다.
- 아직 발견되지 않은 상태, 발견되었지만 아직 방문되지는 않은 상태 (이 상태의 정점들은 이미 큐에 저장), 방문된 상태로 나눠짐.
- 큐를 이용해서 구현 (인접 행렬, 인접 리스트를 이용해 구현한다.)

시간 복잡도

인접 행렬: O(V^2), 인접 리스트: O(V+E)

BFS 를 이용한 문제풀이

- BFS 의 목적은 임의의 정점에서 시작해서, 모든 정점을 한번씩 방문
- BFS 는 최단거리를 구하는 알고리즘
- BFS 는 모든 가중치가 1일때, 최단 거리 구하는 알고리즘
- 최소비용문제, 가중치 1, 정점과 간선 개수 적음

- 내 풀이: itertools 에서 combinations 을 통해 -1 의 수를 점차 늘리는 방법

- 알아두면 좋은 풀이 1
```python
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
```

- 알아두면 좋은 풀이 2
```python
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
```

- 알아두면 좋은 풀이 3
```python
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
```