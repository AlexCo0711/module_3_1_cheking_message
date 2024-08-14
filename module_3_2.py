# Домашняя работа по уроку "Способы вызова функции"

# Создание функции проверки рассылки писем
def send_email(message, recipient, *, sender='university.help@gmail.com'):
    # создание списка проверки правильности email
    mail = [recipient, sender]
    # цикл проверки списка mail установленным правилам (@, .com, .ru, .net)
    for i in mail:
        if i.find('@') != -1 and (i.find('.com', len(i) - 4) != -1 or i.find('.ru', len(i) - 3) != -1 or i.find('.net',
                                                                                                                len(i) - 4) != -1):
            adr = True  # email согласно правил
            continue
        else:
            adr = False  # email не по правилам
            break
    if adr == False:  # условие неправильного email
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif 'university.help@gmail.com' == sender != recipient:  # условие правильного email
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:  # условие равенства email jnghfdbntkz b gjkexfntkz
        print('Нельзя отправить письмо самому себе!')
    else:  # в случае когда email отправителя не соответствует шаблону
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
# дополнительная проверка отправка самому себе с адреса согласно шаблона отправителя
send_email('Напоминаю самому себе', 'university.help@gmail.com')