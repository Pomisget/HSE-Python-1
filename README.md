1. - [x] [Intro](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/1.md)
2. - [x] [Условный оператор](https://github.com/doroteo7/HSE-Python-1/blob/master/2.md)
3. - [x] [Цикл While](https://github.com/doroteo7/HSE-Python-1/blob/master/3.md)
4. - [x] [Цикл While](https://github.com/doroteo7/HSE-Python-1/blob/master/4.md)
5. - [x] [Функция](https://github.com/doroteo7/HSE-Python-1/blob/master/5.md)
6. - [x] [Цикл for](https://github.com/doroteo7/HSE-Python-1/blob/master/6.md)
7. - [x] [Списки - List](https://github.com/doroteo7/HSE-Python-1/blob/master/7.md)
8. - [x] [Сортировка](https://github.com/doroteo7/HSE-Python-1/blob/master/8.md)
9. - [x] [Множество - Set](https://github.com/doroteo7/HSE-Python-1/blob/master/9.md)
10. - [x] [Словарь - Dictionary](https://github.com/doroteo7/HSE-Python-1/blob/master/10.md)

#### Чтение файла построчно в Python

```python
infile = open('input.txt')

data = infile.readlines()

for row in data:
    a = list(row.split())

infile.close()
```
