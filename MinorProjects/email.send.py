import smtplib as s  #inbuilt already

ob = s.SMTP("smtp.gmail.com",587)   #making an object
#587 :code of gmail for sending

ob.starttls()   #this is a method for sending
ob.login("shivadantare@gmail.com","suwsmgqinyltdbbm")  #first it will login our account
subject= "Sending Email Using Python"  #subject for mail
body="Hello my name is Shiva. How are you doing?"
message ="Subject:{}\n\n{}".format(subject,body)   #keeping subject and body together as a msg
listofaddress=["shivadantare@gmail.com","yogeshdantare@gmail.com"]
ob.sendmail("shivadantare",listofaddress,message)  #defining id from which we want to send mail
print("Sent Successfully")
ob.quit()

# MAIL_MAILER=smtp
# MAIL_HOST=smtp.gmail.com
# MAIL_PORT=587
# MAIL_USERNAME=null
# MAIL_PASSWORD=null
# MAIL_ENCRYPTION=tls

