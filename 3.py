a = open('students.csv', encoding='UTF-8').readlines()
a = [x[:-1].strip().split(',') for x in a[1:]]
proj = ''
while True:
    proj = input('Ввод: ')
    if proj == 'стоп':
        break
    for x in a:
        if x[2]==proj:
            f, i, o = x[1].split()
            name = f'{i[0]}. {f}'
            print(f'Вывод: Проект № {x[2]} делал: {name} он(а) получил(а) оценку - {x[-1]})')
            break
    else:
        print('Вывод: Ничего не найдено')