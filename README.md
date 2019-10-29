### Python

1. - [x] [Intro](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/1.md)
2. - [x] [Условный оператор](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/2.md)
3. - [x] [Цикл While](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/3.md)
4. - [x] [Строки](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/4.md)
5. - [x] [Функция](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/5.md)
6. - [x] [Цикл for](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/6.md)
7. - [x] [Списки - List](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/7.md)
8. - [x] [Сортировка](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/8.md)
9. - [x] [Множество - Set](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/9.md)
10. - [x] [Словарь - Dictionary](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/10.md)
11. - [ ] [Функциональное программирование](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/11.md)
12. - [ ] [Класс](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/12.md)




#### Чтение файла построчно в Python

```python
infile = open('input.txt')

data = infile.readlines()

for row in data:
    a = list(row.split())

infile.close()
```
