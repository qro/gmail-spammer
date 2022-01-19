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