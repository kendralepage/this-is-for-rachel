
'''
Kendra Lepage
Send full text with number input
/double cheeked up/

'''
import os
from time import sleep
from subprocess import Popen, PIPE
def send_Message():
    getFile=input(str("Enter file name: "))
    infile=open(getFile, 'r')
    number=input(str("Enter phone number: "))
    words=infile.read()
    scpt = '''on run {targetBuddyPhone, targetMessage}
            tell application "Messages"
            set targetService to 1st service whose service type = iMessage
            set targetBuddy to buddy targetBuddyPhone of targetService
            send targetMessage to targetBuddy
            end tell
            end run'''
    args = [number, words]
    p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(scpt)
           

           

send_Message()
