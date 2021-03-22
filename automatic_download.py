import json
import time
import os
import os.path
import optparse
import sys
import zipfile
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

def summary_writting(file_name, string_to_search,file,title):
    file.write('====================================\n')
    file.write(title + ': \n')
    matched_lines = search_string_in_file(file_name,string_to_search)
    if len(matched_lines) == 0:
        file.write('no data downloaded\n')
    else:
        for elem in matched_lines:
            file.write(elem[1])
            file.write('\n')


line_search = 'product saved as :'

date1 = (datetime.datetime.now() - datetime.timedelta(days=8)).date().strftime('%Y-%m-%d')
date2 = (datetime.datetime.now() - datetime.timedelta(days=1)).date().strftime('%Y-%m-%d')


os.chdir('/home/sarproz/Documents/auto_dl/')
f = open('download.out', 'w')
f.write('====================================\n')
f.write('Sent-1 download from: '+ date1 + ' to: ' + date2 + '\n')
f.write('====================================\n \n')


## Download of the different tracks here
f.write('====================================\n')
f.write('== Track 139  \n')
f.write('====================================\n')

os.system('/home/sarproz/miniconda3/bin/python /home/sarproz/PycharmProjects/peps_download/peps_download.py -a /home/sarproz/PycharmProjects/peps_download/peps.txt -c S1 -w /data1/TRACK_139/S1A_401 -p SLC --sat S1A -m IW -o 139 -x -l Aalborg > /home/sarproz/Documents/auto_dl/cron.log 2>&1')
summary_writting('/home/sarproz/Documents/auto_dl/cron.log',line_search,f,'S1A 139 401')
os.system('/home/sarproz/miniconda3/bin/python /home/sarproz/PycharmProjects/peps_download/peps_download.py -a /home/sarproz/PycharmProjects/peps_download/peps.txt -c S1 -w /data1/TRACK_139/S1A_406 -p SLC --sat S1A -m IW -o 139 -x -l Aarhus > /home/sarproz/Documents/auto_dl/cron.log 2>&1')
summary_writting('/home/sarproz/Documents/auto_dl/cron.log',line_search,f,'S1A 139 406')

os.system('/home/sarproz/miniconda3/bin/python /home/sarproz/PycharmProjects/peps_download/peps_download.py -a /home/sarproz/PycharmProjects/peps_download/peps.txt -c S1 -w /data1/TRACK_139/S1B_399 -p SLC --sat S1B -m IW -o 139 -x --lat 57.72137 --lon 10.58471 > /home/sarproz/Documents/auto_dl/cron.log 2>&1')
summary_writting('/home/sarproz/Documents/auto_dl/cron.log',line_search,f,'S1B 139 399')
os.system('/home/sarproz/miniconda3/bin/python /home/sarproz/PycharmProjects/peps_download/peps_download.py -a /home/sarproz/PycharmProjects/peps_download/peps.txt -c S1 -w /data1/TRACK_139/S1B_404 -p SLC --sat S1B -m IW -o 139 -x -l Aarhus > /home/sarproz/Documents/auto_dl/cron.log 2>&1')
summary_writting('/home/sarproz/Documents/auto_dl/cron.log',line_search,f,'S1B 139 404')

f.write('\n====================================\n')
f.write('== Track 66 \n')
f.write('====================================\n')
os.system('/home/sarproz/miniconda3/bin/python /home/sarproz/PycharmProjects/peps_download/peps_download.py -a /home/sarproz/PycharmProjects/peps_download/peps.txt -c S1 -w /data1/TRACK_66/S1A_409 -p SLC --sat S1A -m IW -o 66 -x --lat 55.433012 --lon 11.553367 > /home/sarproz/Documents/auto_dl/cron.log 2>&1')
summary_writting('/home/sarproz/Documents/auto_dl/cron.log',line_search,f,'S1A 66 409')
os.system('/home/sarproz/miniconda3/bin/python /home/sarproz/PycharmProjects/peps_download/peps_download.py -a /home/sarproz/PycharmProjects/peps_download/peps.txt -c S1 -w /data1/TRACK_66/S1A_404 -p SLC --sat S1A -m IW -o 66 -x --lat  55.779343 --lon 12.526074 > /home/sarproz/Documents/auto_dl/cron.log 2>&1')
summary_writting('/home/sarproz/Documents/auto_dl/cron.log',line_search,f,'S1A 66 404')
os.system('/home/sarproz/miniconda3/bin/python /home/sarproz/PycharmProjects/peps_download/peps_download.py -a /home/sarproz/PycharmProjects/peps_download/peps.txt -c S1 -w /data1/TRACK_66/S1A_409 -p SLC --sat S1B -m IW -o 66 -x --lat 55.433012 --lon 11.553367 > /home/sarproz/Documents/auto_dl/cron.log 2>&1')
summary_writting('/home/sarproz/Documents/auto_dl/cron.log',line_search,f,'S1B 66 406')

f.close()

# Sending summary mail
mail_content = "Processing finished"

# The mail addresses and password
sender_address = 'vincent.phelep.automail@gmail.com'
sender_pass = 'Geopartner2020'
receiver_address = 'vip@geopartner.dk'

# Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
#message['Subject'] = 'Track ' + track + ' finished processing'   #The subject line


# The body and the attachments for the mail

#message.attach(MIMEText(mail_content, 'plain'))

with open('download.out') as fp:
    # Create a text/plain message
    message = MIMEText(fp.read())

message['Subject'] = 'S1 data download'   #The subject line
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')

print(0)