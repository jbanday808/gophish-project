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

2. Modify the **admin_server** and **phish_server** sections to make Gophish accessible from your network:

**NOTE:** You can download the **config.json** file from the GitHub repository. This configuration ensures that both the admin and phishing servers are accessible from any network interface, with the admin server using TLS for secure connections. The database is configured to use SQLite, and logging settings are defined for capturing system logs. 

3. **Start Gophish by running the following command in the terminal:** sudo ./gophish

4. **Accessing the Gophish Admin Interface:**
   - Open a web browser and navigate to https://0.0.0.0:3333 or https://<Your-Kali-Linux-IP>:3333

5. Logging In:

   - Username: admin
   - Password:  0f564e8fxd9171d25

**If You Cannot Log In or Forgot Your Password**:

1. Generate a new password hash:

   - **Create a Python script generate_hash.py**:

      import bcrypt

      password = b"your_new_password"
      hashed = bcrypt.hashpw(password, bcrypt.gensalt())
      print(hashed.decode())

     - **Run the script**: python3 generate_hash.py
     - Copy the generated hash.
    
2. **Update the Gophish database**: 

- **Open the Gophish database using SQLite**: sqlite3 gophish.db
- **Update the password for the admin user**: UPDATE users SET hash = 'your_generated_hash' WHERE username = 'admin';
- **Exit SQLite**: .exit

**Creating a Phishing Campaign**:

1. **Create a New Landing Page**:
   
   - Navigate to **Landing Pages** and click **New Page**.
   - **Name**: Google Home Page
   - **URL**: https://www[.]google[.]com
   - Enable **Capture Submitted Data** and **Capture Passwords**.
   - **Redirect to**: https://www[.]bmc[.]com/forms/communities-contact-us[.]html
   - Click **Save Page**.

2. **Create a New Email Template**:

   - Navigate to **Email Templates** and click** New Template**.
   - **Name**: BMC Remedy Password Expiry Notification
   - **Subject**: Action Required: Your Password is About to Expire

**NOTE:** You can download the **HTML Content - password_expiry_template.html** file from the GitHub repository.

3. **Create a New Sending Profile**:

   - Navigate to **Sending Profiles** and click **New Profile**.
   - **Name**: James
   - **Interface Type**: SMTP
   - Fill in the SMTP server details, using your email provider’s SMTP settings.

4. **Create a New Group**:

   - Navigate to **Users & Groups** and click **New Group**.
   - **Name**: Test Group
   - **Add Users**: Add email addresses of the users you want to include in the campaign.


