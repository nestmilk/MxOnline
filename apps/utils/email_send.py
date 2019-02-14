# _*_ coding: utf-8 _*_
from random import Random

from django.core.mail import send_mail, EmailMessage

from MxOnline.settings import EMAIL_FROM
from users.models import EmailVerifyRecord

__author__ = 'nestmilk'
__date__ = '2019/1/17 17:21'

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length =len(chars)-1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "慕学在线网注册激活链接"
        email_body = "请点击下面的链接激活您的账号：http://127.0.0.1:8000/active/{0}".format(code)
        # send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        msg = EmailMessage(email_title, email_body, EMAIL_FROM, [email])
        msg.attach_file("D:/dog.png")
        send_status = msg.send()
        return send_status

    elif send_type == "forget":
        email_title = "慕学在线网注册密码重置链接"
        email_body = "请点解下面的链接重置密码：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        return send_status
