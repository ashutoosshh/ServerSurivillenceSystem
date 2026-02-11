import smtplib
from email.message import EmailMessage



def Send_Email(sender_email,app_password,recivers_email,subject,body):

    msg=EmailMessage()


    msg["From"]=sender_email
    msg["To"]=recivers_email
    msg["Subject"]=subject


    #add mail body

    msg.set_content(body)

    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)


    smtp.login(sender_email,app_password)

    smtp.send_message(msg)


    smtp.quit()



    



def main():
    sender_email="ashutoshgunjal09@gmail.com"

    app_password="pgpeookqyuystfea"


    recivers_email="ashotosh_gunjal_it@moderncoe.edu.in"

    subject="Test mail for python Script"

    body="Jay ganesh" \
    
    "Regards" \
    "Ashutosh Gunjal"

    Send_Email(sender_email,app_password,recivers_email,subject,body)


    print(" Mail Send Succesfully")


    


if __name__=="__main__":
    main()
