import smtplib, ssl
from email.mime.text import MIMEText

# 以下にGmailの設定を書き込む★ --- (*1)
gmail_account = "devkimadore1228@gmail.com"
gmail_password = ""
# メールの送信先★ --- (*2)
mail_to = "devkimadore1228@gmail.com"

# メールデータ(MIME)の作成 --- (*3)
subject = "メール送信テスト"
body = "メール送信テスト"
msg = MIMEText(body, "html")
msg["Subject"] = subject
msg["To"] = mail_to
msg["From"] = gmail_account
print(msg)

# Gmailに接続 --- (*4)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
    context=ssl.create_default_context())
context = ssl.create_default_context()
print(context)
server.login(gmail_account, gmail_password)
server.send_message(msg) # メールの送信
print("ok.")