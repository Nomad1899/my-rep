from collections import Counter

# 1. Дан файл  с логинами и паролями. Найдите топ10 самых популярных паролей.


f = open('pwd.txt')
data = f.read()
ar = data.split("\n")
pas = []
for x in ar[1:len(ar) - 1]:
    pas.append(x.split(";")[1])

most_pas = Counter(pas).most_common()[0:10]
for x in most_pas:
    print(f"{most_pas.index(x)+1}. {x[0]} встречается {x[1]} раз")

f.close()
