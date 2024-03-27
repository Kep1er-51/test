a = list(open('students.csv', encoding='UTF-8').readlines())
a = [x[:-1].split(',') for x in a[1:]]
for x in a:
    if x[1] == 'Хадаров Владимир Валериевич':
        print(f'Ты получил: {x[-1]}, за проект - {x[2]}')

f = open('students_new.csv', 'w', encoding='UTF-8')
f.write('id,Name,titleProject_id,class,score\n')
average_mark = {}
for x in a:
    if x[-1]!='None':
        if x[-2] not in average_mark:
            average_mark[x[-2]] = [int(x[-1])]
        else:
            average_mark[x[-2]]+= [int(x[-1])]
for x in average_mark:
    average_mark[x] = str(round(sum(average_mark[x])/len(average_mark[x]), 3))
for x in a:
    if x[-1] == 'None':
        x[-1] = average_mark[x[-2]]

for x in a:
    f.write(','.join(x)+'\n')