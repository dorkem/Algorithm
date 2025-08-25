# 눈높이 코딩테스트 챌린지 14기 기본반 b
```aiignore
🗓️ 풀이 기간: 2025.08.11 ~
🍀 개발 언어: Java
```
<img src="https://github.com/user-attachments/assets/c807bc65-ae46-40a2-855c-cb92685d7e82" width="100%" />

<br><br>


## MISSION
|                               미션                                | 문제 유형 | 문제 난이도 |           수행 기간            | 풀이 과정 | 해설지 |
|:---------------------------------------------------------------:|:---:|:---:|:---------------------------:|:-----:|:----:|
|[🃏숫자 카드(OT)](https://www.acmicpc.net/problem/10815)       |`이분탐색`| `S5`| `2025.08.10` | ||
|[🐸폴짝폴짝](https://www.acmicpc.net/problem/1326)       |`BFS/DFS`| `S2`| `2025.08.11` |  [📝GIST](https://gist.github.com/dorkem/590792579e2b459a28ce45ef961f4c29)   | |
|[🗂️섬의 개수](https://www.acmicpc.net/problem/4963)          |`BFS/DFS`| `S2`| `2025.08.12` |  [📝GIST](https://gist.github.com/dorkem/3add04714100f1edd6911b47bb6dde93)   | |
|[🍄버섯 농장](https://www.acmicpc.net/problem/27737)       |`BFS/DFS`| `S1`| `2025.08.13` | | |
|[👀적록색약](https://www.acmicpc.net/problem/4963)          |`BFS/DFS`| `G5`| `2025.08.14` | | |
|[➕1, 2, 3 더하기](https://www.acmicpc.net/problem/9095)          |`DP`| `S3`| `2025.08.15` |  [📝GIST](https://gist.github.com/dorkem/f4d467a74eebfe9145362ff7da719149)   | |
|[⛏️자원 캐기](https://www.acmicpc.net/problem/14430)          |`DP`| `S2`| `2025.08.16` |  [📝GIST](https://gist.github.com/dorkem/e061a089aa83e27a7b202c22509056d6)   | |
|[🎨RGB거리](https://www.acmicpc.net/problem/1149)          |`DP`| `S1`| `2025.08.17` |  [📝GIST](https://gist.github.com/dorkem/44ba11d0afd69e6696e89a126ba03137)   | |
|[🪜내려가기](https://www.acmicpc.net/problem/2096)         |`DP`| `G5`| `2025.08.18` |  [📝GIST](https://gist.github.com/dorkem/fec89a4f3cd48bd23dc3335ddb41d029)   | |
|[🤖로봇](https://www.acmicpc.net/problem/13567)         |`구현`| `S4`| `2025.08.19` |  [📝GIST](https://gist.github.com/dorkem/40b7c4baae280af6c33907f0c4ef7ce5)   | |
|[⚾️숫자 야구](https://www.acmicpc.net/problem/2503)         |`구현`| `S3`| `2025.08.20` |  [📝GIST](https://gist.github.com/dorkem/dc7affcd8679a073794f2b042dffa973)   | |
|[⚪️오목](https://www.acmicpc.net/problem/2615)         |`구현`| `S1`| `2025.08.21` |  [📝GIST](https://gist.github.com/dorkem/fe5ddb3d96f4988b6fc031c58a3a3cd0)   | |
|[🚚트럭](https://www.acmicpc.net/problem/13335)         |`구현`| `S1`| `2025.08.22` |  [📝GIST](https://gist.github.com/dorkem/70b3afe7009adc3bc69bc7257a5ca2a0)   | |
|[🌉어두운 굴다리](https://www.acmicpc.net/problem/17266)  |`이분탐색`| `S4`| `2025.08.23` |     | |
|[🔴선분 위의 점](https://www.acmicpc.net/problem/11663)         |`이분탐색`| `S3`| `2025.08.24` | | |
|[🌳나무 자르기](https://www.acmicpc.net/problem/2805)         |`이분탐색`| `S2`| `2025.08.25` |  [📝GIST](https://gist.github.com/dorkem/70b3afe7009adc3bc69bc7257a5ca2a0)   | |
---

<br><br><br><br><br>

# 문제 풀이 가이드(BoJ숫자카드 문제)

## 📌 문제 탐색하기

<aside>
💡 문제 탐색하기는 어떻게 작성하나요?

우리가 문제를 이해해가는 과정을 작성하시면 됩니다

- 문제에서 구해야 하는 최종 정답은 무엇인지 탐색한 과정
- 그 정답을 구하기 위해 어떻게 코드를 구현해야 할지 고민한 과정
- 문제에 들어오는 범위를 파악하며 어떤 알고리즘을 쓸 수 있을지 고민해 가는 과정

등을 작성해주시면 됩니다.

</aside>

N : 상근이가 가지고 있는 숫자 카드 배열의 크기 

M : 상근이의 숫자카드에 포함되어 있는지 확인해야 하는 숫자들의 크기

총 M개의 숫자들에 대해 크기 N의 배열안에 이 값이 포함되어 있는지 아닌지를 구하는 것이 핵심입니다. 

M은 최대 500,000개이고 N 또한 최대 500,000입니다.

### 가능한 시간복잡도

M번만큼은 무조건 한번씩은 탐색을 해야 합니다. 상근이가 가지고 있는지 아닌지 판별해야 하니까요.

O(M) * x → 일 때 최대 1억개 안의 연산 크기를 만족시켜야 합니다.

x는  N 배열안에 숫자가 포함되어 있는지 확인하는데 걸리는 시간복잡도를 의미합니다.

1. O(M) * O(N) 이라면?
    1. N배열에 대해 0번부터 끝번까지 하나씩 비교하며 탐색하는 케이스이죠.
    2. 총 250000000000번의 연산이 필요해 시간초과가 나게 됩니다.
2. O(M) * O(logN) 이라면?
    1. 총 2,500,000 정도의 연산으로 시간안에 탐색이 가능합니다.

하나의 탐색 당 최대 O(logN)안에 탐색을 해야 시간안에 탐색을 완료할 수 있습니다.

### 알고리즘 선택

탐색 알고리즘 중에 O(LogN)으로 풀 수 있는 이분탐색 알고리즘으로 접근해보겠습니다.

### 이분탐색으로 풀 수 있나?

- 정렬이 되어있는가?
- 정렬할 때 시간복잡도에 들어올 수 있는가?

---

## 📌 코드 설계하기

<aside>
💡 코드 설계하기는 어떻게 작성하나요?

위의 문제 탐색하기에서 고민한 과정을 토대로 문제 풀이에 대한 실마리를 잡으셨을 것 같습니다.
이제 문제 풀이를 본격적으로 하기 전, 이 문제를 풀기 위한 로드맵을 그려보겠습니다.

어떤 순서로 코드를 작성해야 할지,
어떤 함수들을 작성해야 할지 등을 작성해주시면 됩니다.

처음에는 어려울 수 있지만, 문제를 풀기 전 미리 지도를 그린다라는 생각으로 적어나가 보시면 좋을 것 같습니다 :)

</aside>

1. 문제의 Input을 받습니다.
2. 배열 N을 정렬합니다.
3. 이분 탐색을 구현하고, M 배열의 각 원소에 대해 이분 탐색을 진행합니다.

---

## 📌 시도 회차 수정 사항 (Optional)

<aside>
💡 시도별 수정 사항은 어떻게 작성하나요?
- 무문별하게 “맞았습니다”가 나올때 까지 수정하는 형태의 문제 풀이를 반복하면 , 내가 어떤 실수를 해서 해당 문제를 틀렸는지 모르게 됩니다.
- 틀렸습니다를 받았다면 왜 틀렸는지 고민해보고 , 어떻게 수정할 수 있는지 고민하는 과정을 작성해주시면 됩니다.
- 위에 내가 세울 설계에서 어떤 부분이 틀렸는지도 함께 점검해보세요
- 한번에 맞출수도 있기 때문에 이 칸은 Optional입니다.

</aside>

### 1회차

- 이분탐색 수행 시 정렬이 필요함을 깜빡했다. 정렬 과정을 추가했다.

### 2회차

---

## 📌 정답 코드

```python
def binary_search(target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if n_list[mid] == target:
        return mid
    elif n_list[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search(target, start, end)

def solution():
    global n_list
    # 1. get input
    N = int(input())
    n_list = list(map(int, input().split()))
    M = int(input())
    m_list = list(map(int, input().split()))

    # 2. sort n_list
    n_list.sort()

    # 3. do binary search
    for a in m_list:
        res = (binary_search(a, 0, N-1))
        if res >= 0:
            print(1, end=' ')
        else:
            print(0, end=' ')

solution()
```
