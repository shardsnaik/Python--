import smtplib as sm

ob = sm.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('email.addres', 'pass')
sub = 'twst'
body= 'usbxc wsxcwscb '
message ='subject :{}\n\n{}'.formate(sub, body)
listadress = ['To_user_email_1', 'To_user_email_2']
ob.sendmail('From_email.adress', listadress, message) 
print('send mail')
ob.quit()