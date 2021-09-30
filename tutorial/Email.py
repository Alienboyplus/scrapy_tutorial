import smtplib
from email.mime.text import MIMEText

def mail(remains=None):
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # SMTP服务器
    mail_user = "827004264@qq.com"  # 用户名
    mail_pass = "mhkagzwrgkmjbcbb"  # 密码
    # mail_pass = "mhn268251003"

    sender = '827004264@qq.com'  # 发件人邮箱(最好写全, 不然会失败)
    receivers = ['827004264@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    content = '该充值辣!现在还剩'+remains+"元"
    title = '寝室电费充值提醒'  # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
        return
    return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    remains = "12.0"
    mail(remains)


