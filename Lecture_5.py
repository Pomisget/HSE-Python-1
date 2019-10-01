# infile = open('input.txt', 'r', encoding='utf8')
# outfile = open('output.txt', 'w', encoding='utf8')

# data = infile.readlines()

# for row in data:
#     a = list(row.split())

# infile.close()
# outfile.close()


def ByName(student):
    return student[0]

  
a = [('Alex', 9), ('Anna', 7), ('Max', 9), ('Kira', 10)]

a.sort(key=ByName)
print(*a)

a.sort(key=lambda x: x[1])
print(*a)

a.sort(key=lambda x: x[0])
print(*a)
