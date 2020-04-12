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
    getFile=input(str("Enter file name: ")) #get file
    infile=open(getFile, 'r') #open file
    number=input(str("Enter phone number")) #get number
    for line in infile: #go through lines
        words=line.split() #split lines
        for var in words: #go through words in lines
           #start applescript
           scpt = '''on run {targetBuddyPhone, targetMessage} 
            tell application "Messages"
            set targetService to 1st service whose service type = iMessage
            set targetBuddy to buddy targetBuddyPhone of targetService
            send targetMessage to targetBuddy
            end tell
            end run''' #end applescript
           args = [number, words] #command line arguments to be supplied
           p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
           stdout, stderr = p.communicate(scpt) #run it
           sleep(0.1) #delay

send_Message() #full send
