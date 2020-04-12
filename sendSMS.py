'''
Kendra Lepage
text file line by line
phone number from command line
/this is for rachel/
'''
'''import os
from time import sleep
from subprocess import Popen, PIPE
def send_Message():
    getFile=input(str("Enter file name: "))
    infile=open(getFile, 'r')
    number=input(str("Enter phone number"))
    for line in infile:
        words=line.split()
        for var in words: 
           scpt = ''''''on run {targetBuddyPhone, targetMessage}
            tell application "Messages"
            set targetService to 1st service whose service type = iMessage
            set targetBuddy to buddy targetBuddyPhone of targetService
            send targetMessage to targetBuddy
            end tell
            end run''''''
           args = [number, words]
           p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
           stdout, stderr = p.communicate(scpt)
           sleep(0.1)

send_Message()

'''

'''
Kendra Lepage
Send full text with number input
/double cheeked up/
'''
'''
import os
from time import sleep
from subprocess import Popen, PIPE
def send_Message():
    getFile=input(str("Enter file name: "))
    infile=open(getFile, 'r')
    number=input(str("Enter phone number: "))
    words=infile.read()
    scpt = ''''''on run {targetBuddyPhone, targetMessage}
            tell application "Messages"
            set targetService to 1st service whose service type = iMessage
            set targetBuddy to buddy targetBuddyPhone of targetService
            send targetMessage to targetBuddy
            end tell
            end run''''''
    args = [number, words]
    p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(scpt)
           

           

send_Message()'''
'''
Kendra LePage
Spam imeesages from file
/real hot girl sh*t/
'''

import os
from subprocess import Popen, PIPE
def send_Message():
    try:
        getFile=input(str("Enter file name: ")) #get file to send
        infile=open(getFile, 'r') #open file to read
        getPhone=input(str("Enter phone number file name: ")) #get phone file
        number=open(getPhone, 'r') #open phone number file
        words=infile.read() #create message to send
        for phone in number:
            numbies=phone.strip() # remove white spaces to send
            scpt = '''on run {targetBuddyPhone, targetMessage}
                tell application "Messages"
                set targetService to 1st service whose service type = iMessage
                set targetBuddy to buddy targetBuddyPhone of targetService
                send targetMessage to targetBuddy
                end tell
                end run'''
            args = [numbies, words] #phone number to send to, message
            p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            stdout, stderr = p.communicate(scpt) #add args
    except IOerror as err:
        print("Cannot find file")

send_Message() #full send
