### [Python](http://wiki.cs.hse.ru/Основы_и_методология_программирования_на_ПМИ_2018/2019_(основной_поток,_1_модуль))


* [Download book/lectures](https://disk.yandex.ru/i/BkcKilJkumcPV)
* [Online lectures](https://www.coursera.org/learn/python-osnovy-programmirovaniya/home/welcome)

#### Week 1
- [x] [PEP 8 - Руководство по стилю для кода Python](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/0.md)
- [x] [Введение](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/1.md)

#### Week 2
- [x] [Условный оператор](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/2.md)
- [x] [Цикл While](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/3.md)
- [ ] [Задачи](https://github.com/Loglosss/HSE-Python-1/blob/master/notes/task2.md) 

#### Week 3
- [ ] [Строки](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/4.md)
- [ ] [Функция](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/5.md)

#### Week 4
- [ ] [Цикл for](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/6.md)
- [ ] [Списки - List](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/7.md)

#### Week 5
- [ ] [Сортировка](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/8.md)
- [ ] [Множество - Set](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/9.md)

#### Week 6
- [ ] [Словарь - Dictionary](https://github.com/doroteo7/HSE-Python-1/blob/master/notes/10.md)
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
