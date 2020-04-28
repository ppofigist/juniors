import smtplib

url = 'smtp.yandex.ru'
user = 'aldushchenkovns@yandex.ru'
password = '6Y+MDj!7/,KrCik'

def checker(email):
    '''Проверәет почту на кооректностғ'''
    if '@' in email and '.' in email:
        return True
    return False

conn = smtplib.SMTP_SSL(host=url, port=465)
conn.login(user, password)
print('Введите тему')
mail = input()
print('Сколько людей вы хотите оповестить?')
n = int(input())
for i in range(1, n + 1):
    print('Введите адрес получателя', i)
    to_addr = input()
    if checker(to_addr):
        print('Введите своё сообщение')
        body = input()
        msg = f'From: {user}\nTo: {to_addr}\nSubject: {mail}\n\n{body}v'
        conn.sendmail(user, to_addr, msg)
    else:
        print('Проверьте корректность ввода данных')
print(msg)

#This is a test letter, it does not need to be answered