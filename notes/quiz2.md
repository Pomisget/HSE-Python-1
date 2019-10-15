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
