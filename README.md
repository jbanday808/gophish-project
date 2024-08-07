**Instructions for Gophish Phishing Simulation Project:**

This project demonstrates how to set up and deploy a phishing simulation using Gophish on Kali Linux and AWS. The aim is to create a realistic phishing campaign to test organizational security awareness.

**Prerequisites:**

- Kali Linux installed
- AWS account
- Basic knowledge of Linux commands and AWS services

**Installation Steps**:

1. **Download Gophish:**

   wget https://github.com/gophish/gophish/releases/download/v0.11.0/gophish-v0.11.0-linux-64bit.zip

2. **Extract the file:**

   unzip gophish-v0.11.0-linux-64bit.zip -d gophish
  
3. **Navigate to the Gophish directory**:

   cd gophish

**Configure Gophish:**

1. **Open config.json:**  vi config.json

2. **Modify the admin_server and phish_server sections to make Gophish accessible from your network:**

**NOTE:** You can download the config.json file from the GitHub repository. This configuration ensures that both the admin and phishing servers are accessible from any network interface, with the admin server using TLS for secure connections. The database is configured to use SQLite, and logging settings are defined for capturing system logs. 

3. **Start Gophish:** sudo ./gophish

4. 
