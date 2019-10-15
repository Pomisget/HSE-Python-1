### Quiz 2 :thought_balloon:

* __B. Ханойские башни__ [Solution](https://www.youtube.com/watch?v=rFuQCd4RvI0)
<p align="center">
  <img width="400" height="200" src="http://alexandrsoldatkin.com/c-hanoi-tower/images/towershanoi.jpg">
</p>

```python
def move(n, a, b):
    if n <= 0:
        return None
    move(n - 1, a, 6 - a - b)
    print(n, a, b)
    move(n - 1, 6 - a - b, b)

n = int(input())

a = 1

if n % 2 == 0:
    b = 3
else:
    b = 2

for k in range(n, 0, -1):
    move(k, a, b)
    if k % 2 == 1:
        a = 2
        b = 3
    else:
        a = 3
        b = 2
```
* __F. Жизнь в квадрате__

```python
import copy

n, t = list(map(int, input().split()))

a = []
for i in range(n):
    a.append(list(map(int, input().split())))


def inSqare(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False


def count(i, j):
    c = 0
    for x in range(-1, 2, 1):  # -1 0 1
        for y in range(-1, 2, 1):  # -1 0 1
            if x == 0 and y == 0:
                continue
            if inSqare(i + x, j + y) and a[i + x][j + y] == 1:
                c += 1
    return c


def next():
    b = copy.deepcopy(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                if 2 <= count(i, j) <= 3:
                    b[i][j] = 1
                else:
                    b[i][j] = 0
            else:
                if count(i, j) == 3:
                    b[i][j] = 1
    return b


for i in range(t):
    a = next()

for i in range(n):
    print(*a[i])
```
