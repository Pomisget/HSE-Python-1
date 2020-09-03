### [Python](http://wiki.cs.hse.ru/Основы_и_методология_программирования_на_ПМИ_2018/2019_(основной_поток,_1_модуль))

* [Download book/lectures](https://disk.yandex.ru/i/BkcKilJkumcPV)
* [Online lectures](https://www.coursera.org/learn/python-osnovy-programmirovaniya/home/welcome)

0. - [x] [PEP 8 - Руководство по стилю для кода Python](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/0.md)
1. - [x] [Введение](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/1.md)
2. - [x] [Условный оператор](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/2.md)
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
