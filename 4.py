from random import choice

f = open('students.csv', encoding='UTF-8')
data_base = [x.strip().split(',') for x in f.readlines()[1:]]
f.close()
f = open('students_password.csv', 'w', encoding='UTF-8')


def login_gen(data:list):
    fio = data[1].split()
    login = f'{fio[0]}_{fio[1][0]}{fio[2][0]}'
    return login


def password_gen():
    check1 = 'abcdefghijklmnopqrstuvwxyz'
    check2 = 'abcdefghijklmnopqrstuvwxyz'.upper()
    check3 = '123456789'
    while True:
        password = ''
        for i in range(8):
            password += choice('abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.upper() + '123456789')
        if any([x in check1 for x in password]) and any([x in check2 for x in password]) and any(
                [x in check3 for x in password]):
            return password


for data in data_base:
    login = login_gen(data)
    password = password_gen()
    f.write(','.join(data + [login, password]) + '\n')
f.close()
