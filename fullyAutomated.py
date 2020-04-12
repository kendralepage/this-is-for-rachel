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
