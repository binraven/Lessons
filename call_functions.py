"Способы вызова функции"

def send_email(message, recipient, *, sender  = "university.help@gmail.com"):
    if recipient == sender:
        return print("Нельзя отправить письмо самому себе!")
    if ("@" in sender):
        if (".com" in sender) or (".ru" in sender) or (".net" in sender):
            if sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.\n")
            else:
                print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.\n")
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.\n")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.\n")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


