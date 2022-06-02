import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "BridgeLabz Training Invitation"
msg ["From"] = "Training Team"
msg ["To"] = "thakare.santosh1994@gmail.com"
msg.set_content("Test Email From BridgeLabz Team")
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("santoshthakare268@gmail.com",9623500474)
server.send_message(msg)
server.quit()