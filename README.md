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
- [x] [Функциональное программирование](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/11.md)
- [x] [Класс](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/12.md)
- [x] [Пример](https://github.com/Loglosss/HSE-Python-1/blob/master/notes/main.py)






#### Чтение файла построчно в Python

```python

# Method 1. Читать файл построчно
infile = open('input.txt', 'r', encoding='utf-8')

data = infile.readlines()
print(type(data), data)
for row in data:
    a = list(row.split())
    print(a)

infile.close()

# Method 2.
infile = open('input.txt', 'r', encoding='utf-8')

data = infile.read()
print(type(data), data)

infile.close()

# Method 3. 
import sys
data = sys.stdin.read()
# Command + D or Ctrl + D - для завершение чтение данных
print(type(data), data)

# Method 4
import sys
data = sys.stdin.readlines()  # построчно
print(type(data))
# Command + D or Ctrl + D - для завершение чтение данных
print(data)
```
