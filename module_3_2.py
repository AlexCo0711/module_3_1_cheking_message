# Домашняя работа по уроку "Способы вызова функции"

# Создание функции проверки рассылки писем
def send_email(message, recipient, *, sen='university.help@gmail.com'):
# создание списка проверки правильности email
    mail = [rec, sen]
# цикл проверки списка mail установленным правилам
    for i in mail:
        if i.find('@') != -1 and (i.find('.com', len(i) - 4) != -1 or i.find('.ru', len(i) - 3) != -1 or i.find('.net',len(i) - 4) != -1):
            adr = True  # email согласно правил
            continue
        else:
            adr = False # email не по правилам
            break
    if adr == False: # условие неправильного email
        print('Невозможно отправить письмо с адреса', sen, 'на адрес', rec, f'.')
    elif 'university.help@gmail.com' == sen != rec: # условие правильного email
        print('Письмо успешно отправлено с адреса', sen, 'на адрес', rec, f'.')
    elif sen == rec: # условие равенства email jnghfdbntkz b gjkexfntkz
        print('Нельзя отправить письмо самому себе!')
    else: # в случае когда email отправителя не соответствует шаблону
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sen, 'на адрес', rec, f'.')
    return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sen='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sen='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sen='urban.teacher@mail.ru')