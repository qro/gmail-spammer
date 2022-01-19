import os, sys, time, json, smtplib

with open('config.json') as f:
    config = json.load(f)
email = config.get('email')
password = config.get('password')