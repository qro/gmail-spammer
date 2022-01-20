<p align="center">
	<a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/python-3.10.2+-3776AB">
     </a>
     <a href="https://github.com/qro/gmail-spammer/blob/master/LICENSE">
    	<img src="https://img.shields.io/badge/License-GPL 3.0-3776AB">
     </a>
</p>

<h1 align="center">
	<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/2560px-Gmail_icon_%282020%29.svg.png" width="150px"><br>
    📥 Gmail Spammer - a SMTP listener daemon for spamming. 📥
</h1>
<p align="center">
    Simple email sender with a spam function using smtplib.
 </p>

## 🛠️ Installation
[Python](https://www.python.org/downloads/) must be installed on your computer; please get the most recent version.

### Windows 🪟
If you're running Windows, you can [download](https://codeload.github.com/qro/gmail-spammer/zip/refs/heads/master) the .zip file directly from GitHub. In this case, you can still use [Git](https://github.com/git-for-windows/git/releases) to clone my repository. 

Extract the Zip file and then open your command prompt in the same directory
```
$ py main.py
```

### Linux 🐧
If you're running Linux, clone my repository into your own directory by using this command
```
$ sudo apt install git
$ git clone https://github.com/qro/gmail-spammer.git
$ cd gmail-spammer
```
From there,
```
$ python3 main.py
```

## ℹ️ Information
- If your Gmail account continues to return a `SMTPAuthenticationError`, enable less secure app access (https://myaccount.google.com/lesssecureapps). However, this puts your Gmail account at risk, and I am not responsible for any actions you undertake within your account.
- This project is based on gmail.com, so other email sites won't take emails being sent as "spam" and sent straight to an ignored folder. If you want to use a different email to spam with, just change the SMTP server on lines 22 & 35 with the correct port.
- If you need any support, pm my [telegram](https://t.me/afqro).

---
###### This project here has been made for educational purposes only. I do not control the misconduct of my tool. I do not promote the usage of my tool.
---