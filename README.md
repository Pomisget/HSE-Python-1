### [Python 1](http://wiki.cs.hse.ru/Основы_и_методология_программирования_на_ПМИ_2018/2019_(основной_поток,_1_модуль))

0. - [ ] [PEP 8 - Style Guide for Python Code] (https://github.com/doroteo7/HSE-Python-1/blob/master/notes/0.md)
1. - [ ] [Intro](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/1.md)
2. - [ ] [Условный оператор](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/2.md)
3. - [ ] [Цикл While](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/3.md)
4. - [ ] [Строки](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/4.md)
5. - [ ] [Функция](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/5.md)
6. - [ ] [Цикл for](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/6.md)
7. - [ ] [Списки - List](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/7.md)
8. - [ ] [Сортировка](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/8.md)
9. - [ ] [Множество - Set](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/9.md)
10. - [ ] [Словарь - Dictionary](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/10.md)
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
