f = open('students.csv', encoding='UTF-8')
data_base = [x.strip().split(',') for x in f.readlines()[1:]]
f.close()
f = open('students_with_hash.csv', 'w', encoding='UTF-8')


def hesh_gen(data: list):
    p = 67
    m = 10 ** 9 + 9
    alphabet: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper() + ' '
    fio = data[1]
    fio_hesh = [alphabet.index(x) + 1 for x in fio]
    hesh = 0
    for i in range(len(fio_hesh)):
        hesh += (fio_hesh[i] * p ** i) % m
    return hesh


for data in data_base:
    data[0] =  str(hesh_gen(data))
    f.write(','.join(data) + '\n')
f.close()
