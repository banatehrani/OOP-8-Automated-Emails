import yagmail

yagmail.SMTP(user="mehdi.python.developer@gmail.com", password="mehdi_python_developer"). \
    send(to="banatehrani@gmail.com",
         subject="Hi there!",
         contents="Hi, this is the body of the email!\nMehdi",
         attachments="design.txt")
