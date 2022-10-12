import smtplib
from datetime import datetime
import email
import imaplib
from email.header import decode_header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def check_list():
    list = []
    with open(r'check_list',encoding='utf-8') as f:
        list = f.read().split('\n')
    return list

def send_result(sender,pwd, receiver, content):
    subject = '每日调度监控'
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ",".join(receiver)
    # ---这是正文部分---
    part = MIMEText(content, "html", "utf-8")
    msg.attach(part)
    server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465, timeout=3000)  # 发件人邮箱中的SMTP服务器，端口是465
    server.login(sender, pwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(sender, receiver, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()


if __name__ == '__main__':
    imapHost = 'imap.exmail.qq.com'
    # UserPwd = input('输入密码：')
    import sys
    UserAdr = sys.argv[1]
    UserPwd = sys.argv[2]
    imapServer = imaplib.IMAP4(imapHost)
    imapServer.login(UserAdr,UserPwd)
    # print(imapServer.list())
    imapServer.select('&UXZO1mWHTvZZOQ-/&jANepiAUIBRiEFKf-')
    rfc_date = datetime.strftime(datetime.now(),'%d-%b-%Y')
    result, data = imapServer.search(None, 'SINCE "{}"'.format(rfc_date))
    check_list = check_list()
    success_list = []

    if result == 'OK':
        for num in data[0].split():
            result, data = imapServer.fetch(num,'(RFC822)')
            if result == 'OK':
                email_message = email.message_from_bytes(data[0][1])
                bytes_sub = decode_header(email_message['Subject'])[0][0]
                sub = bytes_sub.decode('utf-8')
                title = sub.split('-')[0]
                if 'test' not in title and 'release' not in title:
                    if title in check_list:
                        check_list.remove(title)
                        success_list.append(title)

    content = '已成功跑完：'+str(success_list)+'<br><br>'+'未成功跑完：'+str(check_list)
    # print(content)
    send_result(UserAdr,UserPwd,[UserAdr],content)
    print('Success')


