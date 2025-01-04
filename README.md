## cPanel 2FA Bypass and auto shell uploader (Free Version)

**Contact:** [@xnabob](https://t.me/xnabob)

**Channel:** [Karma Syndicate](https://t.me/KarmaSyndicate)

## Description:

This script is a hacking tool designed for bypassing Two-Factor Authentication (2FA) in cPanel accounts and uploading malicious files (commonly known as "shells") to compromise the server. Here's what it does:

## General Overview:
1. **Target List Processing:**
	+ Reads a list of cPanel credentials from a file. Each line in the file is expected to contain:
	``<cPanel_url>|<username>|<password>``

2. **File Upload & Verification:**
	+ Attempts to upload a file to each target using 2FA bypass.
	+ If the file is uploaded successfully, it constructs the URL for the uploaded file and sends an HTTP GET request to verify the file's presence.

**Key Takeaways:**

+ The script targets websites with vulnerable cPanel accounts.
+ It automates the process of uploading malicious files and checking if the exploit is successful.

**Ethical Concerns:**

+ This script is illegal to use without explicit permission from the target system owner. Misuse of such tools is a violation of ethical and legal standards. 
+ It is important to use such knowledge responsibly, such as in penetration testing under authorized conditions.

## POV:

![POC](https://raw.githubusercontent.com/cpkarma/img/refs/heads/main/2fa-bypass/pov.jpg)
