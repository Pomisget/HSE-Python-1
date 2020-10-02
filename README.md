### [Python](http://wiki.cs.hse.ru/Основы_и_методология_программирования_на_ПМИ_2020/2021_(основной_поток))


* [Download book/lectures](https://disk.yandex.ru/i/BkcKilJkumcPV)
* [Online lectures](https://www.coursera.org/learn/python-osnovy-programmirovaniya/home/welcome)

#### Week 1
- [x] [PEP 8 - Руководство по стилю для кода Python](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/0.md)
- [x] [Введение](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/1.md)
- [x] [Условный оператор](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/2.md)

#### Week 2
- [x] [Цикл While](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/3.md)
- [x] [Строки](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/4.md)
- [ ] [Задачи](https://github.com/Loglosss/HSE-Python-1/blob/master/notes/task2.md) 

#### Week 3
- [x] [Цикл for](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/6.md)
- [x] [Функция и рекурсия](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/5.md)
- [x] [Задачи](https://github.com/Loglosss/HSE-Python-1/blob/master/notes/task3.md) 

#### Week 4
- [x] [Списки - List](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/7.md)
- [x] [Сортировка](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/8.md)
- [x] [Задачи](https://github.com/Loglosss/HSE-Python-1/blob/master/notes/task4.md) 

#### Week 5
- [x] [Разбор КР1](https://github.com/Loglosss/HSE-Python-1/blob/master/notes/quiz_1_2020.md)
- [x] [Множество - Set](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/9.md)
- [x] [Словарь - Dictionary](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/10.md)
- [ ] [Задачи](https://github.com/Loglosss/HSE-Python-1/blob/master/notes/task5.md)

#### Week 6
- [ ] [Функциональное программирование](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/11.md)
- [ ] [Класс](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/12.md)






#### Чтение файла построчно в Python

```python
infile = open('input.txt')

data = infile.readlines()

for row in data:
    a = list(row.split())

infile.close()
```
