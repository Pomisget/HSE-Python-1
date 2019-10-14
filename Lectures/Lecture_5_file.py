infile = open('input.txt', 'r', encoding='utf8')
outfile = open('output.txt', 'w', encoding='utf8')

data = infile.readlines()

for row in data:
    a = list(row.split())

infile.close()
outfile.close()
