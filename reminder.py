# https://myaccount.google.com/lesssecureapps 
import datetime as dt
from datetime import datetime
import time , smtplib
def send_email(have):
    email_user = 'lukesoliman1@gmail.com' # email here
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, 'XXXXX') # pass here or read from input
    message = """\
Subject: Get ur stuff!
\nThings u need to get :
\
"""+ '\n'.join(have)
    server.sendmail(email_user, email_user, message)
    server.quit()
items = ["jacket", "water bottle", "phone", "wallet", "school computer", "backpack", "headphone"] # items to notify
have = [] # list of current items
print("(yes/no)")
[have.append(item) for item in items if (input("Do you have your "+item+"? : ").upper() == "YES")]
send = input("What time do you want to be notified (hh:mm) : ").split(":")
print('waiting to send email ...')
curr = [int(numeric_string) for numeric_string in datetime.now().strftime('%Y-%m-%d').split("-")]
send_time = dt.datetime(curr[0],curr[1],curr[2],int(send[0]),int(send[1]),0)
time.sleep(send_time.timestamp() - time.time())
send_email(have)
print('email sent.')
