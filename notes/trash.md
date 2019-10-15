```python
file = open('input.txt')

votes = dict()
idx = 0
total = 0

for row in file.readlines():
    a = row.split()

    name = ' '.join(a[:-1])
    vote = int(a[-1])

    if name not in votes:
        votes[name] = [idx, 0]
    votes[name] = [votes[name][0], votes[name][1] + vote]

    total += vote
    idx += 1

a = []
availible = 450

for name in votes:
    x = 450 * votes[name][1] / total
    # name, целая часть, часть от деления, id
    a.append([name, int(x), x - int(x), votes[name][0]])
    availible -= int(x)

# by (-часть от деления, целая часть)
a.sort(key=lambda x: (-x[2], x[1]))

for i in range(len(a)):
    if availible == 0:
        break
    a[i][1] += 1
    availible -= 1

# by id
a.sort(key=lambda x: x[3])

for i in range(len(a)):
    print(a[i][0], a[i][1])

```
