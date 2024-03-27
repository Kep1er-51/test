a = open('students.csv', encoding='UTF-8').readlines()
a = [x[:-1].split(',') for x in a[1:]]
for x in a:
    if x[-1] == 'None':
        x[-1] = 0
    else:
        x[-1] = int(x[-1])

for i in range(1, len(a)):
    value=a[i][-1]
    info=a[i]
    j=i-1
    while a[j][-1]<value and j >=0:
        a[j+1]=a[j]
        j-=1
    a[j+1]=info

k=0
print('10 класс')
for x in a:
    if '10' in x[3]:
        k+=1
        name = x[1].split()[:-1]
        print(f'{k} место: {f'{name[-1][0]}. {name[0]}'}')

