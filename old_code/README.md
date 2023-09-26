# Job Achiever Master

## How to create Word doc in Python
### 1. [How to install Microsoft fonts in Linux office suites](https://www.pcworld.com/article/431001/how-to-install-microsoft-fonts-in-linux-office-suites.html)
### 2. Install python-docs with **pip install python-docx**  
    IMPORTANT: while python-docx is focused on working with Microsoft Word documents and uses the Office Open XML (OOXML) format, specifically the .docx file format, there is a similar library called *unotools* designed to work with LibreOffice/OpenOffice documents which uses the Open Document Format (ODF).
### 3. [python-docx documentation](https://python-docx.readthedocs.io/en/latest/)  






## Cover letter bot

The bot takes the User info from the candidate.json file and the job info from the job.json file. It then creates
a cover letter using all the information. Once the cover letter is generated, the user has the option to edit the generated text
via the tkinter module. When you close the tkinter window, the program then automatically saves the Cover letter as pdf, a new tkinter
window appears where the user can choose the path to save the pdf file.

---

## Cv_bot

The bot takes all necessary the User info like private info, education, previous xp. and etc. from the 'candidate.json' file which is in the json folder. Then it generates a CV.pdf file using all the information. Also you are able to upload your photo with popup window. The name of the CV generates as '<name>_<surname>_<CV>.pdf' Once the CV is generated, the bot saves it to the pdfs folder. 

---

## Email module

In this code we are going to use a **gmail** account, but the concepts apply to any other email server provider.

### 1. Create and log into a gmail account
- create a throwaway gmail account (to be used for testing)
- log in the new account
- go to the setting page of your [google account](https://www.myaccount.google.com)

### 2. Allow the 2-Steps Veriication
- click on "Security" (on the left)
- Scroll to the section "Signing in to Google"
- click on "2-Steps Verification"
- follow the instructions on the screen

### 3. Create an app password
- go to the link fro creating an [app password](https://myaccount.google.com/u/4/apppasswords)
- click on the first dropdown menu ("select app")
- Select "Other (Custom name)"
- choose a name (for example "Python")
- click on "Generate"
- copy the 16 character app password in the yellow box  
**IMPORTANT**: This is the **one and only time** you will be able to see this, so copy and paste it in a separate and safe location.

### 4. Import the necessary libraries  
- **SMTP**  
  A class of the module smtplib (Simple Mail Transfer Protocol LIBrary), it takes care of conecting to the server and sending the email.
- **MIMEMultipart**  
  A subclass of MIMEBase, this class represents the outer container of an email message and allows to combine different components ("multipart"), such as sender and receiver address, subject, body and attachments into a single email message.
- **MIMEApplication**  
  A subclass of MIMENonMultipart, this class is used to represent MIME message objects of major type application. The _data  argument contains the bytes for the raw application data while the optional _subtype specifies the MIME subtype.
- **MIMEText**  
  A subclass of MIMENonMultipart, the MIMEText class is used to create **MIME** (**M**ultipurpose **I**nternet **M**ail **E**xtension) objects of major type text.

### 5. Create the class **Email**
  - ### 5.1 define the **class attributes**
    Write an assignment statement for the port.  
    (**587** is the the standard secure mail submission port)

  - ### 5.2 Instatiate the class instance
    The class Email has the following attributes:  
    - sender
    - list of receivers
    - email subject
    - name of the server  
      (defaulted for the gmail)  

  - ### 5.3 Define **password** method
    This method uses a "with" statement and the "open" function in "r" (read) mode to access the file where the app password is stored, recover it, return to the main funcion and closing the file at the end of its scope.
  
  - ### 5.3 Define **attachments** method
    - loop through a copy of the list of documents
    - open the file containing the document.  
      **NB**: using the "**binary**" ("rb") mode instead of the simple "read" ("r") allows us to open files others than text, such as pdf or images
    - read the file and use its data to create an instance of the general-purpose class "**MIME application**", which rappresent an attachment in an email message.
    - use the **.add_header()** method to add the "Content-Disposition" header, which indicates the file should be treated as an attachment, to the attachment object
    - remove the string name of the document from the original list and substitute it with the attachment object.
    - return the new list of documents  

  - ### 5.3 Define **send** method
    - 5.3.1 Connect to the server  
      - Use a "with" statement to be sure the server will be close once we finish to send all the emails  
      - Create an object of the class SMTP, which allows the connection to the serveer using the proper server's name and standard secure SMTP port number  
      - Use the .strarttls() method to encrypt the connection
      - Use the .login() method to log into the email account with the sender address and its password.
    - 5.3.2 "Build" and send the email
      - loop through the list of the receivers
      - create an instance of the class **MIMEMultipart()**, which is like a box contaiing all the different components of the email
      - Set each needed element inside the container:
        - sender's address 
        - receiver's address
        - email subject
        - body of the email, creating an instance of the class **MIMEText** and attaching it throught the .attach() method
        - attachment(s), looping through the list of files to be attached and using the .attach() method
      - Finally, use the smtp **.send_message()** method to send the MIMEMultipart() object, which rapresent the email with all its different components.

### References:
- Python docs:  
  - [**smtplib** module](https://docs.python.org/3/library/smtplib.html#module-smtplib)
  - [**email.mime** module](https://docs.python.org/3/library/email.mime.html?highlight=email#email.mime.multipart.MIMEMultipart)
- Port number details [**"Which SMTP port should I use?"**](https://www.mailgun.com/blog/email/which-smtp-port-understanding-ports-25-465-587/)
---

 

## References


- [**E-mail regex** link](https://uibakery.io/regex-library/email-regex-python)

