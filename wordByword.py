'''
Kendra Lepage
text file word by word
phone number from command line
/this is for rachel/
'''
import os
from time import sleep
from subprocess import Popen, PIPE
def send_Message():
    getFile=input(str("Enter file name: "))
    infile=open(getFile, 'r')
    number=input(str("Enter phone number"))
    for line in infile:
        words=line.split()
        for var in words: 
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
           sleep(0.1)

send_Message()
