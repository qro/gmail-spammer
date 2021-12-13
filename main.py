import os, sys, time, smtplib

os.system('cls & mode 70, 12 & title email spammer │ by lozza (github.com/qro)')
email = input('\n [?] Email: ')
password = input(" [?] Password: ")
victim = input(" [?] Victim: ")
message = input(" [?] Message: ")
number = input(" [?] Amount: ")

class SMTP():
    def __init__(self):
        self.email = email
        self.password = password
        self.victim = victim
        self.message = message
        self.number = number

    def verify(self):

        server1 = smtplib.SMTP("smtp.gmail.com", 587)
        server1.ehlo()
        server1.starttls()

        try:
            server1.login(self.email, self.password)
        except smtplib.SMTPAuthenticationError:
            print('\n [!] The email or password is wrong')
            time.sleep(2)
            exit()

        SMTP().main()

    def main(self):
        if len(sys.argv) < 2:
            os.system('cls')
            sys.stdout.write(f'''
            
        [!] Connected as: {self.email}
        [!] Victim: {self.victim}
        [!] Message: {self.message}  
        [!] Amount: {self.number}
        
        ''')

        option = input('\n [?] Spam email? [y/n]: ')
        if option == 'y':
            SMTP().spam()
            os.system("python main.py")
        if option == 'n':
            os.system("python main.py")
        else:
            print('\n [!] Invalid option')
            time.sleep(0.5)
            SMTP().main()
        
    def spam(self):
        os.system('cls & mode 70, 32 & title email spammer │ by lozza (github.com/qro)')
        server2 = smtplib.SMTP("smtp.gmail.com", 587)
        server2.ehlo()
        server2.starttls()
        server2.login(self.email, self.password)
        i = 0
        while i < self.number:
            i+=1
            server2.sendmail(self.email, self.victim, self.message)
            if i == 1: 
                print((' [>] ''%d Email sent ')%(i))
            else:
                print((' [>] ''%d Emails sent ')%(i))
            sys.stdout.flush()
        print('\n [!] Process finished')
        time.sleep(3)
            
if __name__ == '__main__':
    SMTP().verify()