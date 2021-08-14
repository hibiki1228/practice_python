import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders

# 以下にGmailの設定を書き込む★ --- (*1)
gmail_account = "devkimadore1228@gmail.com"
gmail_password = ""
# メールの送信先 --- (*2)
mail_to = "devkimadore1228@gmail.com"
# 添付ファイルのパス(ZIPファイルで指定) --- (*3)
file_path = "./test.zip"

# メールデータ(MIME)の作成 --- (*4)
subject = "添付ファイル送信テスト"
body = "添付ファイルの送信テスト"
encoding = 'utf-8'
msg = MIMEMultipart()
msg["Subject"] = Header(subject, encoding)
msg["To"] = mail_to
msg["From"] = gmail_account
msg.attach(MIMEText(body, 'plain', encoding))

# 添付ファイル(ZIP)をメールに追加 --- (*5)
attach = MIMEBase('application','zip')
with open(file_path, "br") as f:
    attach.set_payload(f.read())
encoders.encode_base64(attach)
attach.add_header('Content-Disposition', 'attachment',
    filename='attachment.zip')
msg.attach(attach)

# Gmailに接続 --- (*6)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
    context=ssl.create_default_context())
server.login(gmail_account, gmail_password)
server.send_message(msg) # メールの送信
server.quit()
print("ok.")