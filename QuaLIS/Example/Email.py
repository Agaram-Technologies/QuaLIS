
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl

from Utility import BasicOperation

mail = MIMEMultipart()
mail['From'] = 'murali.r@agaramtech.com'
mail['To'] = 'murali.r@agaramtech.com'
mail['CC'] = 'murali.r@agaramtech.com'
mail['Subject'] = 'TestCase Report'
content = """
I have attached the testcase report for your referce
"""
mail.attach(MIMEText(content, 'plain'))
filepath = BasicOperation.projectDirectory()+"\\Report.pdf"
fileinbinary = open(filepath, "rb")
payload = MIMEBase("application", "octate-stream")
payload.set_payload(fileinbinary.read())
encoders.encode_base64(payload)
mail.attach(payload)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls(context=ssl.create_default_context())
server.login("murali.r@agaramtech.com", "IndianArmy@1995")
server.sendmail("murali.r@agaramtech.com", "murali.r@agaramtech.com", str(mail))
server.close()
