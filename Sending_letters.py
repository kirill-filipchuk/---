def send_email(message, recipient, sender=("university.help@gmail.com")):

    if sender == recipient:
        print("Невозможно отправить письмо самому себе")
    elif "@" not in recipient or not recipient.endswith(
            (".com", ".ru", ".net")) or "@" not in sender or not sender.endswith((".com", ".ru", ".net")):

    #elif "@" not in recipient or not (recipient.endswith(".com"), recipient.endswith(".ru"), recipient.endswith(".net")):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif sender == ("university.help@gmail.com"):
        print(f"Письмо успешно отправленно {sender} на адрес {recipient}")

    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')
